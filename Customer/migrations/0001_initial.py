# Generated by Django 3.0.6 on 2020-11-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Email', models.EmailField(max_length=254)),
                ('Seller_Email', models.EmailField(max_length=254)),
                ('Pro_Id', models.IntegerField(default=0)),
                ('Name', models.CharField(max_length=20)),
                ('Price', models.IntegerField()),
                ('Quantity', models.IntegerField()),
                ('Weight', models.IntegerField()),
                ('Weight1', models.CharField(default=0, max_length=10)),
                ('Sub_Total', models.IntegerField()),
                ('CImage', models.ImageField(upload_to='cart')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Mobile', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Email', models.EmailField(max_length=254)),
                ('Seller_Email', models.EmailField(max_length=254)),
                ('Pro_Id', models.IntegerField(default=0)),
                ('Order_Id', models.CharField(default='ABC', max_length=50, unique=True)),
                ('Name', models.CharField(max_length=20)),
                ('Price', models.IntegerField()),
                ('Quantity', models.IntegerField()),
                ('Weight', models.IntegerField()),
                ('Weight1', models.CharField(default=0, max_length=10)),
                ('Sub_Total', models.IntegerField()),
                ('Payment_Mode', models.CharField(default=0, max_length=100)),
                ('Order_Status', models.CharField(max_length=100)),
                ('Order_Date', models.DateTimeField(auto_now=True)),
                ('Status_Date', models.DateTimeField(auto_now=True)),
                ('OImage', models.ImageField(upload_to='orders')),
            ],
        ),
    ]