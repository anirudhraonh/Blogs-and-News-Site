# Generated by Django 5.0.3 on 2024-04-06 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_commentmodelform_comment_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodelform',
            name='comment_on',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_for', to='blogs.blogpost'),
        ),
    ]
