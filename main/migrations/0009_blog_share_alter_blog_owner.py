# Generated by Django 4.1.1 on 2022-10-04 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_blog_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='share',
            field=models.IntegerField(default=0, verbose_name='Share'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='owner',
            field=models.CharField(max_length=100, verbose_name='Owner'),
        ),
    ]
