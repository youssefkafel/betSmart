from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BankrollForm, BetForm
from .models import Bankroll, Bet


# Create your views here.
@login_required(login_url='login')
def index(request):
    bankroll = Bankroll.objects.filter(user_id=request.user.id)
    context = {'bankrolls': bankroll}
    return render(request, 'app/dashboard.html', context)


@login_required(login_url='login')
def index_bankroll(request, id):
    bet = Bet.objects.filter(bankroll_id=id)
    bankroll = Bankroll.objects.filter(id=id)
    context = {'bets': bet, 'bankrolls': bankroll}
    return render(request, 'app/bankroll.html', context)


@login_required(login_url='login')
def create_bankroll(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = BankrollForm(request.POST)  # request.FILES is added for the image field
        # check whether it's valid:
        if form.is_valid():
            # Assign the current user as the user (i.e., owner) for each task
            form.instance.user = request.user
            # save the record into the db
            form.save()
            # after saving redirect to dashboard page
            return redirect('dashboard')
    else:
        # if the request does not have post data, a blank form will be rendered
        form = BankrollForm()

    return render(request, 'app/create-bankroll.html', {'form': form})


@login_required(login_url='login')
def update_bankroll(request, bankroll_id):
    # Get the product based on its id
    bankroll = Bankroll.objects.get(id=bankroll_id, user=request.user)

    if request.method == 'POST':
        # populate a form instance with data from the data on the database
        # instance=product allows to update the record rather than creating a new record when save method is called
        form = BankrollForm(request.POST, instance=bankroll) # request.FILES is added for the image field
        # check whether it's valid:
        if form.is_valid():
            # Assign the current user as the user (i.e., owner) for each task
            form.instance.user = request.user
            # update the record in the db
            form.save()
            # after updating redirect to index page
            return redirect('dashboard')
    else:
        # if the request does not have post data, render the page with the form containing the product's info
        form = BankrollForm(instance=bankroll)

    return render(request, 'app/update-bankroll.html', {'form': form})


@login_required(login_url='login')
def create_bet(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = BetForm(request.POST)  # request.FILES is added for the image field
        # check whether it's valid:
        if form.is_valid():
            # Assign the current user as the user (i.e., owner) for each task
            form.instance.user = request.user
            # save the record into the db
            form.save()
            # after saving redirect to dashboard page
            return redirect('dashboard')
    else:
        # if the request does not have post data, a blank form will be rendered
        form = BetForm()

    return render(request, 'app/create-bet.html', {'form': form})


@login_required(login_url='login')
def update_bet(request, bet_id):
    # Get the product based on its id
    bet = Bet.objects.get(id=bet_id, user=request.user)

    if request.method == 'POST':
        # populate a form instance with data from the data on the database
        # instance=product allows to update the record rather than creating a new record when save method is called
        form = BetForm(request.POST, request.FILES, instance=bet) # request.FILES is added for the image field
        # check whether it's valid:
        if form.is_valid():
            # Assign the current user as the user (i.e., owner) for each task
            form.instance.user = request.user
            # update the record in the db
            form.save()
            # after updating redirect to index page
            return redirect('dashboard')
    else:
        # if the request does not have post data, render the page with the form containing the product's info
        form = BetForm(instance=bet)

    return render(request, 'app/update-bet.html', {'form': form})
