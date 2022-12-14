# Generated by Django 4.0.6 on 2022-09-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('meeting_id', models.IntegerField(default='')),
                ('meeting_time', models.TimeField(default='12:00:00')),
                ('meeting_date', models.DateField(default='')),
                ('created_by', models.CharField(max_length=50)),
                ('meeting_link', models.URLField(max_length=2000)),
            ],
        ),
        migrations.DeleteModel(
            name='Link',
        ),
    ]
