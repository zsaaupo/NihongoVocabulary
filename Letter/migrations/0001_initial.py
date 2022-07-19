# Generated by Django 4.0.5 on 2022-07-16 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hiragana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hiragana', models.CharField(max_length=20)),
                ('pronounce', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Katakana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('katakana', models.CharField(max_length=20)),
                ('pronunciation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Pronounce', to='Letter.hiragana')),
            ],
        ),
    ]