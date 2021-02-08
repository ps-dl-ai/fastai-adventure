# Generated by Django 2.2.17 on 2021-02-08 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0016_answer_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsId', models.IntegerField(null=True, verbose_name='newsId')),
                ('author', models.CharField(max_length=256, null=True)),
                ('title', models.CharField(max_length=256, null=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('newsImage', models.ImageField(default=False, upload_to='')),
                ('publishedAt', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='increase_or_decrease',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='stock',
            name='last_pattern',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
