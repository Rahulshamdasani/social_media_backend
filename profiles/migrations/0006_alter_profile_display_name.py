# Generated by Django 3.2.7 on 2021-12-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='display_name',
            field=models.CharField(blank=True, default='user-AKW19YcBYGdVlhuEmAU5', max_length=220),
        ),
    ]
