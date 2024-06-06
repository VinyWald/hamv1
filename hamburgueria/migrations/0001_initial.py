# Generated by Django 4.2.7 on 2023-11-14 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('pao', models.CharField(max_length=100)),
                ('carne', models.CharField(max_length=100)),
                ('opcionais', models.CharField(max_length=100)),
                ('dataPedido', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Em andamento', 'Em andamento'), ('Concluído', 'Concluído'), ('Cancelado', 'Cancelado')], default='Em andamento', max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
