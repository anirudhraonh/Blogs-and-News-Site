# Generated by Django 5.0.3 on 2024-04-06 19:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_remove_commentmodelform_comment_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('comment_at', models.DateTimeField(auto_now=True)),
                ('comment_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_for', to='blogs.blogpost')),
            ],
        ),
        migrations.DeleteModel(
            name='CommentModelForm',
        ),
    ]
