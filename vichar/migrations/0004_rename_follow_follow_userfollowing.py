# Generated by Django 4.1.5 on 2023-08-26 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vichar', '0003_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='follow',
            new_name='userfollowing',
        ),
    ]