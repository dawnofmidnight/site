# Generated by Django 3.0.11 on 2021-03-26 18:21

import django.core.validators
from django.db import migrations, models
import pydis_site.apps.api.models.bot.documentation_link


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0068_split_nomination_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentationlink',
            name='base_url',
            field=models.URLField(help_text='The base URL from which documentation will be available for this project. Used to generate links to various symbols within this package.', validators=[pydis_site.apps.api.models.bot.documentation_link.ends_with_slash_validator]),
        ),
        migrations.AlterField(
            model_name='documentationlink',
            name='package',
            field=models.CharField(help_text='The Python package name that this documentation link belongs to.', max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Package names can only consist of lowercase a-z letters, digits, and underscores.', regex='^[a-z0-9_]+$')]),
        ),
    ]
