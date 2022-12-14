# Generated by Django 4.1.3 on 2022-11-17 00:37

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_articlepage_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Add additional text', required=True))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
