# Generated by Django 4.1.7 on 2023-03-30 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_alter_categoria_dt_criacao_carta'),
    ]

    operations = [
        migrations.AddField(
            model_name='carta',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carta',
            name='data',
            field=models.DateTimeField(),
        ),
    ]