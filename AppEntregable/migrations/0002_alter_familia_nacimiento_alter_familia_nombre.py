# Generated by Django 4.0.6 on 2022-07-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntregable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='nacimiento',
            field=models.DateField(max_length=30),
        ),
        migrations.AlterField(
            model_name='familia',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]
