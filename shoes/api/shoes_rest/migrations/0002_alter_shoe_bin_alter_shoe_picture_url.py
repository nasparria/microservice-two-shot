# Generated by Django 4.0.3 on 2022-07-27 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='bin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shoes', to='shoes_rest.binvo'),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='picture_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
