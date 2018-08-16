# Generated by Django 2.1 on 2018-08-16 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180815_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='imprint',
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='media',
            field=models.CharField(default='paperback', help_text='Type of media such as hardback, paperback, audiobook', max_length=200),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Born'),
        ),
    ]
