from django.test import TestCase
from django.urls import reverse
from accounts.models import Account

class AccountTests(TestCase):
    def setUp(self):
        self.account_1 = Account.objects.create(name="John", balance=100.00)
        self.account_2 = Account.objects.create(name="Jane", balance=50.00)

    def test_account_list(self):
        response = self.client.get(reverse('list_accounts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John")
        self.assertContains(response, "Jane")

    def test_account_info(self):
        response = self.client.get(reverse('account_info', args=[self.account_1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John")

    def test_transfer_funds(self):
        response = self.client.post(reverse('transfer_funds'), {
            'from_account': self.account_1.id,
            'to_account': self.account_2.id,
            'amount': 30.00,
        })
        self.assertEqual(response.status_code, 200)
        self.account_1.refresh_from_db()
        self.account_2.refresh_from_db()
        self.assertEqual(self.account_1.balance, 70.00)
        self.assertEqual(self.account_2.balance, 80.00)
