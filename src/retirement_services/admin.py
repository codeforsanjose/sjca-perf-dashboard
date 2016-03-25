from django.contrib import admin
from .models import (RSOpExpenditure, RSAuthPosition,
                     RSRetireeBenefits, RSFederatedFundedPercent,
                     RSPoliceAndFireFundedPercent)

admin.site.register(RSOpExpenditure)
admin.site.register(RSAuthPosition)
admin.site.register(RSRetireeBenefits)
admin.site.register(RSFederatedFundedPercent)
admin.site.register(RSPoliceAndFireFundedPercent)
