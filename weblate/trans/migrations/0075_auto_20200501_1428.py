# Generated by Django 3.0.5 on 2020-05-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0074_fix_broken_browser_alert"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="alert",
            options={
                "verbose_name": "component alert",
                "verbose_name_plural": "component alerts",
            },
        ),
        migrations.AlterModelOptions(
            name="change",
            options={
                "verbose_name": "history event",
                "verbose_name_plural": "history events",
            },
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={
                "verbose_name": "string comment",
                "verbose_name_plural": "string comments",
            },
        ),
        migrations.AlterModelOptions(
            name="contributoragreement",
            options={
                "verbose_name": "contributor agreement",
                "verbose_name_plural": "contributor agreements",
            },
        ),
        migrations.AlterModelOptions(
            name="dictionary",
            options={
                "verbose_name": "glossary entry",
                "verbose_name_plural": "glossary entries",
            },
        ),
        migrations.AlterModelOptions(
            name="label",
            options={"verbose_name": "label", "verbose_name_plural": "label"},
        ),
        migrations.AlterModelOptions(
            name="shaping",
            options={
                "verbose_name": "shaping definition",
                "verbose_name_plural": "shaping definitions",
            },
        ),
        migrations.AlterModelOptions(
            name="suggestion",
            options={
                "verbose_name": "string suggestion",
                "verbose_name_plural": "string suggestions",
            },
        ),
        migrations.AlterModelOptions(
            name="translation",
            options={
                "verbose_name": "translation",
                "verbose_name_plural": "translations",
            },
        ),
        migrations.AlterModelOptions(
            name="unit",
            options={"verbose_name": "string", "verbose_name_plural": "strings"},
        ),
        migrations.AlterModelOptions(
            name="vote",
            options={
                "verbose_name": "suggestion vote",
                "verbose_name_plural": "suggestion votes",
            },
        ),
        migrations.AlterField(
            model_name="component",
            name="language_code_style",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Default based on the file format"),
                    ("posix", "POSIX style using underscore as a separator"),
                    ("bcp", "BCP style using hyphen as a separator"),
                    (
                        "posix_long",
                        "POSIX style using underscore as a separator, including country code",
                    ),
                    (
                        "bcp_long",
                        "BCP style using hyphen as a separator, including country code",
                    ),
                    ("android", "Android style"),
                    ("java", "Java style"),
                ],
                default="",
                help_text="Customize language code used to generate the filename for translations created by Weblate.",
                max_length=10,
                verbose_name="Language code style",
            ),
        ),
    ]