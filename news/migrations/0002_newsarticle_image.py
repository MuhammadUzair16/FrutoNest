# Generated by Django 5.0.7 on 2024-07-21 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='image',
            field=models.ImageField(default='news_images/', upload_to=''),
        ),
    ]