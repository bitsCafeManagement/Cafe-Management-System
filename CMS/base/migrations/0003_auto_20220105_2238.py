# Generated by Django 3.2.9 on 2022-01-05 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_moreinfo_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='full_Name',
            field=models.CharField(default=set, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='home_Address',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
