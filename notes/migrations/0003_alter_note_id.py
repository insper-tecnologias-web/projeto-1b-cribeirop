# Generated by Django 4.1.1 on 2022-10-09 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_note_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]