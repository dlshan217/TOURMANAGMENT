# Generated by Django 5.1.6 on 2025-03-02 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twd', '0006_alter_bookingdetails_user_alter_packagecreate_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagecreate',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='twd.vendorregister'),
        ),
    ]
