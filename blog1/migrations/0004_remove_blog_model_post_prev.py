# Generated by Django 3.0.4 on 2020-04-21 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0003_blog_model_post_prev'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_model',
            name='post_prev',
        ),
    ]
