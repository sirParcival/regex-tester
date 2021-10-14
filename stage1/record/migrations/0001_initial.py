# Generated by Django 3.2.8 on 2021-10-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regex', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=1024)),
                ('result', models.BooleanField()),
            ],
        ),
    ]
