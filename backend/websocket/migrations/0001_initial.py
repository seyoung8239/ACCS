# Generated by Django 4.0.1 on 2022-02-02 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('la', models.FloatField(default=0)),
                ('lo', models.FloatField(default=0)),
            ],
        ),
    ]
