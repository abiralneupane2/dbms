# Generated by Django 3.1.4 on 2020-12-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20201221_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='job_at',
            field=models.CharField(choices=[('Google', 'Google'), ('Apple', 'Apple')], max_length=50),
        ),
    ]
