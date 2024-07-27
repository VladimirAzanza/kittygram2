# Generated by Django 3.2.3 on 2024-07-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_alter_cat_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cat',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='cat',
            constraint=models.UniqueConstraint(fields=('name', 'owner'), name='unique_name_owner'),
        ),
    ]
