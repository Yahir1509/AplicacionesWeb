# Generated by Django 5.1.3 on 2024-11-20 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedagogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePedagogo', models.CharField(max_length=255)),
                ('numeroTrabajador', models.CharField(max_length=20, unique=True)),
                ('bActivo', models.BooleanField(null=True)),
            ],
        ),
    ]
