# Generated by Django 3.2 on 2021-04-19 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('durations', models.PositiveIntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start', models.DateTimeField()),
                ('end', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.course')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('course', models.ManyToManyField(to='customers.Course')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.group')),
            ],
        ),
    ]
