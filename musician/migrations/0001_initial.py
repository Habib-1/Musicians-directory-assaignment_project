# Generated by Django 5.1.2 on 2024-11-17 07:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musicians',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=11)),
                ('instrument', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50)),
                ('realise_date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(help_text='Enter A rating between 1 to 5', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musicians')),
            ],
        ),
    ]
