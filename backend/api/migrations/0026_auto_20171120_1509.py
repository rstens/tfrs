# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 23:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20171120_1356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credittrade',
            old_name='fairMarketValuePerCredit',
            new_name='fair_market_value_per_credit',
        ),
        migrations.RenameField(
            model_name='credittrade',
            old_name='numberOfCredits',
            new_name='number_of_credits',
        ),
        migrations.RenameField(
            model_name='credittradehistory',
            old_name='creditTradeUpdateTime',
            new_name='credit_trade_update_time',
        ),
        migrations.RenameField(
            model_name='credittradehistory',
            old_name='newFairMarketValuePerCredit',
            new_name='fair_market_value_per_credit',
        ),
        migrations.RenameField(
            model_name='credittradehistory',
            old_name='isInternalHistoryRecord',
            new_name='is_internal_history_record',
        ),
        migrations.RenameField(
            model_name='credittradehistory',
            old_name='newNote',
            new_name='note',
        ),
        migrations.RenameField(
            model_name='credittradehistory',
            old_name='newNumberOfCredits',
            new_name='number_of_credits',
        ),
        migrations.RenameField(
            model_name='credittradestatus',
            old_name='displayOrder',
            new_name='display_order',
        ),
        migrations.RenameField(
            model_name='credittradetype',
            old_name='displayOrder',
            new_name='display_order',
        ),
        migrations.RenameField(
            model_name='credittradetype',
            old_name='isGovOnlyType',
            new_name='is_gov_only_type',
        ),
        migrations.RenameField(
            model_name='credittradetype',
            old_name='theType',
            new_name='the_type',
        ),
        migrations.RenameField(
            model_name='credittradezeroreason',
            old_name='displayOrder',
            new_name='display_order',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='createdDate',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='organizationactionstype',
            old_name='displayOrder',
            new_name='display_order',
        ),
        migrations.RenameField(
            model_name='organizationactionstype',
            old_name='theType',
            new_name='the_type',
        ),
        migrations.RenameField(
            model_name='organizationattachment',
            old_name='complianceYear',
            new_name='compliance_year',
        ),
        migrations.RenameField(
            model_name='organizationattachment',
            old_name='fileLocation',
            new_name='file_location',
        ),
        migrations.RenameField(
            model_name='organizationattachment',
            old_name='fileName',
            new_name='file_name',
        ),
        migrations.RenameField(
            model_name='organizationbalance',
            old_name='validatedCredits',
            new_name='validated_credits',
        ),
        migrations.RenameField(
            model_name='organizationhistory',
            old_name='historyText',
            new_name='history_text',
        ),
        migrations.RenameField(
            model_name='organizationstatus',
            old_name='displayOrder',
            new_name='display_order',
        ),
        migrations.RenameField(
            model_name='organizationtype',
            old_name='displayOrder',
            new_name='display_order',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='isGovernmentRole',
            new_name='is_government_role',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='authorizationDirectory',
            new_name='authorization_directory',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='guid',
            new_name='authorization_guid',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='authorizationID',
            new_name='authorization_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='givenName',
            new_name='given_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='userId',
        ),
    ]