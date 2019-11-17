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
            return HttpResponse(json.dumps(validation.errors), status=400)

        playerClass = request_body.get('playerClass')
        cards = list(Card.objects.raw("""
        with cte as (
        SELECT *, ROW_NUMBER() OVER (PARTITION BY name ORDER BY RANDOM()) 
        AS rn FROM deck_card)
        SELECT dbfid, name, playerclass FROM cte 
        WHERE rn<=2 
        AND (playerclass='Neutral' OR playerclass=%s) 
        ORDER BY RANDOM() LIMIT 30;
        """, (playerClass,)))

        output = json.dumps([{'dbfId': c.dbfid,
                              'name': c.name,
                              'playerClass': c.playerclass} for c in cards])

        return HttpResponse(output)
    return HttpResponse(status=400)
