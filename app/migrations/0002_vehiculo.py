# Generated by Django 3.2.3 on 2021-06-15 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Patente')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca Vehiculo')),
                ('modelo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Modelo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoria')),
            ],
        ),
    ]