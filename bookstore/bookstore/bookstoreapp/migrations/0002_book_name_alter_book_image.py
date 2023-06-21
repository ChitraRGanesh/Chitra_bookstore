# Generated by Django 4.1.7 on 2023-06-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(default='Untitled', max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
    ]