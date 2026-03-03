import requests
from django.conf import settings
from .models import Currency

def update_exchange_rates():
    url = f"https://v6.exchangerate-api.com/v6/{settings.EXCHANGE_RATE_API_KEY}/latest/USD"
    response = requests.get(url)
    data = response.json()

    rates = data.get("conversion_rates", {})

    for code, rate in rates.items():
        Currency.objects.update_or_create(
            code=code,
            defaults={"rate_to_base": rate}
        )
