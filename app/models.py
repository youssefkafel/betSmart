from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Bankroll(models.Model):
    # create fields for the bankroll model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    win_count = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    loss_count = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    def save(self, *args, **kwargs):
        # Set the initial balance as the current balance when the bankroll is created
        if not self.pk:
            self.balance = self.initial_balance

        super().save(*args, **kwargs)

    def calculate_profit(self):
        self.profit = self.balance - self.initial_balance

    def __str__(self):
        return self.name


class Bet(models.Model):
    # create fields for the bet model
    bankroll = models.ForeignKey(Bankroll, on_delete=models.CASCADE)
    event = models.CharField(max_length=255)
    stake = models.DecimalField(max_digits=10, decimal_places=2)
    odds = models.DecimalField(max_digits=5, decimal_places=2)
    result = models.CharField(max_length=255)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Set the initial balance as the current balance when the bankroll is created
        if not self.pk:
            if self.result == "Won":
                self.profit = self.stake * self.odds
                self.bankroll.balance += self.profit
                self.bankroll.profit += self.profit
                self.bankroll.win_count += 1
            if self.result == "Lost":
                self.profit = 0 - self.stake
                self.bankroll.balance += self.profit
                self.bankroll.profit += self.profit
                self.bankroll.loss_count += 1
            if self.result == "Pending":
                self.profit = 0
                self.bankroll.balance += self.profit
                self.bankroll.profit += self.profit
        self.bankroll.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.event
