# Generated by Django 4.2.5 on 2023-09-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='intro',
            field=models.TextField(max_length=300),
        ),
    ]