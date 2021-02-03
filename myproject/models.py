from django.db import models


"""2. Создать модели:
- Client (клиент): first_name (string), last_name (string), birth (datetime), identity_code (ИНН - integer, unique), passport (string, unique), client_type (string, [“INTERNAL”, “HUMAN”])
- Account (счет): iban (string (29), unique), client (FK -> Client), balance (positive integer, в копейках, default 0), name (string)
 TransactionType (тип операции): name (string (255)), code (positive integer, unique).
- Transaction (транзакция): transaction_type (FK -> TransactionType), amount (integer, в копейках), debit_account (FK -> Account), credit_account (FK -> Account), created (datetime, default now), description (string (255)).
"""


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth = models.DateTimeField(null=True, blank=True)
    identity_code = models.PositiveSmallIntegerField(unique=True)
    passport = models.CharField(max_length=100, unique=True)
    client_type = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"Client {self.first_name} {self.last_name} {self.birth} {self.identity_code} {self.passport} {self.client_type}"


class Account(models.Model):
    iban = models.CharField(max_length=29, unique=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    balance = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=100)


class TransactionType(models.Model):
    name = models.CharField(max_length=255)
    code = models.PositiveSmallIntegerField(unique=True)


class Transaction(models.Model):
    transaction_type = models.ForeignKey("TransactionType", on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
    debit_account = models.ForeignKey('Account', on_delete=models.CASCADE)
    credit_account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='candidate_details', null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=255)