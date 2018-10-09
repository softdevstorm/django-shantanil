# Generated by Django 2.1.1 on 2018-10-09 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('code_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('code_type', models.CharField(max_length=100)),
                ('code_name', models.IntegerField()),
                ('code_value', models.IntegerField()),
                ('code_description', models.TextField()),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cdg_code',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('content_type_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('content_type_name', models.CharField(max_length=50)),
                ('content_type_short', models.CharField(max_length=100)),
                ('content_type_long_description', models.TextField()),
                ('content_type_is_active', models.BooleanField(default=False)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cdg_content_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CurrentSchedule',
            fields=[
                ('cs_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('cs_name', models.CharField(max_length=100)),
                ('cs_command', models.CharField(max_length=200)),
                ('cs_parameters', models.CharField(max_length=100)),
                ('cs_runtime', models.CharField(max_length=50)),
                ('cs_frequency', models.CharField(max_length=100)),
                ('cs_description', models.TextField()),
                ('cs_is_active', models.BooleanField(default=False)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cdg_current_schedules',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CurrentScheduleActivities',
            fields=[
                ('csa_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('csa_name', models.CharField(max_length=100)),
                ('csa_command', models.CharField(max_length=200)),
                ('csa_parameters', models.CharField(max_length=100)),
                ('csa_runtime', models.CharField(max_length=50)),
                ('csa_frequency', models.CharField(max_length=100)),
                ('csa_jobstatus', models.CharField(max_length=30)),
                ('csa_job_starttime', models.DateTimeField(auto_now_add=True)),
                ('csa_job_endtime', models.DateTimeField(auto_now=True)),
                ('csa_job_run_duration', models.DateTimeField()),
                ('csa_run_errors', models.CharField(max_length=200)),
                ('csa_run_output', models.CharField(max_length=200)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
                ('cs_seq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.CurrentSchedule')),
            ],
            options={
                'db_table': 'cdg_current_schedules_activities',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('dataset_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('dataset_name', models.CharField(max_length=50)),
                ('dataset_description', models.TextField()),
                ('dataset_is_active', models.BooleanField(default=False)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
                ('dataset_content_type_seq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.ContentType')),
            ],
            options={
                'db_table': 'cdg_dataset',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DatasetAttribute',
            fields=[
                ('dataset_attribute_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('dataset_attribute_name', models.CharField(max_length=100)),
                ('da_source_col_seq', models.IntegerField()),
                ('da_source_col_name', models.CharField(max_length=100)),
                ('da_sample_col_data', models.CharField(max_length=100)),
                ('da_source_col_type', models.CharField(max_length=100)),
                ('is_pii_yn', models.CharField(max_length=100)),
                ('da_source_col_size_1', models.CharField(max_length=50)),
                ('da_source_col_size_2', models.CharField(max_length=50)),
                ('da_source_col_short_desc', models.CharField(max_length=200)),
                ('da_is_active', models.BooleanField(default=False)),
                ('dataset_attributes_is_profiled', models.BooleanField(default=False)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
                ('content_type_seq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.ContentType')),
                ('da_dataset_seq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.DataSet')),
            ],
            options={
                'db_table': 'cdg_dataset_attribute',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DatasetLineage',
            fields=[
                ('dataset_lineage_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('dl_dataset_name', models.CharField(max_length=100)),
                ('dl_dataset_type', models.CharField(max_length=200)),
                ('dl_comment', models.TextField()),
                ('dl_is_active', models.BooleanField(default=False)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cdg_dataset_lineage',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataStore',
            fields=[
                ('datastore_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('datastore_name', models.CharField(max_length=100)),
                ('datastore_host', models.CharField(max_length=50)),
                ('datastore_port', models.CharField(max_length=50)),
                ('datastore_directory', models.CharField(max_length=100)),
                ('datastore_connection_type', models.CharField(max_length=50)),
                ('ec_connection_success_flag', models.BooleanField(default=False)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cdg_datastore',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EstablishedConnections',
            fields=[
                ('established_connections_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('ec_name', models.CharField(max_length=100)),
                ('ec_userid', models.CharField(max_length=100)),
                ('ec_password', models.CharField(max_length=200)),
                ('ec_host', models.CharField(max_length=50)),
                ('ec_port', models.CharField(max_length=50)),
                ('ec_connectstring', models.CharField(max_length=200)),
                ('ec_connection_type', models.CharField(max_length=50)),
                ('ec_connection_success_flag', models.BooleanField(default=False)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
                ('ec_datastore_seq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.DataStore')),
            ],
            options={
                'db_table': 'cdg_established_connections',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EstablishedSource',
            fields=[
                ('established_sources_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('es_name', models.CharField(max_length=50)),
                ('es_source_type', models.CharField(max_length=50)),
                ('es_schema', models.CharField(max_length=100)),
                ('es_directory', models.CharField(max_length=200)),
                ('es_connect_string', models.CharField(max_length=100)),
                ('es_is_active', models.BooleanField(default=False)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
                ('es_established_connections_seq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.EstablishedConnections')),
            ],
            options={
                'db_table': 'cdg_established_sources',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EstablishedTarget',
            fields=[
                ('established_target_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('et_source_name', models.CharField(max_length=50)),
                ('et_type', models.CharField(max_length=50)),
                ('et_schema', models.CharField(max_length=100)),
                ('et_directory', models.CharField(max_length=200)),
                ('et_connect_string', models.CharField(max_length=100)),
                ('et_is_active', models.BooleanField(default=False)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
                ('et_established_connections_seq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.EstablishedConnections')),
            ],
            options={
                'db_table': 'cdg_established_target',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Functions',
            fields=[
                ('functions_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('functions_name', models.CharField(max_length=100)),
                ('functions_type', models.CharField(max_length=100)),
                ('functions_description', models.TextField()),
                ('functions_parameters', models.CharField(max_length=100)),
                ('functions_is_active', models.BooleanField(default=True)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cdg_functions',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InstalledDriver',
            fields=[
                ('installed_drivers_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('installed_drivers_name', models.CharField(max_length=100)),
                ('driver_version', models.CharField(max_length=30)),
                ('driver_description', models.TextField()),
                ('install_pip_cmd', models.CharField(max_length=50)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cdg_installed_drivers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SourceLineage',
            fields=[
                ('source_lineage_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('sl_source_name', models.CharField(max_length=100)),
                ('sl_comment', models.TextField()),
                ('sl_is_active', models.BooleanField(default=False)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
                ('sl_content_type_seq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.ContentType')),
                ('sl_established_sources_seq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.EstablishedSource')),
            ],
            options={
                'db_table': 'cdg_source_lineage',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SupportDriver',
            fields=[
                ('supported_driver_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('driver_official_pip_name', models.CharField(max_length=200)),
                ('driver_description', models.TextField()),
                ('driver_version', models.CharField(max_length=50)),
                ('driver_for_source_system_name', models.CharField(max_length=100)),
                ('driver_icon_path', models.FilePathField()),
                ('driver_for_source_type', models.CharField(max_length=50)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cdg_supported_drivers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserLogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('login_timestamp', models.DateTimeField(auto_now_add=True)),
                ('logout_timestamp', models.DateTimeField(auto_now_add=True)),
                ('login_hostname', models.TextField()),
                ('login_ipaddress', models.TextField()),
                ('comments', models.TextField()),
                ('is_session_active', models.BooleanField(default=False)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cdg_user_logger',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='installeddriver',
            name='supported_driver_seq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.SupportDriver'),
        ),
        migrations.AddField(
            model_name='establishedconnections',
            name='ec_installed_drivers_seq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.InstalledDriver'),
        ),
        migrations.AddField(
            model_name='datastore',
            name='datastore_installed_drivers_seq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.InstalledDriver'),
        ),
        migrations.AddField(
            model_name='datasetlineage',
            name='dl_child1_target_seq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.EstablishedTarget'),
        ),
        migrations.AddField(
            model_name='datasetlineage',
            name='dl_content_type_seq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.ContentType'),
        ),
        migrations.AddField(
            model_name='datasetlineage',
            name='dl_dataset_seq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.DataSet'),
        ),
        migrations.AddField(
            model_name='datasetlineage',
            name='dl_parent1_sources_seq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.EstablishedSource'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='dataset_established_sources_seq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.EstablishedSource'),
        ),
    ]
