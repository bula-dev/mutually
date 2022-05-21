# Generated by Django 4.0.4 on 2022-05-21 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_x_coord_alter_user_y_coord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='x_coord',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='y_coord',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]
