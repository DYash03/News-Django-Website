# Generated by Django 3.0.6 on 2020-07-17 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_auto_20200715_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='title_desc',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
