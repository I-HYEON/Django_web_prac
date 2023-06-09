# Generated by Django 3.2.18 on 2023-03-30 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('contents', models.TextField()),
                ('category', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('contents', models.TextField()),
                ('post_id', models.ForeignKey(db_column='post_id', on_delete=django.db.models.deletion.CASCADE, related_name='post', to='articles.article')),
            ],
        ),
    ]
