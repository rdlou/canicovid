# Generated by Django 2.2.10 on 2020-03-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='interrogative',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_searchable_string',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
