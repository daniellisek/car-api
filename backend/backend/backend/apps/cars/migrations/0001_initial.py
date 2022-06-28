# Generated by Django 4.0.5 on 2022-06-28 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make_name', models.CharField(choices=[('A', 'Audi'), ('B', 'BMW'), ('T', 'Toyota'), ('S', 'Skoda')], default='A', max_length=1)),
                ('is_premium', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('price', models.FloatField()),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.carmake')),
            ],
        ),
    ]