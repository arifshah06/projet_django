# Generated by Django 5.1 on 2024-09-10 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('paye', models.CharField(choices=[('OUI', 'Oui'), ('NON', 'Non')], default='Non', max_length=9)),
                ('cout', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=60)),
                ('mdp', models.CharField(max_length=60)),
                ('question', models.CharField(max_length=60)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('abonnement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.abonnement')),
            ],
        ),
        migrations.AddField(
            model_name='abonnement',
            name='paiement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.paiement'),
        ),
    ]
