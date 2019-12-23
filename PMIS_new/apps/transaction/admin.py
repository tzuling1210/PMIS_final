from django.contrib import admin
from .models import Transaction, Transaction_product

from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Transaction)
# admin.site.register(Transaction)
# admin.site.register(Transaction_product)
class TransactionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'date', 'total_price', 'member_id')

@admin.register(Transaction_product)
class Transaction_productAdmin(ImportExportModelAdmin):
    list_display = ('id', 'quantity', 'price', 'product_id', 'transaction_id')