from os import name
from django.db import models
from django.utils import timezone

class Account(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def transfer(self, to_account, amount):
        """Transfers funds to another account."""
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        to_account.balance += amount
        self.save()
        to_account.save()
