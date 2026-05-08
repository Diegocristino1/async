import asyncio

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone


def home_view(request):
    return render(request, "timer/index.html")


async def contador_view(request):
    segundos = int(request.GET.get("segundos", 10))
    inicio = timezone.now().isoformat()
    timeline = []

    for i in range(1, segundos + 1):
        await asyncio.sleep(1)
        timeline.append({"tick": i, "tempo": timezone.now().isoformat()})

    fim = timezone.now().isoformat()

    return JsonResponse(
        {
            "mensagem": "Contador finalizado",
            "inicio": inicio,
            "fim": fim,
            "segundos": segundos,
            "timeline": timeline,
        }
    )
