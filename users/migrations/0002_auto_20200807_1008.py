# Generated by Django 2.2.9 on 2020-08-07 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='manprof.png', upload_to='profile_pics'),
        ),
    ]