# Generated by Django 4.2.15 on 2025-01-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0021_applicationpublicaccessclient_client_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='tts_autoplay',
            field=models.BooleanField(default=False, verbose_name='自动播放'),
        ),
    ]