# Generated by Django 4.2.5 on 2023-09-29 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='intro',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
