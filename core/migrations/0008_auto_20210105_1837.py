# Generated by Django 3.0.8 on 2021-01-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201230_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='cross1A',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Cross  Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='punizioni_difensive1A',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Punizioni difensive  Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='punizioni_offensive1A',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Punzioni offensive Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='tiri_in_fuori1A',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tiri in fuori Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='tiri_in_porta1A',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tiri in porta Primo Tempo Squadra A'),
        ),
    ]