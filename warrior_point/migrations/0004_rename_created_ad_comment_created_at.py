# Generated by Django 5.0.8 on 2024-09-17 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warrior_point', '0003_alter_category_options_alter_game_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_ad',
            new_name='created_at',
        ),
    ]