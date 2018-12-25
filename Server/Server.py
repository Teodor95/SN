import sys
import asyncoro.disasyncoro as asyncoro


def server_proc(coro=None):
    coro.set_daemon()
    coro.register('server_coro')
    while True:
        msg = yield coro.receive()
        print('processing %s' % (msg))


server = asyncoro.Coro(server_proc)
while True:
    cmd = sys.stdin.readline().strip().lower()
    if cmd == 'quit' or cmd == 'exit':
        break
