# Generated by Django 4.1.5 on 2023-01-10 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="description",
            new_name="description_1",
        ),
        migrations.AddField(
            model_name="product",
            name="description_2",
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="product",
            name="description_3",
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="product",
            name="description_4",
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="product",
            name="description_5",
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="product",
            name="description_6",
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
