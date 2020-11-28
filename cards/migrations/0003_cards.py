# Generated by Django 3.1.2 on 2020-11-28 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_learnset_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_side', models.CharField(max_length=200)),
                ('back_side', models.CharField(max_length=200)),
                ('success_counter', models.IntegerField()),
                ('failed_counter', models.IntegerField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('learn_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.learnset')),
            ],
        ),
    ]
