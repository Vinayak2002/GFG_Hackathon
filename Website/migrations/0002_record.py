# Generated by Django 2.2.5 on 2022-06-24 09:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('voice_record', models.FileField(upload_to='records')),
                ('language', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Record',
                'verbose_name_plural': 'Records',
            },
        ),
    ]
