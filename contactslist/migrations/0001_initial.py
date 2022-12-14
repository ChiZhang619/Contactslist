# Generated by Django 4.1.2 on 2022-11-10 13:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, 'First name must be greater than 2 characters')])),
                ('last_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, 'Last name must be greater than 2 characters')])),
                ('email', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3, 'email must be greater than 3 characters')])),
                ('text', models.TextField()),
                ('picture', models.BinaryField(blank=True, editable=True, null=True)),
                ('content_type', models.CharField(blank=True, help_text='The MIMEType of the file', max_length=256, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
