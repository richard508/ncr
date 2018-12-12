# Generated by Django 2.1.4 on 2018-12-12 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField(default=0)),
                ('card_name', models.CharField(max_length=200)),
                ('cvv', models.IntegerField(default=0, max_length=3)),
                ('expiration_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('field', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('expected_date', models.DateField()),
                ('image_url', models.TextField()),
                ('order_history_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='main.OrderHistory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image_url', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField()),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('unit', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping', to='main.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TrackPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_status', models.CharField(max_length=200)),
                ('order_history_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_packages', to='main.OrderHistory')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.ProductType'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='main.Product'),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_histories', to='main.Profile'),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='shipping_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_histories', to='main.Shipping'),
        ),
        migrations.AddField(
            model_name='billing',
            name='profie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billing', to='main.Profile'),
        ),
        migrations.AddField(
            model_name='billing',
            name='shipping_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billing', to='main.Shipping'),
        ),
    ]
