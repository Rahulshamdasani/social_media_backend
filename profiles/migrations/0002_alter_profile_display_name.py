# Generated by Django 3.2.7 on 2021-11-25 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='display_name',
            field=models.CharField(blank=True, default='user-ikgU2Jp5YVwfb3rKdstm', max_length=220),
        ),
    ]