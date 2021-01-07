from aiohttp import web, MultipartReader


async def get_business_request(request):
    # print(request.business)
    return web.Response(text="Hello world", status=200)



app = web.Application()

app.router.add_route('GET', '/', get_business_request)

web.run_app(app, host='0.0.0.0', port=6789)