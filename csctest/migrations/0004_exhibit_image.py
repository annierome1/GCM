# Generated by Django 5.0.4 on 2024-04-11 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csctest', '0003_rename_exhibits_exhibit'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='html_pages_images/'),
        ),
    ]
