# Generated by Django 3.0.5 on 2020-04-18 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='cbd',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='flower',
            name='kind',
            field=models.CharField(choices=[('S', 'Sativa'), ('I', 'Indica'), ('H', 'Hybrid')], default='H', max_length=1),
        ),
        migrations.AlterField(
            model_name='flower',
            name='thc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]
