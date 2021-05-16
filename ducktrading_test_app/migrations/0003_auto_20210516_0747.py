# Generated by Django 2.2 on 2021-05-16 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ducktrading_test_app', '0002_remove_security_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='security',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ducktrading_test_app.Security'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ducktrading_test_app.User'),
        ),
    ]
