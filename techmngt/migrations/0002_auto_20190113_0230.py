# Generated by Django 2.1.5 on 2019-01-13 02:30

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techmngt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asynchronousflow',
            name='description',
            field=markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='historicalasynchronousflow',
            name='description',
            field=markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='historicalbatchflow',
            name='description',
            field=markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='historicalnetworkflow',
            name='description',
            field=markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='historicalprotocol',
            name='description',
            field=markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='historicalserver',
            name='description',
            field=markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='historicalservertype',
            name='description',
            field=markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='historicaltechflow',
            name='description',
            field=markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='historicaluriflow',
            name='description',
            field=markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='networkflow',
            name='description',
            field=markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='protocol',
            name='description',
            field=markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='server',
            name='description',
            field=markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='servertype',
            name='description',
            field=markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='techflow',
            name='description',
            field=markdownx.models.MarkdownxField(help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description'),
        ),
    ]
