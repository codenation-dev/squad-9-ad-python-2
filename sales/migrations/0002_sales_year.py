# Generated by Django 2.2.3 on 2019-07-30 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='year',
            field=models.IntegerField(default=0, verbose_name='Ano'),
        ),
    ]
