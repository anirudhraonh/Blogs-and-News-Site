# Generated by Django 5.0.3 on 2024-04-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_blogpost_image_small'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
