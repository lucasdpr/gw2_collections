# Generated by Django 2.0.3 on 2018-03-15 00:55

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specializations',
            name='build_usage',
            field=djrichtextfield.models.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
