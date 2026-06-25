from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(db_index=True, max_length=60)),
                ('min_qty', models.PositiveSmallIntegerField()),
                ('discount_pct', models.PositiveSmallIntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['product_id', 'min_qty'],
                'unique_together': {('product_id', 'min_qty')},
            },
        ),
    ]
