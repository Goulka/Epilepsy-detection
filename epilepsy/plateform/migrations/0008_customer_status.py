# Generated by Django 3.2 on 2021-05-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plateform', '0007_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.CharField(choices=[('patient', 'patient'), ('expert', 'expert')], max_length=100, null=True),
        ),
    ]