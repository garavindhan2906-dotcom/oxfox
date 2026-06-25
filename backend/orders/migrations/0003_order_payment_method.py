from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_productdiscount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default='cod', max_length=20),
        ),
    ]
