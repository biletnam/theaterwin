# Generated by Django 2.0.7 on 2018-08-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheaterWinBook', '0007_auto_20180802_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theaterwinbookrecord',
            name='win_check',
            field=models.IntegerField(choices=[('0', 'lose'), ('1', 'win'), ('2', 'soon')], default=1),
        ),
    ]
