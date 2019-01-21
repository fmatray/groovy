# Generated by Django 2.1.4 on 2019-01-14 15:55

from django.db import migrations, models
import django_cryptography.fields
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('techmngt', '0004_auto_20190114_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asynchronousflow',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='asynchronousflow',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='asynchronousflow',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicalasynchronousflow',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicalasynchronousflow',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicalasynchronousflow',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicalbatchflow',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicalbatchflow',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicalbatchflow',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicalnetworkflow',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicalnetworkflow',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicalnetworkflow',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicalprotocol',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicalprotocol',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicalprotocol',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicalserver',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicalserver',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicalserver',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicalservertype',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicalservertype',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicalservertype',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicaltechflow',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicaltechflow',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicaltechflow',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='historicaluriflow',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='historicaluriflow',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='historicaluriflow',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='networkflow',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='networkflow',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='networkflow',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='protocol',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='protocol',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='protocol',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='server',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='server',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='server',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='servertype',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='servertype',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='servertype',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
        migrations.AlterField(
            model_name='techflow',
            name='comment',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
        ),
        migrations.AlterField(
            model_name='techflow',
            name='description',
            field=django_cryptography.fields.encrypt(markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
        ),
        migrations.AlterField(
            model_name='techflow',
            name='documentation',
            field=django_cryptography.fields.encrypt(models.URLField(blank=True, null=True, verbose_name='Documentation')),
        ),
    ]
