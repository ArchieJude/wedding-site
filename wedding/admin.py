import csv
from django.contrib import admin
from django.db.models import Sum, Count, Q
from django.http import HttpResponse
from django.utils.html import format_html
from .models import RSVP, GalleryPhoto, ScheduleEvent


def export_rsvps_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="rsvps.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Attending', 'Party Size', 'Guest Names', 'Dietary Notes', 'Song Request', 'Message', 'Submitted'])
    for r in queryset:
        writer.writerow([
            r.name, r.email, r.get_attendance_display(),
            r.number_in_party, ', '.join(r.guest_names), r.dietary_notes,
            r.song_request, r.message,
            r.submitted_at.strftime('%Y-%m-%d %H:%M'),
        ])
    return response

export_rsvps_csv.short_description = 'Export selected RSVPs to CSV'


@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'attendance', 'number_in_party', 'guest_names_display', 'submitted_at']
    list_filter = ['attendance']
    search_fields = ['name', 'email']
    readonly_fields = ['submitted_at']
    date_hierarchy = 'submitted_at'
    actions = [export_rsvps_csv]

    def guest_names_display(self, obj):
        return ', '.join(obj.guest_names) if obj.guest_names else '—'
    guest_names_display.short_description = 'Guests'

    def changelist_view(self, request, extra_context=None):
        qs = self.get_queryset(request)
        totals = qs.aggregate(
            total=Count('id'),
            attending=Count('id', filter=Q(attendance='yes')),
            declining=Count('id', filter=Q(attendance='no')),
            headcount=Sum('number_in_party', filter=Q(attendance='yes')),
        )
        extra_context = extra_context or {}
        extra_context['rsvp_summary'] = totals
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'order']
    list_editable = ['order']


@admin.register(ScheduleEvent)
class ScheduleEventAdmin(admin.ModelAdmin):
    list_display = ['time', 'title', 'location', 'order']
    list_editable = ['order']
