# Generated by Django 3.2.9 on 2021-12-09 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplestrangle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='EntryDateTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='Exit',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='ExitDateTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='PL',
            field=models.FloatField(null=True),
        ),
    ]