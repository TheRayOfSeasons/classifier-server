# Generated by Django 3.2.7 on 2021-09-18 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        ('trees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EpiphyticOrganism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.IntegerField()),
                ('modified_by', models.IntegerField()),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.IntegerField()),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'epiphytic_organisms',
            },
        ),
        migrations.CreateModel(
            name='Specimen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.IntegerField()),
                ('modified_by', models.IntegerField()),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.IntegerField()),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=64)),
                ('with_stain', models.BooleanField(default=False)),
                ('state_of_decay', models.CharField(choices=[('loose', 'Loose'), ('moderately_intact', 'Moderately Intact'), ('intact', 'Intact')], max_length=32)),
                ('bark_texture', models.CharField(choices=[('smooth', 'Smooth'), ('rough', 'Rough')], max_length=8)),
                ('date_of_collection', models.DateTimeField()),
            ],
            options={
                'db_table': 'specimens',
            },
        ),
        migrations.CreateModel(
            name='SpecimenDirectionalBreakdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.DecimalField(decimal_places=8, max_digits=16)),
                ('second', models.DecimalField(decimal_places=8, max_digits=16)),
                ('third', models.DecimalField(decimal_places=8, max_digits=16)),
            ],
            options={
                'db_table': 'specimen_directional_breakdowns',
            },
        ),
        migrations.CreateModel(
            name='SpecimenEpiphyticOrganism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epiphytic_organism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specimens.epiphyticorganism')),
                ('specimen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specimens.specimen')),
            ],
            options={
                'db_table': 'specimen_epiphytic_organisms',
            },
        ),
        migrations.CreateModel(
            name='SpecimenDirectionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('east', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specimens_east_direction_set', to='specimens.specimendirectionalbreakdown')),
                ('north', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specimens_north_direction_set', to='specimens.specimendirectionalbreakdown')),
                ('south', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specimens_south_direction_set', to='specimens.specimendirectionalbreakdown')),
                ('west', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specimens_west_direction_set', to='specimens.specimendirectionalbreakdown')),
            ],
            options={
                'db_table': 'specimen_direction_data',
            },
        ),
        migrations.AddField(
            model_name='specimen',
            name='direction_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specimens.specimendirectiondata'),
        ),
        migrations.AddField(
            model_name='specimen',
            name='host_tree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trees.tree'),
        ),
        migrations.AddField(
            model_name='specimen',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='locations.location'),
        ),
    ]
