# Generated by Django 4.1.4 on 2022-12-15 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('univ_id', models.CharField(default='', max_length=70)),
                ('first_name', models.CharField(default='', max_length=70)),
                ('last_name', models.CharField(default='', max_length=70)),
                ('course', models.CharField(default='', max_length=70)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
