import json
import logging
import os
import urllib.error
import urllib.request
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import get_language
from .models import GalleryPhoto, ScheduleEvent, RSVP
from .forms import RSVPForm

logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'wedding/home.html')


def rsvp(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            rsvp = form.save(commit=False)
            rsvp.guest_names = [
                n.strip() for n in request.POST.getlist('guest_name') if n.strip()
            ]
            rsvp.save()
            _send_rsvp_notification(rsvp)
            messages.success(request, "Thank you! Your RSVP has been received.")
            return redirect('rsvp_confirm')
    else:
        form = RSVPForm()
    return render(request, 'wedding/rsvp.html', {'form': form})


def _send_rsvp_notification(rsvp):
    attending = rsvp.get_attendance_display()
    lines = [
        f"Name:        {rsvp.name}",
        f"Email:       {rsvp.email}",
        f"Attending:   {attending}",
    ]
    if rsvp.attendance == 'yes':
        lines.append(f"Party size:  {rsvp.number_in_party}")
    if rsvp.guest_names:
        for i, name in enumerate(rsvp.guest_names, 1):
            lines.append(f"Guest {i}:     {name}")
    if rsvp.dietary_notes:
        lines.append(f"Dietary:     {rsvp.dietary_notes}")
    if rsvp.message:
        lines.append(f"Message:     {rsvp.message}")

    subject = f"New RSVP: {rsvp.name} — {attending}"
    body = "\n".join(lines)

    # Railway blocks outbound SMTP, so in production we send over HTTPS via the
    # Resend API (set RESEND_API_KEY). Locally, with no key, fall back to SMTP.
    api_key = os.environ.get('RESEND_API_KEY')
    if api_key:
        _send_via_resend(api_key, subject, body)
    else:
        try:
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.RSVP_NOTIFICATION_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            logger.error("RSVP email failed (SMTP): %s", e)


def _send_via_resend(api_key, subject, body):
    payload = json.dumps({
        "from": os.environ.get('RESEND_FROM', 'onboarding@resend.dev'),
        "to": [settings.RSVP_NOTIFICATION_EMAIL],
        "subject": subject,
        "text": body,
    }).encode()
    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            resp.read()
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        logger.error("RSVP email failed (Resend %s): %s", e.code, detail)
    except Exception as e:
        logger.error("RSVP email failed (Resend): %s", e)


def rsvp_confirm(request):
    return render(request, 'wedding/rsvp_confirm.html')


def gallery(request):
    lang = get_language()
    photos = GalleryPhoto.objects.all()
    for photo in photos:
        if lang == 'zh-hant':
            photo.display_caption = photo.caption_zh_hant or photo.caption
        elif lang == 'mn':
            photo.display_caption = photo.caption_mn or photo.caption
        else:
            photo.display_caption = photo.caption
    return render(request, 'wedding/gallery.html', {'photos': photos})


def schedule(request):
    events = ScheduleEvent.objects.all()
    return render(request, 'wedding/schedule.html', {'events': events})


def travel(request):
    return render(request, 'wedding/travel.html')


def faq(request):
    return render(request, 'wedding/faq.html')
