# Generated by Django 5.0.6 on 2024-05-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('desc', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='shop/images')),
            ],
        ),
    ]
