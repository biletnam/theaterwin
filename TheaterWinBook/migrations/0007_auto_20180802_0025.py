# Generated by Django 2.0.7 on 2018-08-01 15:25

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('TheaterWinBook', '0006_auto_20180730_2125'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestModel',
        ),
        migrations.RemoveField(
            model_name='theaterwinbook_record',
            name='author',
        ),
        migrations.RenameField(
            model_name='theaterwinbookrecord',
            old_name='user',
            new_name='user_name',
        ),
        migrations.AlterField(
            model_name='theaterwinbookrecord',
            name='batting_money',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='theaterwinbookrecord',
            name='batting_ratio',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='theaterwinbookrecord',
            name='buy_date',
            field=models.DateField(blank=True, default=django.utils.datetime_safe.datetime.now),
        ),
        migrations.AlterField(
            model_name='theaterwinbookrecord',
            name='buy_game_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='theaterwinbookrecord',
            name='etc_memo',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='theaterwinbookrecord',
            name='folder_num',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='theaterwinbookrecord',
            name='win_check',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.DeleteModel(
            name='TheaterWinBook_Record',
        ),
    ]
