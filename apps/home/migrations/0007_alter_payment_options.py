# Generated by Django 3.2.16 on 2022-11-08 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_transfer_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['created_at'], 'verbose_name': 'Платеж ', 'verbose_name_plural': 'Платежи '},
        ),
    ]