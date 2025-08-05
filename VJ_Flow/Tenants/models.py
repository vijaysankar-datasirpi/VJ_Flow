from django.db import models
from django_tenants.models import TenantMixin,DomainMixin

class Tenant(TenantMixin):
    name = models.CharField(max_length=100)


    auto_create_schema = True

    def __str__(self):
        return self.name
    
class Domain(DomainMixin):
    pass