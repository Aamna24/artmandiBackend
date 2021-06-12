# Generated by Django 3.1.4 on 2020-12-24 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_price', models.IntegerField()),
                ('user_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.userlisting')),
            ],
        ),
    ]