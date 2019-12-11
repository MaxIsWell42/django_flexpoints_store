# Generated by Django 2.2.7 on 2019-12-10 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_description', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='Date added')),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
