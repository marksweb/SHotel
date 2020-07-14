# Generated by Django 3.0.8 on 2020-07-14 18:12

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('birth_date', models.DateField()),
                ('function', models.CharField(choices=[('HO', 'Hotel Owner'), ('SV', 'Supervisor'), ('RT', 'Receptionist'), ('RS', 'Room Service'), ('CG', 'Concierge'), ('BB', 'Bell Boy'), ('HK', 'House Keeping'), ('CH', 'Chef'), ('WT', 'Waiter'), ('BT', 'Bartender'), ('EG', 'Engineer'), ('OT', 'Other')], max_length=2)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('passport_number', models.CharField(max_length=30)),
            ],
        ),
    ]