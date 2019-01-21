# Generated by Django 2.1.4 on 2019-01-14 15:55

from django.db import migrations, models
import django_cryptography.fields
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('funcmngt', '0003_auto_20190114_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcflow',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='funcflow',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='funcflow',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicalfuncflow',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicalfuncflow',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicalfuncflow',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicalsubfuncflow',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicalsubfuncflow',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicalsubfuncflow',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='subfuncflow',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='subfuncflow',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='subfuncflow',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
    ]
