# Generated by Django 4.1 on 2022-08-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinchonapp', '0011_alter_person_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='author',
            field=models.CharField(max_length=10, null=True),
        ),
    ]