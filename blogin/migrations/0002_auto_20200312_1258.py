# Generated by Django 3.0.1 on 2020-03-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contengt',
            new_name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default=1, max_length=105),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(blank=True),
        ),
    ]
