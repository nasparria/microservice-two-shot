# Generated by Django 4.0.3 on 2022-07-28 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0004_alter_shoe_binn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='binvo',
            old_name='name',
            new_name='closet_name',
        ),
        migrations.RenameField(
            model_name='shoe',
            old_name='binn',
            new_name='bin',
        ),
        migrations.AddField(
            model_name='binvo',
            name='bin_number',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='binvo',
            name='bin_size',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
