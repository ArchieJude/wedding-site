from django.db import models
from django.utils.translation import gettext_lazy as _


class RSVP(models.Model):
    ATTENDANCE_CHOICES = [
        ('yes', _('Joyfully accepts')),
        ('no', _('Regretfully declines')),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    attendance = models.CharField(max_length=13, choices=ATTENDANCE_CHOICES)
    number_in_party = models.PositiveIntegerField(default=1)
    guest_names = models.JSONField(default=list, blank=True)
    dietary_notes = models.TextField(blank=True)
    plus_one_dietary_notes = models.TextField(blank=True)
    song_request = models.CharField(max_length=300, blank=True)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'RSVP'
        verbose_name_plural = 'RSVPs'

    def __str__(self):
        return f"{self.name} — {self.get_attendance_display()}"


class GalleryPhoto(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=300, blank=True)
    caption_zh_hant = models.CharField(max_length=300, blank=True, verbose_name='Caption (中文)')
    caption_mn = models.CharField(max_length=300, blank=True, verbose_name='Caption (Монгол)')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.caption or f"Photo {self.id}"


class ScheduleEvent(models.Model):
    time = models.TimeField()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'time']

    def __str__(self):
        return f"{self.time.strftime('%I:%M %p')} — {self.title}"
