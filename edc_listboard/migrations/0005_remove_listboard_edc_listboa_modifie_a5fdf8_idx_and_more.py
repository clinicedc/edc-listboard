# Generated by Django 4.2.7 on 2023-12-04 02:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "edc_listboard",
            "0004_alter_listboard_options_listboard_locale_created_and_more",
        ),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="listboard",
            name="edc_listboa_modifie_a5fdf8_idx",
        ),
        migrations.AddIndex(
            model_name="listboard",
            index=models.Index(
                fields=["modified", "created"], name="edc_listboa_modifie_e63312_idx"
            ),
        ),
    ]