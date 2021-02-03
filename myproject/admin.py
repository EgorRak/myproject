from  django.contrib import admin
from .models import Client, Account , TransactionType , Transaction


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass
@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    pass
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
