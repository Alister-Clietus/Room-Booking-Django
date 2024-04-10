# Generated by Django 4.0 on 2024-04-10 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='booked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='User.user'),
        ),
        migrations.AddField(
            model_name='room',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
