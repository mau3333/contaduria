# Generated by Django 5.0.4 on 2024-04-24 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0010_remove_contaduria_valor_bono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contaduria',
            name='id_contaduria',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
