# Generated by Django 4.2 on 2023-04-14 16:56

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
                ('data', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(max_length=50)),
                ('imagem', models.CharField(max_length=500)),
                ('Anime', models.CharField(max_length=400)),
                ('tipo', models.CharField(max_length=50)),
                ('HP', models.DecimalField(decimal_places=2, max_digits=999)),
                ('ATK', models.DecimalField(decimal_places=2, max_digits=999)),
                ('DEF', models.DecimalField(decimal_places=2, max_digits=999)),
                ('SPEED', models.DecimalField(decimal_places=2, max_digits=999)),
                ('PM', models.DecimalField(decimal_places=2, max_digits=999)),
                ('TOTAL', models.DecimalField(decimal_places=2, max_digits=999)),
                ('talento', models.CharField(max_length=500)),
                ('observacoes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('nomec', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=30)),
                ('level', models.DecimalField(decimal_places=0, max_digits=2)),
                ('afinidade', models.DecimalField(decimal_places=1, max_digits=3)),
                ('exp', models.DecimalField(decimal_places=0, max_digits=3)),
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
            name='Item',
            fields=[
                ('ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='IDItem')),
                ('Data', models.DateTimeField()),
                ('Item_Nome', models.CharField(max_length=999)),
                ('HP_Item', models.DecimalField(decimal_places=0, max_digits=999)),
                ('MP_Item', models.DecimalField(decimal_places=0, max_digits=999)),
                ('ATK_Item', models.DecimalField(decimal_places=0, max_digits=999)),
                ('ATK_M_Item', models.DecimalField(decimal_places=0, max_digits=999)),
                ('DEF_Item', models.DecimalField(decimal_places=0, max_digits=999)),
                ('DEF_M_Item', models.DecimalField(decimal_places=0, max_digits=999)),
                ('SPEED_Item', models.DecimalField(decimal_places=0, max_digits=999)),
                ('QUEIMADURA_Item', models.DecimalField(decimal_places=2, max_digits=999)),
                ('ENVENENAR_Item', models.DecimalField(decimal_places=2, max_digits=999)),
                ('SANGRAMENTO_Item', models.DecimalField(decimal_places=2, max_digits=999)),
                ('PEN_ARM_Item', models.DecimalField(decimal_places=2, max_digits=999)),
                ('ROUBO_VIDA_Item', models.DecimalField(decimal_places=2, max_digits=999)),
                ('ACERTO_CRIT_Item', models.DecimalField(decimal_places=2, max_digits=999)),
                ('ESCUDO_Item', models.DecimalField(decimal_places=2, max_digits=999)),
                ('DMG_VERDADEIRO_Item', models.DecimalField(decimal_places=2, max_digits=999)),
                ('Descricao_Item', models.TextField(blank=True)),
                ('observacoes_Item', models.TextField(blank=True, null=True)),
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
            name='CopiaCarta',
            fields=[
                ('ID_CCARD', models.DecimalField(decimal_places=0, max_digits=999, primary_key=True, serialize=False)),
                ('idcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.carta')),
                ('valor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valor2', to='contas.categoria')),
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
