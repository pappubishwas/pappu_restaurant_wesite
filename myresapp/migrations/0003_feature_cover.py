# Generated by Django 4.1.3 on 2023-02-27 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresapp', '0002_feature_itemno_feature_price_feature_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='cover',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
