# Generated by Django 4.0.6 on 2022-08-28 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement_system', '0007_student_save_hper_student_save_hschool_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_save',
            name='skills',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='student_save',
            name='intper',
            field=models.CharField(max_length=50, null=True),
        ),
    ]