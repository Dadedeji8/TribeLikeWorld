# Generated by Django 4.2 on 2023-06-16 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_remove_new_tags_delete_tags_new_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'tag', 'verbose_name_plural': 'tags'},
        ),
    ]