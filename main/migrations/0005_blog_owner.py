# Generated by Django 4.1.1 on 2022-10-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='owner',
            field=models.ImageField(default=1, upload_to='', verbose_name='Owner'),
        ),
    ]
