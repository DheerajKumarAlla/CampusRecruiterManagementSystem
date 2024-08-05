# Generated by Django 3.2.12 on 2022-03-03 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campusrecruiter', '0006_delete_applyjob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applyjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Resume', models.FileField(max_length=200, null=True, upload_to='')),
                ('ApplyDate', models.DateField(null=True)),
                ('Message', models.CharField(max_length=255, null=True)),
                ('Remark', models.CharField(max_length=255, null=True)),
                ('Status', models.CharField(max_length=255, null=True)),
                ('ResponseDate', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campusrecruiter.candidate')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campusrecruiter.vacancy')),
            ],
        ),
    ]