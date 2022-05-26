# Generated by Django 3.1.13 on 2022-05-12 18:56

import app.models
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
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('front_text', models.CharField(max_length=280)),
                ('back_text', models.CharField(max_length=280)),
                ('front_Img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('back_Img', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creator_username', models.CharField(max_length=50)),
                ('deckName', models.CharField(max_length=50)),
                ('dateCreated', models.DateField(blank=True, null=True)),
                ('isFavourite', models.BooleanField(default=False)),
                ('editable', models.BooleanField(default=False)),
                ('cardCount', models.IntegerField(default=0)),
                ('user_account', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CardLedger',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('study_date', models.DateField(default=None)),
                ('ELO', models.IntegerField(default=0)),
                ('leech', models.IntegerField(default=0)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.card')),
                ('deck', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='app.deck')),
                ('user_account', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='app.deck'),
        ),
    ]
