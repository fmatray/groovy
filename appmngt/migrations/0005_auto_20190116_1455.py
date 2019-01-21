# Generated by Django 2.1.4 on 2019-01-16 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmngt', '0004_auto_20190114_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='pin',
            field=models.BooleanField(default=False, verbose_name='Pin'),
        ),
        migrations.AddField(
            model_name='environment',
            name='pin',
            field=models.BooleanField(default=False, verbose_name='Pin'),
        ),
        migrations.AddField(
            model_name='historicalapplication',
            name='pin',
            field=models.BooleanField(default=False, verbose_name='Pin'),
        ),
        migrations.AddField(
            model_name='historicalenvironment',
            name='pin',
            field=models.BooleanField(default=False, verbose_name='Pin'),
        ),
        migrations.AddField(
            model_name='historicalpartner',
            name='pin',
            field=models.BooleanField(default=False, verbose_name='Pin'),
        ),
        migrations.AddField(
            model_name='historicalrelease',
            name='pin',
            field=models.BooleanField(default=False, verbose_name='Pin'),
        ),
        migrations.AddField(
            model_name='historicalunivers',
            name='pin',
            field=models.BooleanField(default=False, verbose_name='Pin'),
        ),
        migrations.AddField(
            model_name='partner',
            name='pin',
            field=models.BooleanField(default=False, verbose_name='Pin'),
        ),
        migrations.AddField(
            model_name='release',
            name='pin',
            field=models.BooleanField(default=False, verbose_name='Pin'),
        ),
        migrations.AddField(
            model_name='univers',
            name='pin',
            field=models.BooleanField(default=False, verbose_name='Pin'),
        ),
    ]
