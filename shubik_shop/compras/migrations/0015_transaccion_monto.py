# Generated by Django 5.1.1 on 2024-10-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0014_transaccion_token_ws'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='monto',
            field=models.IntegerField(default=9999),
            preserve_default=False,
        ),
    ]
