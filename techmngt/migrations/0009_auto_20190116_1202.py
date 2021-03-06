# Generated by Django 2.1.4 on 2019-01-16 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techmngt', '0008_auto_20190115_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalprotocol',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='historicalprotocol',
            name='documentation',
        ),
        migrations.RemoveField(
            model_name='historicalprotocol',
            name='status',
        ),
        migrations.RemoveField(
            model_name='historicalservertype',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='historicalservertype',
            name='documentation',
        ),
        migrations.RemoveField(
            model_name='historicalservertype',
            name='status',
        ),
        migrations.RemoveField(
            model_name='protocol',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='protocol',
            name='documentation',
        ),
        migrations.RemoveField(
            model_name='protocol',
            name='status',
        ),
        migrations.RemoveField(
            model_name='protocol',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='servertype',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='servertype',
            name='documentation',
        ),
        migrations.RemoveField(
            model_name='servertype',
            name='status',
        ),
        migrations.RemoveField(
            model_name='servertype',
            name='tags',
        ),
        migrations.AlterField(
            model_name='asynchronousflow',
            name='protocol',
            field=models.ForeignKey(limit_choices_to={'type': 'Asynchronous'}, on_delete=django.db.models.deletion.PROTECT, related_name='asynchronousflow_protocol', to='techmngt.Protocol', verbose_name='Protocol'),
        ),
        migrations.AlterField(
            model_name='historicalasynchronousflow',
            name='protocol',
            field=models.ForeignKey(blank=True, db_constraint=False, limit_choices_to={'type': 'Asynchronous'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='techmngt.Protocol', verbose_name='Protocol'),
        ),
        migrations.AlterField(
            model_name='historicalserver',
            name='server_type',
            field=models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='techmngt.ServerType', verbose_name='Server Type'),
        ),
        migrations.AlterField(
            model_name='historicalsynchronousflow',
            name='protocol',
            field=models.ForeignKey(blank=True, db_constraint=False, limit_choices_to={'type': 'Synchronous'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='techmngt.Protocol', verbose_name='Protocol'),
        ),
        migrations.AlterField(
            model_name='server',
            name='server_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='server_servertype', to='techmngt.ServerType', verbose_name='Server Type'),
        ),
        migrations.AlterField(
            model_name='synchronousflow',
            name='protocol',
            field=models.ForeignKey(limit_choices_to={'type': 'Synchronous'}, on_delete=django.db.models.deletion.PROTECT, related_name='synchronousflow_protocol', to='techmngt.Protocol', verbose_name='Protocol'),
        ),
    ]
