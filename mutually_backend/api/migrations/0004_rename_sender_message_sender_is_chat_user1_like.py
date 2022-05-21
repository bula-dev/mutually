# Generated by Django 4.0.4 on 2022-05-21 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_x_coord_alter_user_y_coord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sender',
            new_name='sender_is_chat_user1',
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likee', to='api.user')),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker', to='api.user')),
            ],
        ),
    ]