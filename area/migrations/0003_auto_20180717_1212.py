# Generated by Django 2.0.5 on 2018-07-17 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0002_auto_20170324_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='area',
            name='parent_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='area.Area', verbose_name='上级区域'),
        ),
    ]
