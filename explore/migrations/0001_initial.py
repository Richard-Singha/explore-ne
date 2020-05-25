# Generated by Django 3.0.1 on 2020-05-07 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Stay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('number_of_rooms', models.IntegerField()),
                ('price', models.IntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explore.Destination')),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explore.Image')),
            ],
        ),
        migrations.CreateModel(
            name='PopularFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explore.Destination')),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explore.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Hotspot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explore.Destination')),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explore.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explore.Destination')),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explore.Image')),
            ],
        ),
    ]
