# Generated by Django 3.0.8 on 2020-12-23 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='first_half',
            field=models.TimeField(blank=True, max_length=200, null=True, verbose_name='Primo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='possession1A',
            field=models.TimeField(blank=True, max_length=200, null=True, verbose_name='Possesso Palla Squadra A Primo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='possession1B',
            field=models.TimeField(blank=True, max_length=200, null=True, verbose_name='Possesso Palla Squadra B Primo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='possession2A',
            field=models.TimeField(blank=True, max_length=200, null=True, verbose_name='Possesso Palla Squadra A Secondo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='possession2B',
            field=models.TimeField(blank=True, max_length=200, null=True, verbose_name='Possesso Palla Squadra B Secondo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='second_half',
            field=models.TimeField(blank=True, max_length=200, null=True, verbose_name='Secondo Tempo'),
        ),
    ]
