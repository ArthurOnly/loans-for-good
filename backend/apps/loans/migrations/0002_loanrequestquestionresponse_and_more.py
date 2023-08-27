# Generated by Django 4.2.4 on 2023-08-27 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanRequestQuestionResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_label', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('file', models.FileField(blank=True, null=True, upload_to='storage/loan_request_question_response')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='loanrequest',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['ordering']},
        ),
        migrations.AlterModelOptions(
            name='questionoption',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='response',
        ),
        migrations.AddIndex(
            model_name='question',
            index=models.Index(fields=['ordering'], name='loans_quest_orderin_0af968_idx'),
        ),
        migrations.AddField(
            model_name='loanrequestquestionresponse',
            name='loan_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.loanrequest'),
        ),
    ]
