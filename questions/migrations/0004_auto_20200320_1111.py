# Generated by Django 2.2.10 on 2020-03-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_answer_data_appended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_searchable_string',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]