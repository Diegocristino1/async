import asyncio
import httpx
from django.http import HttpResponse

# funcao assincrona que faz uma chamada HTTP e retorna o resultado
async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/get")
        print(r.status_code, r.text)


async def async_view(request):
    await http_call_async()
    return HttpResponse("OK")