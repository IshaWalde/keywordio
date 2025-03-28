# Generated by Django 5.1.7 on 2025-03-24 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_author_name_alter_book_book_add_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_add_date',
            field=models.DateField(default=datetime.date(2025, 3, 24)),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_add_time',
            field=models.TimeField(default=datetime.datetime(2025, 3, 24, 14, 5, 32, 832162, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='issueditem',
            name='issue_date',
            field=models.DateField(default=datetime.date(2025, 3, 24)),
        ),
    ]
