# Generated by Django 2.2.7 on 2019-12-03 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tariff_schemas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tariff_name', models.CharField(max_length=5)),
                ('user_id', models.IntegerField()),
                ('DT_create', models.DateField(auto_now_add=True)),
                ('DT_modify', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UR_conn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('POB_id', models.IntegerField()),
                ('SE_id', models.IntegerField()),
                ('DT_from', models.DateField()),
                ('DT_to', models.DateField()),
                ('DT_create', models.DateField(auto_now_add=True)),
                ('user_id', models.IntegerField()),
                ('DT_modify', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='tariff_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tariff_date', models.DateField()),
                ('hour_1', models.FloatField()),
                ('hour_2', models.FloatField()),
                ('hour_3', models.FloatField()),
                ('hour_4', models.FloatField()),
                ('hour_5', models.FloatField()),
                ('hour_6', models.FloatField()),
                ('hour_7', models.FloatField()),
                ('hour_8', models.FloatField()),
                ('hour_9', models.FloatField()),
                ('hour_10', models.FloatField()),
                ('hour_11', models.FloatField()),
                ('hour_12', models.FloatField()),
                ('hour_13', models.FloatField()),
                ('hour_14', models.FloatField()),
                ('hour_15', models.FloatField()),
                ('hour_16', models.FloatField()),
                ('hour_17', models.FloatField()),
                ('hour_18', models.FloatField()),
                ('hour_19', models.FloatField()),
                ('hour_20', models.FloatField()),
                ('hour_21', models.FloatField()),
                ('hour_22', models.FloatField()),
                ('hour_23', models.FloatField()),
                ('hour_24', models.FloatField()),
                ('tariff_schemas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bil_site_project.tariff_schemas')),
            ],
        ),
    ]
