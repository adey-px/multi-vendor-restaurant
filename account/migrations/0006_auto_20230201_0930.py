# Generated by Django 3.2.5 on 2023-02-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='users/cover_images'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='users/profile_images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Restaurant'), (2, 'Customer')], null=True),
        ),
    ]
