# Generated by Django 4.1.7 on 2023-03-30 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_rename_nome_categoria_nomec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carta',
            name='exp',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
    ]