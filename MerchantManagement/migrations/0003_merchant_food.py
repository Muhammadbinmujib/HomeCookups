# Generated by Django 2.2 on 2020-09-20 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FoodManagement', '0001_initial'),
        ('MerchantManagement', '0002_auto_20200920_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='food',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='FoodManagement.Food'),
        ),
    ]