# Generated by Django 3.0.8 on 2021-01-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210107_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='cornersA',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale corners Equipo A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='cornersB',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale cornerns Equipo B'),
        ),
        migrations.AddField(
            model_name='stats',
            name='crossA',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale cross Equipo A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='crossB',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale cross Equipo B'),
        ),
        migrations.AddField(
            model_name='stats',
            name='fuorigiocoA',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale fuorigioco Equipo A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='fuorigiocoB',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale fuorigioco Equipo B'),
        ),
        migrations.AddField(
            model_name='stats',
            name='parateA',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale parate Equipo A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='parateB',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale parate Equipo B'),
        ),
        migrations.AddField(
            model_name='stats',
            name='punizioni_difensiveA',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale punizioni difensive Equipo A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='punizioni_difensiveB',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale punizioni difensive Equipo B'),
        ),
        migrations.AddField(
            model_name='stats',
            name='punizioni_offensiveA',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale punizioni offensive Equipo A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='punizioni_offensiveB',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale punizioni offensive Equipo B'),
        ),
        migrations.AddField(
            model_name='stats',
            name='tiri_in_fuoriA',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale tiri in fuori Equipo A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='tiri_in_fuoriB',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale tiri in fuori Equipo B'),
        ),
        migrations.AddField(
            model_name='stats',
            name='tiri_in_portaA',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale tiri in porta Equipo A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='tiri_in_portaB',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Totale tiri in porta Equipo B'),
        ),
    ]
