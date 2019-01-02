# Generated by Django 2.1.4 on 2019-01-02 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appmngt', '0001_initial'),
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FuncFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('On going', 'On going'), ('Released', 'Released'), ('Retired', 'Retired'), ('Abort', 'Abort')], default='Draft', max_length=20)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('flow_id', models.CharField(default='', max_length=64, unique=True, verbose_name='Flow ID')),
                ('type', models.CharField(choices=[('Asynchronous', 'Asynchronous'), ('Synchronous', 'Synchronous'), ('Redirection', 'Redirection')], max_length=32, verbose_name='Type')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Functional flow',
            },
        ),
        migrations.CreateModel(
            name='HistoricalFuncFlow',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Name')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('On going', 'On going'), ('Released', 'Released'), ('Retired', 'Retired'), ('Abort', 'Abort')], default='Draft', max_length=20)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('flow_id', models.CharField(db_index=True, default='', max_length=64, verbose_name='Flow ID')),
                ('type', models.CharField(choices=[('Asynchronous', 'Asynchronous'), ('Synchronous', 'Synchronous'), ('Redirection', 'Redirection')], max_length=32, verbose_name='Type')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Functional flow',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSubFuncFlow',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Name')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('On going', 'On going'), ('Released', 'Released'), ('Retired', 'Retired'), ('Abort', 'Abort')], default='Draft', max_length=20)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('subflow_id', models.CharField(db_index=True, default='', max_length=64, verbose_name='Sub flow ID')),
                ('vital', models.BooleanField(default=False, verbose_name='Vital')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('func_flow', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='funcmngt.FuncFlow', verbose_name='Functional Flow')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appmngt.Application', verbose_name='Receiver')),
                ('requester', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appmngt.Application', verbose_name='Requester')),
            ],
            options={
                'verbose_name': 'historical Sub functional flow',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='SubFuncFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('On going', 'On going'), ('Released', 'Released'), ('Retired', 'Retired'), ('Abort', 'Abort')], default='Draft', max_length=20)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('subflow_id', models.CharField(default='', max_length=64, unique=True, verbose_name='Sub flow ID')),
                ('vital', models.BooleanField(default=False, verbose_name='Vital')),
                ('func_flow', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subfuncflow_flow', to='funcmngt.FuncFlow', verbose_name='Functional Flow')),
                ('receiver', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subfuncflow_rec_app', to='appmngt.Application', verbose_name='Receiver')),
                ('requester', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subfuncflow_req_app', to='appmngt.Application', verbose_name='Requester')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Sub functional flow',
            },
        ),
    ]
