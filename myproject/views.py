from django.http import HttpResponse,JsonResponse
from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from myproject.models import Client
from myproject.models import Account
from myproject.models import TransactionType
from myproject.models import Transaction

import json

class HomePageView(TemplateView):
    template_name = 'HomePageView.html'
    def get_context_data(self, **kwargs):

        clients = Client.objects.all()
        accounts = Account.objects.all()
        transactionTypes = TransactionType.objects.all()
        transactions = Transaction.objects.all()
        return {
                'clients': clients,
                'accounts': accounts,
                'transactionTypes': transactionTypes,
                'transactions': transactions
            }

class EndPointView(TemplateView):
    template_name = 'EndPointView.html'
    def get_context_data(self, **kwargs):
        clients = Client.objects.all()
        accounts = Account.objects.all()
        transactionTypes = TransactionType.objects.all()
        transactions = Transaction.objects.all()
        return {
            'clients': clients,
            'accounts': accounts,
            'transactionTypes': transactionTypes,
            'transactions': transactions
        }
