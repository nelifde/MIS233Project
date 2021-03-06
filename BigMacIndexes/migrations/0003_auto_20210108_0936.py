# Generated by Django 3.1.4 on 2021-01-08 09:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('BigMacIndexes', '0002_auto_20210108_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigmacindexes',
            name='CNY_adjusted',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bigmacindexes',
            name='EUR_adjusted',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bigmacindexes',
            name='GBP_adjusted',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bigmacindexes',
            name='JPY_adjusted',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bigmacindexes',
            name='USD_adjusted',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
