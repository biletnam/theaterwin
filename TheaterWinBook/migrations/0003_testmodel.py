# Generated by Django 2.0.7 on 2018-07-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheaterWinBook', '0002_theaterbook_theaterwinbook_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.TextField()),
            ],
        ),
    ]
