# Generated by Django 3.0.6 on 2020-05-23 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20200523_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportRequestConversation',
            fields=[
                ('src_id', models.AutoField(primary_key=True, serialize=False)),
                ('src_content', models.CharField(max_length=256)),
                ('src_time', models.IntegerField()),
                ('pg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.PictureGroup')),
                ('sr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='src_sr_id', to='common.SupportRequest')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='src_u_id', to='common.Users')),
            ],
        ),
    ]
