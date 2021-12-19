# Generated by Django 3.2.7 on 2021-12-09 05:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_alter_pages_pageauthor'),
        ('profiles', '0006_alter_profile_display_name'),
        ('events', '0003_auto_20211204_0712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('eventName', models.CharField(db_column='eventName', max_length=40)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('pageName', models.ForeignKey(db_column='pageName', on_delete=django.db.models.deletion.CASCADE, to='pages.pages')),
                ('userID', models.ForeignKey(db_column='userID', on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]