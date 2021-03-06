import json
from django.test import TestCase, Client

from rest_framework import status
from api.models.User import User

# Credit Trade Statuses
STATUS_DRAFT = 1
STATUS_SUBMITTED = 2
STATUS_ACCEPTED = 3
STATUS_RECOMMENDED = 4
STATUS_APPROVED = 6
STATUS_COMPLETED = 7
STATUS_CANCELLED = 8
STATUS_DECLINED = 9


class TestCreditTrades(TestCase):
    fixtures = ['organization_types.json',
                'organization_government.json',
                'organization_balance_gov.json',
                'credit_trade_statuses.json',
                'organization_actions_types.json',
                'organization_statuses.json',
                'test_users.json',
                'credit_trade_types.json',
                'test_credit_trades.json',
                'test_organization_fuel_suppliers.json',
                'test_organization_balances.json',
                ]

    def setUp(self):

        # Initialize Foreign keys
        self.test_url = "/api/credit_trades"

        self.gov_user = User.objects.filter(organization__id=1).first()
        self.gov_client = Client(
            HTTP_SMGOV_USERGUID=str(self.gov_user.authorization_guid),
            HTTP_SMGOV_USERDISPLAYNAME=self.gov_user.display_name,
            HTTP_SMGOV_USEREMAIL=self.gov_user.email,
            HTTP_SM_UNIVERSALID=self.gov_user.authorization_id,
            HTTP_SMGOV_USERTYPE='Internal',
            HTTP_SM_AUTHDIRNAME='IDIR')

        self.user_1 = User.objects.filter(organization__id=2).first()
        self.fs_client_1 = Client(
            HTTP_SMGOV_USERGUID=str(self.user_1.authorization_guid),
            HTTP_SMGOV_USERDISPLAYNAME=self.user_1.display_name,
            HTTP_SMGOV_USEREMAIL=self.user_1.email,
            HTTP_SM_UNIVERSALID=self.user_1.authorization_id)

        self.user_2 = User.objects.filter(organization__id=3).first()
        self.fs_client_2 = Client(
            HTTP_SMGOV_USERGUID=str(self.user_2.authorization_guid),
            HTTP_SMGOV_USERDISPLAYNAME=self.user_2.display_name,
            HTTP_SMGOV_USEREMAIL=self.user_2.email,
            HTTP_SM_UNIVERSALID=self.user_2.authorization_id)

        self.user_3 = User.objects.filter(organization__id=4).first()
        self.fs_client_3 = Client(
            HTTP_SMGOV_USERGUID=str(self.user_3.authorization_guid),
            HTTP_SMGOV_USERDISPLAYNAME=self.user_3.display_name,
            HTTP_SMGOV_USEREMAIL=self.user_3.email,
            HTTP_SM_UNIVERSALID=self.user_3.authorization_id)

    # As a fuel supplier, I should see all credit trades where:
    # I'm the initiator, regardless of status
    # I'm the respondent, if the status is "submitted" or greater
    def test_initiator_should_see_appropriate_credit_trades(self):
        response = self.fs_client_1.get('/api/credit_trades')
        assert response.status_code == status.HTTP_200_OK

        fs_credit_trades = response.json()
        for ct in fs_credit_trades:
            correct_view = False
            if ct['initiator']['id'] == self.user_1.organization.id:
                correct_view = True
            elif (ct['respondent']['id'] == self.user_1.organization.id and
                  ct['status']['id'] >= STATUS_SUBMITTED):
                correct_view = True
            assert correct_view is True

    # As a government user, I should see all credit trades where:
    # I'm the initiator, regardless of status
    # Government will never be the respondent
    # All other credit trades that have the status "Accepted" or greater
    def test_government_user_should_see_appropriate_credit_trades(self):
        response = self.gov_client.get('/api/credit_trades')
        print(response.content)
        assert response.status_code == status.HTTP_200_OK

        gov_credit_trades = response.json()
        for ct in gov_credit_trades:
            correct_view = False
            if ct['initiator']['id'] == self.gov_user.organization.id:
                correct_view = True
            elif ct['status']['id'] >= STATUS_ACCEPTED and \
                    ct['status']['id'] != STATUS_CANCELLED:
                correct_view = True
            assert correct_view is True
