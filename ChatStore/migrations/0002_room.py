# Generated by Django 3.2.4 on 2021-06-27 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ChatStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('author1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users1_room', to=settings.AUTH_USER_MODEL)),
                ('author2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users2_room', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]