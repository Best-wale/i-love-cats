import requests
import logging
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

def profile_view(request):
    """
    Returns user info + random cat fact + timestamp oya na
    """
    #if the thing no work  he go just use this one
    fact = "Cats are wonderful creatures!"  

    try:
        res = requests.get(
            "https://catfact.ninja/fact",
            timeout=3
        )
        if res.status_code == 200:
            fact = res.json().get("fact", fact)
    except Exception as e:
        logger.warning(f"Cat fact API failed: {e}")

    data = {
        "status": "success",
        "user": {
            "email": 'Bestigbekele5@gmail.com',
            "name": 'Best Igbekele',
            "stack": 'Python/Django',
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": fact,
    }

    return JsonResponse(data, status=200)
