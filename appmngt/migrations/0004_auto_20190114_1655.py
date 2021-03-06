# Generated by Django 2.1.4 on 2019-01-14 15:55

from django.db import migrations, models
import django_cryptography.fields
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('appmngt', '0003_auto_20190113_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='application',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='application',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='environment',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='environment',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='environment',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicalapplication',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicalapplication',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicalapplication',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicalenvironment',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicalenvironment',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicalenvironment',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicalpartner',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicalpartner',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicalpartner',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicalrelease',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicalrelease',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicalrelease',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicalunivers',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicalunivers',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicalunivers',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='partner',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='partner',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='partner',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='release',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='release',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='release',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='univers',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='univers',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='univers',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
    ]
