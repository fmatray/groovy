# Generated by Django 2.1.5 on 2019-01-04 23:06

import datetime

import django.db.models.deletion
import markdownx.models
import simple_history.models
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('On going', 'On going'), ('Released', 'Released'), ('Retired', 'Retired'), ('Abort', 'Abort')], default='Draft', max_length=20)),
                ('description', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
                ('documentation', models.URLField(blank=True, null=True, verbose_name='Documentation')),
                ('comment', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
            ],
            options={
                'verbose_name_plural': 'Applications',
            },
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('On going', 'On going'), ('Released', 'Released'), ('Retired', 'Retired'), ('Abort', 'Abort')], default='Draft', max_length=20)),
                ('description', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
                ('documentation', models.URLField(blank=True, null=True, verbose_name='Documentation')),
                ('comment', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('application', models.ForeignKey(blank=True, default=None, limit_choices_to={'status__in': ('On going', 'Released')}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='env_app', to='appmngt.Application', verbose_name='Application')),
            ],
            options={
                'verbose_name_plural': 'Environments',
            },
        ),
        migrations.CreateModel(
            name='HistoricalApplication',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Name')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('On going', 'On going'), ('Released', 'Released'), ('Retired', 'Retired'), ('Abort', 'Abort')], default='Draft', max_length=20)),
                ('description', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
                ('documentation', models.URLField(blank=True, null=True, verbose_name='Documentation')),
                ('comment', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical application',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalEnvironment',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('On going', 'On going'), ('Released', 'Released'), ('Retired', 'Retired'), ('Abort', 'Abort')], default='Draft', max_length=20)),
                ('description', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
                ('documentation', models.URLField(blank=True, null=True, verbose_name='Documentation')),
                ('comment', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('application', models.ForeignKey(blank=True, db_constraint=False, default=None, limit_choices_to={'status__in': ('On going', 'Released')}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appmngt.Application', verbose_name='Application')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical environment',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPartner',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Name')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('On going', 'On going'), ('Released', 'Released'), ('Retired', 'Retired'), ('Abort', 'Abort')], default='Draft', max_length=20)),
                ('description', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
                ('documentation', models.URLField(blank=True, null=True, verbose_name='Documentation')),
                ('comment', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical partner',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalRelease',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Name')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('On going', 'On going'), ('Released', 'Released'), ('Retired', 'Retired'), ('Abort', 'Abort')], default='Draft', max_length=20)),
                ('description', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
                ('documentation', models.URLField(blank=True, null=True, verbose_name='Documentation')),
                ('comment', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
                ('release_date', models.DateField(default=datetime.datetime.now, verbose_name='Release date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical release',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalUnivers',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Name')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('On going', 'On going'), ('Released', 'Released'), ('Retired', 'Retired'), ('Abort', 'Abort')], default='Draft', max_length=20)),
                ('description', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
                ('documentation', models.URLField(blank=True, null=True, verbose_name='Documentation')),
                ('comment', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical univers',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('On going', 'On going'), ('Released', 'Released'), ('Retired', 'Retired'), ('Abort', 'Abort')], default='Draft', max_length=20)),
                ('description', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
                ('documentation', models.URLField(blank=True, null=True, verbose_name='Documentation')),
                ('comment', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Partners',
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('On going', 'On going'), ('Released', 'Released'), ('Retired', 'Retired'), ('Abort', 'Abort')], default='Draft', max_length=20)),
                ('description', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
                ('documentation', models.URLField(blank=True, null=True, verbose_name='Documentation')),
                ('comment', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
                ('release_date', models.DateField(default=datetime.datetime.now, verbose_name='Release date')),
                ('applications', models.ManyToManyField(blank=True, default=None, limit_choices_to={'status__in': ('On going', 'Released')}, related_name='release_app', to='appmngt.Application', verbose_name='Applications')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Releases',
            },
        ),
        migrations.CreateModel(
            name='Univers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('On going', 'On going'), ('Released', 'Released'), ('Retired', 'Retired'), ('Abort', 'Abort')], default='Draft', max_length=20)),
                ('description', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", null=True, verbose_name='Description')),
                ('documentation', models.URLField(blank=True, null=True, verbose_name='Documentation')),
                ('comment', markdownx.models.MarkdownxField(blank=True, help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>", verbose_name='Comment')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Univers',
            },
        ),
        migrations.AddField(
            model_name='historicalapplication',
            name='partner',
            field=models.ForeignKey(blank=True, db_constraint=False, default=None, limit_choices_to={'status__in': ('On going', 'Released')}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appmngt.Partner', verbose_name='Partner'),
        ),
        migrations.AddField(
            model_name='historicalapplication',
            name='univers',
            field=models.ForeignKey(blank=True, db_constraint=False, default=None, limit_choices_to={'status__in': ('On going', 'Released')}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appmngt.Univers', verbose_name='Univers'),
        ),
    ]
