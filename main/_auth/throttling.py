from rest_framework.throttling import UserRateThrottle
from django.contrib.auth.models import User


class RoleBasedThrottle(UserRateThrottle):
    rates_by_role = {
        'admin': '100000/hour',
        'user': '10000/hour',
        'anonymous': '1000/hour',
    }

    def get_rate(self):
        user = self.scope if hasattr(self, 'scope') else None
        if isinstance(user, User) and user.is_authenticated:
            if user.is_staff:
                return self.rates_by_role.get('admin')
            return self.rates_by_role.get('user')
        return self.rates_by_role.get('anonymous')
