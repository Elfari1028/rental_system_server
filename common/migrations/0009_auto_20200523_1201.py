# Generated by Django 3.0.6 on 2020-05-23 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_supportrequestrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturegroup',
            name='pg_2',
            field=models.ImageField(blank=True, null=True, upload_to='images/PictureGroup/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='picturegroup',
            name='pg_3',
            field=models.ImageField(blank=True, null=True, upload_to='images/PictureGroup/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='picturegroup',
            name='pg_4',
            field=models.ImageField(blank=True, null=True, upload_to='images/PictureGroup/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='picturegroup',
            name='pg_5',
            field=models.ImageField(blank=True, null=True, upload_to='images/PictureGroup/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='picturegroup',
            name='pg_6',
            field=models.ImageField(blank=True, null=True, upload_to='images/PictureGroup/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='picturegroup',
            name='pg_7',
            field=models.ImageField(blank=True, null=True, upload_to='images/PictureGroup/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='picturegroup',
            name='pg_8',
            field=models.ImageField(blank=True, null=True, upload_to='images/PictureGroup/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='picturegroup',
            name='pg_9',
            field=models.ImageField(blank=True, null=True, upload_to='images/PictureGroup/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='supportrequestconversation',
            name='src_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]