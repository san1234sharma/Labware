# Generated by Django 4.2.6 on 2023-11-02 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labware_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(default='', max_length=100)),
                ('category', models.CharField(default=' ', max_length=100)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='images/images')),
            ],
        ),
    ]
