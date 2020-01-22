# Generated by Django 3.0.2 on 2020-01-22 04:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FootballPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=64)),
                ('height', models.DecimalField(decimal_places=2, max_digits=4)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fourty_yard_dash', models.DecimalField(decimal_places=2, max_digits=3)),
                ('wonderlick_score', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasketballPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=64)),
                ('height', models.DecimalField(decimal_places=2, max_digits=4)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('position', models.CharField(choices=[('1', 'PG'), ('2', 'SG'), ('3', 'SF'), ('4', 'PF'), ('5', 'C'), ('6', 'water boy')], default='water boy', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
