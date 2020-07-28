# Generated by Django 2.0.7 on 2020-07-26 02:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete='CASCODE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
