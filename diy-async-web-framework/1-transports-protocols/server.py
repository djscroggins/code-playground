import asyncio


class Server(asyncio.Protocol):
    def connection_made(self, transport):
        self._transport = transport

    def data_received(self, data):
        message = data.decode()

        self._transport.write(data)

        self._transport.close()


loop = asyncio.get_event_loop()

coro = loop.create_server(Server, '127.0.0.1', 8080)
server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
