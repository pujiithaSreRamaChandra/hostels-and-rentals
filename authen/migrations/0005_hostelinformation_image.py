# Generated by Django 4.2.6 on 2023-10-15 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0004_hostelinformation_rentalinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostelinformation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hostel_images/'),
        ),
    ]
