# Generated by Django 5.1.1 on 2024-10-14 04:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_alter_puja_monto'),
        ('tiendas', '0004_remove_tienda_id_tienda_password_tienda_tienda_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subasta',
            name='tienda_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tiendas.tienda'),
            preserve_default=False,
        ),
    ]