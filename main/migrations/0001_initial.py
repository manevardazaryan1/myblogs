# Generated by Django 4.1.1 on 2022-10-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('owner', models.CharField(max_length=50, verbose_name='Owner')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
            ],
        ),
    ]
