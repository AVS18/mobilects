# Generated by Django 3.1.2 on 2021-01-01 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('semester', models.IntegerField()),
            ],
        ),
    ]
