# Generated by Django 2.1.2 on 2018-11-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]