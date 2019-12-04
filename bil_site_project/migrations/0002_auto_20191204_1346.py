# Generated by Django 3.0 on 2019-12-04 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bil_site_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff_schemas',
            name='user_id',
            field=models.ForeignKey(on_delete=models.SET('deleted'), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ur_conn',
            name='user_id',
            field=models.ForeignKey(on_delete=models.SET('deleted'), to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UR_objects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=70)),
                ('is_pob', models.IntegerField()),
                ('DT_create', models.DateField(auto_now_add=True)),
                ('DT_modify', models.DateField(auto_now=True)),
                ('UR_conn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bil_site_project.UR_conn')),
                ('user_id', models.ForeignKey(on_delete=models.SET('deleted'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CSPR_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PPE_number', models.CharField(max_length=40)),
                ('month_date', models.DateField()),
                ('value_d1', models.FloatField(null=True)),
                ('value_d2', models.FloatField(null=True)),
                ('value_d3', models.FloatField(null=True)),
                ('value_d4', models.FloatField(null=True)),
                ('value_d5', models.FloatField(null=True)),
                ('value_d6', models.FloatField(null=True)),
                ('value_d7', models.FloatField(null=True)),
                ('value_d8', models.FloatField(null=True)),
                ('value_d9', models.FloatField(null=True)),
                ('value_d10', models.FloatField(null=True)),
                ('value_d11', models.FloatField(null=True)),
                ('value_d12', models.FloatField(null=True)),
                ('value_d13', models.FloatField(null=True)),
                ('value_d14', models.FloatField(null=True)),
                ('value_d15', models.FloatField(null=True)),
                ('value_d16', models.FloatField(null=True)),
                ('value_d17', models.FloatField(null=True)),
                ('value_d18', models.FloatField(null=True)),
                ('value_d19', models.FloatField(null=True)),
                ('value_d20', models.FloatField(null=True)),
                ('value_d21', models.FloatField(null=True)),
                ('value_d22', models.FloatField(null=True)),
                ('value_d23', models.FloatField(null=True)),
                ('value_d24', models.FloatField(null=True)),
                ('value_d25', models.FloatField(null=True)),
                ('value_d26', models.FloatField(null=True)),
                ('value_d27', models.FloatField(null=True)),
                ('value_d28', models.FloatField(null=True)),
                ('value_d29', models.FloatField(null=True)),
                ('value_d30', models.FloatField(null=True)),
                ('value_d31', models.FloatField(null=True)),
                ('status_d1', models.FloatField(null=True)),
                ('status_d2', models.FloatField(null=True)),
                ('status_d3', models.FloatField(null=True)),
                ('status_d4', models.FloatField(null=True)),
                ('status_d5', models.FloatField(null=True)),
                ('status_d6', models.FloatField(null=True)),
                ('status_d7', models.FloatField(null=True)),
                ('status_d8', models.FloatField(null=True)),
                ('status_d9', models.FloatField(null=True)),
                ('status_d10', models.FloatField(null=True)),
                ('status_d11', models.FloatField(null=True)),
                ('status_d12', models.FloatField(null=True)),
                ('status_d13', models.FloatField(null=True)),
                ('status_d14', models.FloatField(null=True)),
                ('status_d15', models.FloatField(null=True)),
                ('status_d16', models.FloatField(null=True)),
                ('status_d17', models.FloatField(null=True)),
                ('status_d18', models.FloatField(null=True)),
                ('status_d19', models.FloatField(null=True)),
                ('status_d20', models.FloatField(null=True)),
                ('status_d21', models.FloatField(null=True)),
                ('status_d22', models.FloatField(null=True)),
                ('status_d23', models.FloatField(null=True)),
                ('status_d24', models.FloatField(null=True)),
                ('status_d25', models.FloatField(null=True)),
                ('status_d26', models.FloatField(null=True)),
                ('status_d27', models.FloatField(null=True)),
                ('status_d28', models.FloatField(null=True)),
                ('status_d29', models.FloatField(null=True)),
                ('status_d30', models.FloatField(null=True)),
                ('status_d31', models.FloatField(null=True)),
                ('tariff_d1', models.FloatField(null=True)),
                ('tariff_d2', models.FloatField(null=True)),
                ('tariff_d3', models.FloatField(null=True)),
                ('tariff_d4', models.FloatField(null=True)),
                ('tariff_d5', models.FloatField(null=True)),
                ('tariff_d6', models.FloatField(null=True)),
                ('tariff_d7', models.FloatField(null=True)),
                ('tariff_d8', models.FloatField(null=True)),
                ('tariff_d9', models.FloatField(null=True)),
                ('tariff_d10', models.FloatField(null=True)),
                ('tariff_d11', models.FloatField(null=True)),
                ('tariff_d12', models.FloatField(null=True)),
                ('tariff_d13', models.FloatField(null=True)),
                ('tariff_d14', models.FloatField(null=True)),
                ('tariff_d15', models.FloatField(null=True)),
                ('tariff_d16', models.FloatField(null=True)),
                ('tariff_d17', models.FloatField(null=True)),
                ('tariff_d18', models.FloatField(null=True)),
                ('tariff_d19', models.FloatField(null=True)),
                ('tariff_d20', models.FloatField(null=True)),
                ('tariff_d21', models.FloatField(null=True)),
                ('tariff_d22', models.FloatField(null=True)),
                ('tariff_d23', models.FloatField(null=True)),
                ('tariff_d24', models.FloatField(null=True)),
                ('tariff_d25', models.FloatField(null=True)),
                ('tariff_d26', models.FloatField(null=True)),
                ('tariff_d27', models.FloatField(null=True)),
                ('tariff_d28', models.FloatField(null=True)),
                ('tariff_d29', models.FloatField(null=True)),
                ('tariff_d30', models.FloatField(null=True)),
                ('tariff_d31', models.FloatField(null=True)),
                ('direction', models.IntegerField()),
                ('DT_modify', models.DateField(auto_now=True)),
                ('conn_UR', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bil_site_project.UR_conn')),
                ('user_id', models.ForeignKey(on_delete=models.SET('deleted'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CSB_raw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PPE_number', models.CharField(max_length=40)),
                ('sell_DT', models.DateField()),
                ('invoice_DT_from', models.DateField()),
                ('invoice_DT_to', models.DateField()),
                ('volume', models.FloatField()),
                ('zone_1', models.FloatField()),
                ('zone_2', models.FloatField()),
                ('zone_3', models.FloatField()),
                ('DT_modify', models.DateField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=models.SET('deleted'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CSB_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PPE_number', models.CharField(max_length=40)),
                ('month_date', models.DateField()),
                ('value_d1', models.FloatField(null=True)),
                ('value_d2', models.FloatField(null=True)),
                ('value_d3', models.FloatField(null=True)),
                ('value_d4', models.FloatField(null=True)),
                ('value_d5', models.FloatField(null=True)),
                ('value_d6', models.FloatField(null=True)),
                ('value_d7', models.FloatField(null=True)),
                ('value_d8', models.FloatField(null=True)),
                ('value_d9', models.FloatField(null=True)),
                ('value_d10', models.FloatField(null=True)),
                ('value_d11', models.FloatField(null=True)),
                ('value_d12', models.FloatField(null=True)),
                ('value_d13', models.FloatField(null=True)),
                ('value_d14', models.FloatField(null=True)),
                ('value_d15', models.FloatField(null=True)),
                ('value_d16', models.FloatField(null=True)),
                ('value_d17', models.FloatField(null=True)),
                ('value_d18', models.FloatField(null=True)),
                ('value_d19', models.FloatField(null=True)),
                ('value_d20', models.FloatField(null=True)),
                ('value_d21', models.FloatField(null=True)),
                ('value_d22', models.FloatField(null=True)),
                ('value_d23', models.FloatField(null=True)),
                ('value_d24', models.FloatField(null=True)),
                ('value_d25', models.FloatField(null=True)),
                ('value_d26', models.FloatField(null=True)),
                ('value_d27', models.FloatField(null=True)),
                ('value_d28', models.FloatField(null=True)),
                ('value_d29', models.FloatField(null=True)),
                ('value_d30', models.FloatField(null=True)),
                ('value_d31', models.FloatField(null=True)),
                ('tariff_d1', models.FloatField(null=True)),
                ('tariff_d2', models.FloatField(null=True)),
                ('tariff_d3', models.FloatField(null=True)),
                ('tariff_d4', models.FloatField(null=True)),
                ('tariff_d5', models.FloatField(null=True)),
                ('tariff_d6', models.FloatField(null=True)),
                ('tariff_d7', models.FloatField(null=True)),
                ('tariff_d8', models.FloatField(null=True)),
                ('tariff_d9', models.FloatField(null=True)),
                ('tariff_d10', models.FloatField(null=True)),
                ('tariff_d11', models.FloatField(null=True)),
                ('tariff_d12', models.FloatField(null=True)),
                ('tariff_d13', models.FloatField(null=True)),
                ('tariff_d14', models.FloatField(null=True)),
                ('tariff_d15', models.FloatField(null=True)),
                ('tariff_d16', models.FloatField(null=True)),
                ('tariff_d17', models.FloatField(null=True)),
                ('tariff_d18', models.FloatField(null=True)),
                ('tariff_d19', models.FloatField(null=True)),
                ('tariff_d20', models.FloatField(null=True)),
                ('tariff_d21', models.FloatField(null=True)),
                ('tariff_d22', models.FloatField(null=True)),
                ('tariff_d23', models.FloatField(null=True)),
                ('tariff_d24', models.FloatField(null=True)),
                ('tariff_d25', models.FloatField(null=True)),
                ('tariff_d26', models.FloatField(null=True)),
                ('tariff_d27', models.FloatField(null=True)),
                ('tariff_d28', models.FloatField(null=True)),
                ('tariff_d29', models.FloatField(null=True)),
                ('tariff_d30', models.FloatField(null=True)),
                ('tariff_d31', models.FloatField(null=True)),
                ('DT_modify', models.DateField(auto_now=True)),
                ('SE_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bil_site_project.UR_objects')),
                ('user_id', models.ForeignKey(on_delete=models.SET('deleted'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
