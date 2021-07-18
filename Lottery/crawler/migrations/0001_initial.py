# Generated by Django 3.1.2 on 2020-11-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LotteryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('lottery_count', models.IntegerField(default=0)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'lottery_store',
            },
        ),
    ]
