# Generated by Django 3.0.3 on 2023-03-08 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('profile', models.ImageField(upload_to='pics')),
                ('img1', models.ImageField(null=True, upload_to='pics')),
                ('img2', models.ImageField(null=True, upload_to='pics')),
                ('img3', models.ImageField(null=True, upload_to='pics')),
                ('img4', models.ImageField(null=True, upload_to='pics')),
                ('short_description', models.CharField(max_length=50)),
                ('long_description', models.TextField()),
                ('basePrice', models.IntegerField()),
                ('currentPrice', models.IntegerField()),
                ('tag', models.CharField(max_length=25)),
                ('status', models.CharField(max_length=25, null=True)),
                ('sold', models.CharField(default='unsold', max_length=10)),
                ('ownermail', models.EmailField(max_length=254)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('highest_bidder', models.IntegerField(null=True)),
                ('sendwinmail', models.CharField(default='unsended', max_length=7)),
            ],
        ),
    ]
