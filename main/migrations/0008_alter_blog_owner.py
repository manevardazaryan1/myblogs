# Generated by Django 4.1.1 on 2022-10-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_blog_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='Owner'),
        ),
    ]
