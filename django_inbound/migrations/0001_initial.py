# Generated by Django 3.0 on 2020-07-11 16:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='InboundRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.CharField(blank=True, max_length=100, null=True)),
                ('namespace', models.CharField(blank=True, max_length=100, null=True)),
                ('url_name', models.CharField(blank=True, max_length=100, null=True)),
                ('allow_all', models.BooleanField(default=False, help_text='Allow all User', verbose_name="Allow all IP's")),
                ('is_active', models.BooleanField(default=True)),
                ('extra', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'verbose_name': 'Inbound Rule',
                'verbose_name_plural': 'Inbound Rules',
            },
        ),
        migrations.CreateModel(
            name='InboundIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_ip', models.GenericIPAddressField()),
                ('end_ip', models.GenericIPAddressField(blank=True, help_text='For Single or specific IP, Leave it Blank', null=True)),
                ('cidr', models.CharField(blank=True, help_text='CIDR Block', max_length=20, null=True, verbose_name='CIDR')),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('inbound_rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_inbound.InboundRule')),
            ],
            options={
                'verbose_name': 'Inbound IP',
                'verbose_name_plural': 'Inbound IPs',
            },
        ),
    ]
