import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from .models import Card
from .serializers import InputSerializer


@api_view(['POST'])
def index(request):
    if request.method == 'POST':
        request_body = request.data
        validation = InputSerializer(data=request_body)

        if not validation.is_valid():
            return JsonResponse(validation.errors, status=400)

        playerClass = request_body.get('playerClass')
        cards = list(Card.objects.raw("""
        with cte as (
            SELECT *, ROW_NUMBER() OVER (PARTITION BY name) 
            AS rn FROM deck_card)
            SELECT dbfId, name, playerClass FROM cte 
            WHERE rn<=2 
            AND (playerClass='Neutral' OR playerClass=%s) 
            LIMIT 30;
        """, (playerClass,)))

        output = json.dumps([{'dbfId': c.dbfId,
                              'name': c.name,
                              'playerClass': c.playerClass} for c in cards])

        return HttpResponse(output)
    return HttpResponse(status=400)
