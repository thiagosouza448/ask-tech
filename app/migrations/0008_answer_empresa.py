# Generated by Django 2.1 on 2018-08-19 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_answer_data_resposta'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Empresa'),
            preserve_default=False,
        ),
    ]
