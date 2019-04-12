# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-31 19:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trans', '0024_resolve_auto_format'),
        ('accounts', '0004_create_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(choices=[('MergeFailureNotification', 'Merge failure'), ('ParseErrorNotification', 'Parse error'), ('NewStringNotificaton', 'New string'), ('NewContributorNotificaton', 'New contributor'), ('NewSuggestionNotificaton', 'New suggestion'), ('LastAuthorCommentNotificaton', 'Comment on authored translation'), ('MentionCommentNotificaton', 'Mentioned in comment'), ('NewCommentNotificaton', 'New comment'), ('ChangedStringNotificaton', 'Changed string'), ('NewTranslationNotificaton', 'New language'), ('NewComponentNotificaton', 'New translation component'), ('NewWhiteboardMessageNotificaton', 'New whiteboard message'), ('NewAlertNotificaton', 'New component alert')], max_length=100)),
                ('scope', models.IntegerField(choices=[(10, 'Defaults'), (20, 'Admin'), (30, 'Project'), (40, 'Component')])),
                ('frequency', models.IntegerField(choices=[(0, 'Disabled'), (1, 'Instant notification'), (2, 'Daily digest'), (3, 'Weekly digest'), (4, 'Monthly digest')])),
                ('component', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.Component')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set([('notification', 'scope', 'project', 'component', 'user')]),
        ),
    ]
