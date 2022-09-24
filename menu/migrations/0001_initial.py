# Generated by Django 4.1.1 on 2022-06-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishName', models.CharField(max_length=20)),
                ('dishDesc', models.TextField()),
                ('dishPrice', models.IntegerField()),
                ('dishPrepTime', models.IntegerField()),
                ('dishImage', models.ImageField(upload_to='menu_imgs/')),
            ],
        ),
    ]
