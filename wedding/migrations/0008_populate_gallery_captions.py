from django.db import migrations


CAPTIONS = {
    'gallery/IMG_9286.jpg': 'Angels Landing, Zion National Park — our first big adventure together, 2021',
    'gallery/IMG_5220.jpg': 'Camping in the Catskills, autumn 2022',
    'gallery/IMG_8012.jpg': "Erdene Zuu Monastery, Mongolia — Ariel meets Archie's home country, 2023",
    'gallery/IMG_3586.jpg': 'Somewhere in the Mongolian steppe, 2023',
    'gallery/IMG_1418.JPG': 'Elephant Mountain, Taipei — the trip that made us fall in love with Taiwan, 2024',
    'gallery/IMG_3643.jpg': 'Above the snowline, Crested Butte, Colorado, 2024',
    'gallery/IMG_2187.jpg': 'Trout fishing at a mountain lake, Rocky Mountain National Park, 2024',
    'gallery/IMG_0230.jpg': 'Snowboarding in Breckenridge, 2025',
    'gallery/IMG_8651.jpg': 'Under the arch, Arches National Park, Moab, 2025',
    'gallery/IMG_9634.jpg': 'Sunset at Rialto Beach, Olympic Peninsula, 2025',
    'gallery/IMG_9702.jpg': 'Hoh Rainforest, Olympic National Park, 2025',
    'gallery/IMG_1268.jpg': 'The proposal — Big Island, Hawaii, December 2025',
    'gallery/IMG_1283.jpg': 'The cowrie shell and the ring',
    'gallery/DSCF1609.jpg': 'Engagement shoot, Big Island, Hawaii, December 2025',
    'gallery/IMG_0062.JPG': 'Giant tortoise spotting in the Galápagos with family, 2026',
}


def set_captions(apps, schema_editor):
    GalleryPhoto = apps.get_model('wedding', 'GalleryPhoto')
    for image, caption in CAPTIONS.items():
        GalleryPhoto.objects.filter(image=image).update(caption=caption)


def clear_captions(apps, schema_editor):
    GalleryPhoto = apps.get_model('wedding', 'GalleryPhoto')
    GalleryPhoto.objects.filter(image__in=CAPTIONS.keys()).update(caption='')


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0007_populate_gallery_photos'),
    ]

    operations = [
        migrations.RunPython(set_captions, clear_captions),
    ]
