# Generated by Django 3.2.4 on 2021-06-30 08:57

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='type',
            field=models.CharField(choices=[('PAINTING', 'Painting'), ('MUSIC', 'Music'), ('MOVIE', 'Movie'), ('BOOK', 'Book')], max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[1024, 1024], upload_to='books/covers/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='artwork_type',
            field=models.CharField(choices=[('PAINTING', 'Painting'), ('MUSIC', 'Music'), ('MOVIE', 'Movie'), ('BOOK', 'Book')], max_length=30),
        ),
    ]
