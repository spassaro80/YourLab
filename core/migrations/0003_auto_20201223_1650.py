# Generated by Django 3.0.8 on 2020-12-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201223_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stats',
            name='corners1',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='cross_cc1',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='cross_dx1',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='cross_sx1',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='fuorigioco1',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='parate1',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='punizioni_difensive1_cc',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='punizioni_difensive1_dx',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='punizioni_difensive1_sx',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='punizioni_offensive1_cc',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='punizioni_offensive1_dx',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='punizioni_offensive1_sx',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='tiri_in_fuori1_cc',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='tiri_in_fuori1_dx',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='tiri_in_fuori1_sx',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='tiri_in_porta1_cc',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='tiri_in_porta1_dx',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='tiri_in_porta1_sx',
        ),
        migrations.AddField(
            model_name='stats',
            name='corners1A',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name="Calci d'angolo Primo Tempo Squadra A"),
        ),
        migrations.AddField(
            model_name='stats',
            name='cross_cc1A',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Cross al centro Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='cross_dx1A',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Cross a destra Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='cross_sx1A',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Cross a sinistra Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='fuorigioco1A',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Fuorigioco Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='parate1A',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Parate Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='punizioni_difensive1A_cc',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Punizioni difensive al centro Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='punizioni_difensive1A_dx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Punizioni difensive a destra Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='punizioni_difensive1A_sx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Punizioni difensive a sinistra Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='punizioni_offensive1A_cc',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Punzioni offensive al centro Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='punizioni_offensive1A_dx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Punzioni offensive a destra Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='punizioni_offensive1A_sx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Punzioni offensive a sinistra Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='tiri_in_fuori1A_cc',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tiri in fuori al centro Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='tiri_in_fuori1A_dx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tiri in fuori a destra Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='tiri_in_fuori1A_sx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tiri in fuori a sinistra Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='tiri_in_porta1A_cc',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tiri in porta al centro Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='tiri_in_porta1A_dx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tiri in porta a destra Primo Tempo Squadra A'),
        ),
        migrations.AddField(
            model_name='stats',
            name='tiri_in_porta1A_sx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tiri in porta a sinistra Primo Tempo Squadra A'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='corners2',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name="Calci d'angolo Secondo Tempo"),
        ),
        migrations.AlterField(
            model_name='stats',
            name='cross_cc2',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Cross al centro SecondoTempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='cross_dx2',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Cross a destra Secondo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='cross_sx2',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Cross a sinistra Secondo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='fuorigioco2',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Fuorigioco Secondo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='parate2',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Parate Secondo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='punizioni_difensive2_cc',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Punizioni difensive al centro SecondoTempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='punizioni_difensive2_dx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Punizioni difensive a destra Secondo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='punizioni_difensive2_sx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Punizioni difensive a sinistra Secondo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='punizioni_offensive2_cc',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Punzioni offensive al centro SecondoTempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='punizioni_offensive2_dx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Punzioni offensive a destra Secondo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='punizioni_offensive2_sx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Punzioni offensive a sinistra Secondo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='tiri_in_fuori2_cc',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tiri in fuori al centro SecondoTempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='tiri_in_fuori2_dx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tiri in fuori a destra Secondo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='tiri_in_fuori2_sx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tiri in fuori a sinistra Secondo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='tiri_in_porta2_cc',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tiri in porta al centro SecondoTempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='tiri_in_porta2_dx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tiri in porta a destra Secondo Tempo'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='tiri_in_porta2_sx',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tiri in porta a sinistra Secondo Tempo'),
        ),
    ]
