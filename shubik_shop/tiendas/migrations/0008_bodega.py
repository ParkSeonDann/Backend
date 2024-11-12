# Generated by Django 5.1.1 on 2024-10-16 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_remove_producto_usuario_id_producto_tienda_id'),
        ('tiendas', '0007_remove_tienda_sector_remove_tienda_tamano_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('bodega_id', models.AutoField(primary_key=True, serialize=False)),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('tienda_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendas.tienda')),
            ],
        ),
    ]
