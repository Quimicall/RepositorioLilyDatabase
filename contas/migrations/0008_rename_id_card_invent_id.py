# Generated by Django 4.2 on 2023-04-10 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0007_rename_eventos_evento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invent',
            old_name='ID_CARD',
            new_name='id',
        ),
    ]