from django.shortcuts import render, redirect
from django.contrib import messages
from .models import GalleryPhoto, ScheduleEvent, RSVP
from .forms import RSVPForm


def home(request):
    return render(request, 'wedding/home.html')


def rsvp(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your RSVP has been received.")
            return redirect('rsvp_confirm')
    else:
        form = RSVPForm()
    return render(request, 'wedding/rsvp.html', {'form': form})


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
