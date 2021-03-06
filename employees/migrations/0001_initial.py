# Generated by Django 3.2 on 2021-06-28 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('budget', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('description', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('startDate', models.DateField(null=True)),
                ('terminationDate', models.DateField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.department')),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField(null=True)),
                ('gross_salary', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('taxes', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('net_salary', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('benefits', models.CharField(choices=[('MP', 'Medical plan'), ('DP', 'Dental plan'), ('GY', 'Gym'), ('N', 'None')], default='N', max_length=2)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
    ]
