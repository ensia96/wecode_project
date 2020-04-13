# Generated by Django 3.0.5 on 2020-04-13 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'allergy',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'description',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.Category')),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ko', models.CharField(max_length=50)),
                ('name_en', models.CharField(max_length=50)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.Category')),
                ('group_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.Group')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('num_ml', models.IntegerField()),
                ('num_oz', models.IntegerField()),
            ],
            options={
                'db_table': 'size',
            },
        ),
        migrations.CreateModel(
            name='Product_Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.Description')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.Product')),
            ],
            options={
                'db_table': 'product_description',
            },
        ),
        migrations.CreateModel(
            name='Product_Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.Allergy')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.Product')),
            ],
            options={
                'db_table': 'product_allergy',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_id', models.CharField(max_length=20)),
                ('kcal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sugar', models.DecimalField(decimal_places=2, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sodium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('caffeine', models.DecimalField(decimal_places=2, max_digits=5)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.Product')),
            ],
            options={
                'db_table': 'ingredient',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.URLField(max_length=2000)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.Product')),
            ],
            options={
                'db_table': 'image',
            },
        ),
        migrations.AddField(
            model_name='description',
            name='product_id',
            field=models.ManyToManyField(through='data.Product_Description', to='data.Product'),
        ),
        migrations.AddField(
            model_name='allergy',
            name='product_id',
            field=models.ManyToManyField(through='data.Product_Allergy', to='data.Product'),
        ),
    ]
