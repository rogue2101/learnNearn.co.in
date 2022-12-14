# Generated by Django 4.0.6 on 2022-08-28 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement_system', '0005_delete_company_save'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cimg', models.FileField(default=None, max_length=500, null=True, upload_to='jobs/')),
                ('cjob', models.CharField(max_length=100)),
                ('cname', models.CharField(max_length=100)),
                ('cdesc', models.CharField(max_length=500)),
                ('cjobcity', models.CharField(max_length=50)),
                ('cwebsite', models.CharField(max_length=100)),
                ('cemail', models.CharField(max_length=100)),
                ('chrname', models.CharField(max_length=50)),
                ('chrcontact', models.CharField(max_length=10)),
            ],
        ),
    ]
