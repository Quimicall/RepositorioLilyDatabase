# Generated by Django 4.2 on 2023-04-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0008_rename_id_card_invent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bat_log',
            name='ID_BAT_LOG',
            field=models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='batalha',
            name='ID_BAT',
            field=models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='carteira',
            name='ID_CARTEIRA',
            field=models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='event_user',
            name='ID_EVENT_USER',
            field=models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='evento',
            name='ID_EVENT',
            field=models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='invent',
            name='ID_INV',
            field=models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='minigame',
            name='ID_MINIG',
            field=models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='minigame_user',
            name='ID_MINIG_USER',
            field=models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='ID_USER',
            field=models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False),
        ),
    ]