from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill


