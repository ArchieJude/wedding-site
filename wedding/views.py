from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import GalleryPhoto, ScheduleEvent, RSVP
from .forms import RSVPForm


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
    if rsvp.song_request:
        lines.append(f"Song:        {rsvp.song_request}")
    if rsvp.message:
        lines.append(f"Message:     {rsvp.message}")

    send_mail(
        subject=f"New RSVP: {rsvp.name} — {attending}",
        message="\n".join(lines),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.RSVP_NOTIFICATION_EMAIL],
        fail_silently=True,  # never break the RSVP flow if email fails
    )


def rsvp_confirm(request):
    return render(request, 'wedding/rsvp_confirm.html')


def gallery(request):
    photos = GalleryPhoto.objects.all()
    return render(request, 'wedding/gallery.html', {'photos': photos})


def schedule(request):
    events = ScheduleEvent.objects.all()
    return render(request, 'wedding/schedule.html', {'events': events})


def travel(request):
    return render(request, 'wedding/travel.html')


def faq(request):
    return render(request, 'wedding/faq.html')
