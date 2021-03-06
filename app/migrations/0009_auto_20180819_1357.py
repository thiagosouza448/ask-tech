# Generated by Django 2.1 on 2018-08-19 16:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_answer_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='data_resposta',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='question',
            name='resposta',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Empresa'),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
