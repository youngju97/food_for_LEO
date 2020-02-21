# Generated by Django 2.2.9 on 2020-02-21 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0002_remove_pet_img'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='like',
        ),
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='like', to='mypage.Profile'),
        ),
    ]
