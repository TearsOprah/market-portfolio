# Generated by Django 4.0.3 on 2022-03-04 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='caregory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory'),
        ),
    ]
