# Generated by Django 3.1.1 on 2020-10-04 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='search',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
