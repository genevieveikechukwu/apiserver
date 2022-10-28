# Generated by Django 4.1.2 on 2022-10-28 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serverapi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_username', models.CharField(max_length=120)),
                ('backend', models.BooleanField(default=True)),
                ('age', models.IntegerField()),
                ('bio', models.TextField()),
            ],
        ),
    ]
