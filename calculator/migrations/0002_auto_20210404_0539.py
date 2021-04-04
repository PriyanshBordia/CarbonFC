# Generated by Django 3.1.7 on 2021-04-04 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='ph_no',
            field=models.BigIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('X', 'Not Preferred to say')], default='X', max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]