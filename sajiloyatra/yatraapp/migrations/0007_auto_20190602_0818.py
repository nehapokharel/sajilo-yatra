# Generated by Django 2.2.1 on 2019-06-02 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yatraapp', '0006_auto_20190602_0816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='activetttt',
            new_name='active',
        ),
    ]
