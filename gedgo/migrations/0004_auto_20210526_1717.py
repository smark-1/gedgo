# Generated by Django 3.0 on 2021-05-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gedgo', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='uploads/comments'),
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='document',
            name='kind',
            field=models.CharField(choices=[('DOCUM', 'Document'), ('VIDEO', 'Video'), ('PHOTO', 'Image')], max_length=5),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_approxQ',
            field=models.BooleanField(verbose_name='Date is approximate'),
        ),
        migrations.AlterField(
            model_name='family',
            name='kind',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Event'),
        ),
    ]