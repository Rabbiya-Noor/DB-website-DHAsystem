# Generated by Django 3.2.13 on 2022-04-29 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adha',
            fields=[
                ('adha_id', models.IntegerField(db_column='ADHA_ID', primary_key=True, serialize=False)),
                ('login_password', models.CharField(blank=True, max_length=20, null=True)),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('starting_date', models.DateField(blank=True, null=True)),
                ('ending_date', models.DateField(blank=True, null=True)),
                ('adha_rank', models.CharField(blank=True, db_column='ADHA_rank', max_length=20, null=True)),
            ],
            options={
                'db_table': 'adha',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('client_id', models.IntegerField(db_column='client_ID', primary_key=True, serialize=False)),
                ('login_password', models.CharField(blank=True, max_length=20, null=True)),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('user_rank', models.CharField(blank=True, max_length=20, null=True)),
                ('previous_employ', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'clients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('branch', models.CharField(blank=True, max_length=20, null=True)),
                ('director_rank', models.CharField(blank=True, max_length=20, null=True)),
                ('dir_id', models.IntegerField(db_column='dir_ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'director',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('emp_id', models.IntegerField(db_column='emp_ID', primary_key=True, serialize=False)),
                ('branch', models.CharField(blank=True, max_length=20, null=True)),
                ('typeemp', models.CharField(blank=True, max_length=20, null=True)),
                ('position', models.CharField(blank=True, max_length=20, null=True)),
                ('duration', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('alloted_plot_no', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
            ],
            options={
                'db_table': 'employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Plots',
            fields=[
                ('phase_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sector', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('size', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'plots',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Boat',
        ),
        migrations.DeleteModel(
            name='Reserve',
        ),
        migrations.DeleteModel(
            name='Sailor',
        ),
    ]
