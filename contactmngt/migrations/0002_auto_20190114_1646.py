# Generated by Django 2.1.4 on 2019-01-14 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appmngt', '0003_auto_20190113_0230'),
        ('contactmngt', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalperson',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Person'},
        ),
        migrations.AlterModelOptions(
            name='historicalteam',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Team'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'Persons'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Team', 'verbose_name_plural': 'Teams'},
        ),
        migrations.AlterField(
            model_name='person',
            name='team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='person_team', to='contactmngt.Team', verbose_name='Team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='partner',
            field=models.ForeignKey(default=None, limit_choices_to={'status__in': ('On going', 'Released')}, on_delete=django.db.models.deletion.PROTECT, related_name='team_partner', to='appmngt.Partner', verbose_name='Partner'),
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together={('name', 'departement', 'partner')},
        ),
    ]
