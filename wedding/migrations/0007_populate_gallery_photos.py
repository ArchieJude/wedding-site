from django.db import migrations


PHOTOS = [
    {'id': 1,  'image': 'gallery/IMG_9286.jpg',  'order': 1},
    {'id': 2,  'image': 'gallery/IMG_5220.jpg',  'order': 2},
    {'id': 3,  'image': 'gallery/IMG_8012.jpg',  'order': 3},
    {'id': 4,  'image': 'gallery/IMG_3586.jpg',  'order': 4},
    {'id': 5,  'image': 'gallery/IMG_1418.JPG',  'order': 5},
    {'id': 6,  'image': 'gallery/IMG_3643.jpg',  'order': 6},
    {'id': 7,  'image': 'gallery/IMG_2187.jpg',  'order': 7},
    {'id': 8,  'image': 'gallery/IMG_0230.jpg',  'order': 8},
    {'id': 9,  'image': 'gallery/IMG_8651.jpg',  'order': 9},
    {'id': 10, 'image': 'gallery/IMG_9634.jpg',  'order': 10},
    {'id': 11, 'image': 'gallery/IMG_9702.jpg',  'order': 11},
    {'id': 12, 'image': 'gallery/IMG_1268.jpg',  'order': 12},
    {'id': 13, 'image': 'gallery/IMG_1283.jpg',  'order': 13},
    {'id': 14, 'image': 'gallery/DSCF1609.jpg',  'order': 14},
    {'id': 15, 'image': 'gallery/IMG_0062.JPG',  'order': 15},
]


def populate_photos(apps, schema_editor):
    GalleryPhoto = apps.get_model('wedding', 'GalleryPhoto')
    if not GalleryPhoto.objects.exists():
        for p in PHOTOS:
            GalleryPhoto.objects.create(**p)


def remove_photos(apps, schema_editor):
    GalleryPhoto = apps.get_model('wedding', 'GalleryPhoto')
    GalleryPhoto.objects.filter(image__in=[p['image'] for p in PHOTOS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0006_gallery_caption_translations'),
    ]

    operations = [
        migrations.RunPython(populate_photos, remove_photos),
    ]
