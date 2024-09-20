from django.db import models

# Create your models here.



class Paiement(models.Model):
    id = models.BigAutoField(primary_key=True)
    raison = models.CharField(max_length=60, null=True, blank=True)
    paye_choix = {
        ("OUI", "Oui"),
        ('NON', "Non"),
    }

    paye = models.CharField(max_length=9, choices=paye_choix, default="Non")
    cout = models.IntegerField()

class Abonnement(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=60)
    paiement = models.ForeignKey(Paiement, on_delete=models.CASCADE, null=True, blank=True)  # Clé étrangère vers Paiement

class Compte(models.Model):
    id = models.BigAutoField(primary_key=True)
    login = models.CharField(max_length=60)
    mdp = models.CharField(max_length=60)
    question = models.CharField(max_length=60)
    date_debut = models.DateField()
    date_fin = models.DateField()
    abonnement = models.ForeignKey(Abonnement, on_delete=models.CASCADE, null=True, blank=True)  # Clé étrangère vers Abonnement

    def serialize(self):
        return {
            "id": self.id,
            "login": self.login,
            "mdp": self.mdp
        }    
    

