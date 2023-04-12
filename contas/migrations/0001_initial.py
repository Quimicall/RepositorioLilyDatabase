# Generated by Django 4.2 on 2023-04-12 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batalha',
            fields=[
                ('ID_BAT', models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False)),
                ('NOME_BAT', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('nome', models.CharField(max_length=50)),
                ('imagem', models.CharField(max_length=500)),
                ('descricao', models.CharField(max_length=400)),
                ('observacoes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CopiaCarta',
            fields=[
                ('ID_CCARD', models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('idcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.carta')),
                ('imagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagem2', to='contas.carta')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nome2', to='contas.carta')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('ID_EVENT', models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False)),
                ('NOME_EVENT', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='Minigame',
            fields=[
                ('ID_MINIG', models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False)),
                ('NOME_MINIG', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('ID_USER', models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False)),
                ('NOME_USER', models.CharField(max_length=34)),
            ],
        ),
        migrations.CreateModel(
            name='Minigame_User',
            fields=[
                ('ID_MINIG_USER', models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False)),
                ('ID_MINIGAME', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ID_MINIG2', to='contas.minigame')),
                ('ID_USER_minig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.user')),
                ('NOME_MINIG_LOG', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.minigame')),
            ],
        ),
        migrations.CreateModel(
            name='Invent',
            fields=[
                ('ID_INV', models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False)),
                ('ID_USER_inv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.user')),
                ('id_card_copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.copiacarta')),
            ],
        ),
        migrations.CreateModel(
            name='Event_User',
            fields=[
                ('ID_EVENT_USER', models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False)),
                ('ID_EVENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ID_EVENT2', to='contas.evento')),
                ('ID_USER_evt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.user')),
                ('NOME_EVENT_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NOME_EVENT2', to='contas.evento')),
            ],
        ),
        migrations.CreateModel(
            name='DateSim',
            fields=[
                ('ID_DATE_SIM', models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False)),
                ('PERGUNTA', models.CharField(max_length=99)),
                ('RESPOSTA', models.CharField(max_length=99)),
                ('ID_CARD_DATE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.carta')),
            ],
        ),
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('ID_CARTEIRA', models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False)),
                ('ID_USER_carteira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.user')),
            ],
        ),
        migrations.CreateModel(
            name='Bat_Log',
            fields=[
                ('ID_BAT_LOG', models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False)),
                ('ID_BAT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ID_BAT2', to='contas.batalha')),
                ('ID_USER_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.user')),
                ('NOME_BAT_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NOME_BAT2', to='contas.batalha')),
            ],
        ),
    ]
