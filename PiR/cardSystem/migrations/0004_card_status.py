# Generated by Django 4.1.5 on 2023-01-12 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardSystem', '0003_alter_card_date_of_last_use'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Card availability', max_length=1),
        ),
    ]
