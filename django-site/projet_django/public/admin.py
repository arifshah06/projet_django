from django.contrib import admin

from .models import Compte

from .models import Abonnement

from .models import Paiement


# Register your models here.


@admin.register(Compte)
class CompteAdmin(admin.ModelAdmin):

    pass


@admin.register(Abonnement)
class AbonnementAdmin(admin.ModelAdmin):

    pass


@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):

    pass