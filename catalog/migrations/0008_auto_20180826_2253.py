# Generated by Django 2.1 on 2018-08-27 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20180824_2307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
