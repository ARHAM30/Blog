# Generated by Django 2.2.4 on 2020-02-02 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_proimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proimg',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Proimg',
        ),
    ]
