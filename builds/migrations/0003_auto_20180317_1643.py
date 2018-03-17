# Generated by Django 2.0.3 on 2018-03-17 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0002_specializations_build_usage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specializations',
            name='major1_1',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='major1_2',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='major1_3',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='major2_1',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='major2_2',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='major2_3',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='major3_1',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='major3_2',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='major3_3',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='minor1_1',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='minor1_2',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='minor1_3',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='minor2_1',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='minor2_2',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='minor2_3',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='minor3_1',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='minor3_2',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='minor3_3',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='skill0',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='skill1',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='skill2',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='skill3',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='skill4',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='skill5',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='skill6',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='skill7',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='skill8',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='skill9',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='spec1',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='spec2',
        ),
        migrations.RemoveField(
            model_name='specializations',
            name='spec3',
        ),
        migrations.AddField(
            model_name='specializations',
            name='skills',
            field=models.CharField(max_length=23, null=True, verbose_name='Skills, Deltaconnected-style decoded(Base64)'),
        ),
        migrations.AddField(
            model_name='specializations',
            name='traits',
            field=models.CharField(max_length=27, null=True, verbose_name='Traits, Deltaconnected-style decoded(Base64)'),
        ),
    ]