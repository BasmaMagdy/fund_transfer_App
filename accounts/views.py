from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Account
from .forms import TransferForm

def list_accounts(request):
    accounts = Account.objects.all()
    return render(request, 'list_accounts.html', {'accounts': accounts})

def account_info(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    return render(request, 'account_info.html', {'account': account})

def transfer_funds(request):
    if request.method == "POST":
        form = TransferForm(request.POST)
        if form.is_valid():
            from_account = form.cleaned_data['from_account']
            to_account = form.cleaned_data['to_account']
            amount = form.cleaned_data['amount']

            try:
                from_account.transfer(to_account, amount)
                return JsonResponse({'status': 'success', 'message': 'Transfer successful'})
            except ValueError as e:
                return JsonResponse({'status': 'error', 'message': str(e)})

    form = TransferForm()
    return render(request, 'transfer_funds.html', {'form': form})
