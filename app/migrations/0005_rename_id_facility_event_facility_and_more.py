# Generated by Django 5.0.7 on 2024-08-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_profile_birth_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='id_facility',
            new_name='facility',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='id_organizer',
            new_name='organizer',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='profile_pictures/default_profile_picture.jpg', upload_to='profile_pictures'),
        ),
    ]