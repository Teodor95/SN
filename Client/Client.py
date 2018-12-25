import random
import asyncoro.disasyncoro as asyncoro


def client_proc(n, coro=None):
    global msg_id
    server = yield coro.locate('server_coro')
    for x in range(3):
        yield coro.suspend(random.uniform(0.5, 3))
        msg_id += 1
        server.send('%d: %d / %d' % (msg_id, n, x))


msg_id = 0
for i in range(10):
    asyncoro.Coro(client_proc, i)
