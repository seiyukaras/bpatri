# Generated by Django 3.0.9 on 2020-08-05 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buscar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichero', models.TextField()),
                ('tamanno', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
