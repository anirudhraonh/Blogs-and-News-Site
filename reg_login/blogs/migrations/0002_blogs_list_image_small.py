# Generated by Django 5.0.3 on 2024-04-03 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs_list',
            name='image_small',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
