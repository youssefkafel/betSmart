from django import forms
from .models import Bankroll, Bet


class BetForm(forms.ModelForm):
    # create a form for creating bets
    class Meta:
        model = Bet
        fields = ('bankroll', 'event', 'stake', 'odds', 'result')


class BankrollForm(forms.ModelForm):
    # create a form for creating bankrolls
    class Meta:
        model = Bankroll
        fields = ('name', 'initial_balance')

