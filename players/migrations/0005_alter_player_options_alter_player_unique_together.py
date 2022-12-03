# Generated by Django 4.1.2 on 2022-11-27 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_remove_player_comments_remove_player_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['-last_name']},
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together={('name', 'last_name')},
        ),
    ]