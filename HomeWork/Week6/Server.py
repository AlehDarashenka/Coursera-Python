import asyncio
import re

WRONG_RESPONSE = 'error\nwrong command\n\n'
GENERIC_RESPONSE = 'ok\n\n'

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()




class ClientServerProtocol(asyncio.Protocol):

    storage = {}

    def connection_made(self, transport):
        self.transport = transport


    def put_storage(self, data):
        print(data)
        metric, value, timestamp = re.findall('([\S]*) ([\.\d]*) ([\d]*)\n', data)[0]
        print([(value, timestamp)])
        self.storage[metric] = self.storage.get(metric, list())+[(value, timestamp)]
        print(self.storage)
        self.storage[metric] = list(set(self.storage[metric]))
        self.storage[metric].sort(key=lambda x: x[1])
        print(self.storage)
        return GENERIC_RESPONSE


    def get_value(self, data):
        print (data)
        print(self.storage)

        if data == '*':
            resp = [' '.join(map(str, [key, value, datetime]))
                          for key in self.storage for value, datetime in self.storage[key]]
        else:
            try:
                resp = [' '.join(map(str, [data, value, datetime])) for value, datetime in self.storage[data]]
            except KeyError:
                return GENERIC_RESPONSE
        print( repr('ok\n'+'\n'.join(resp)+'\n'))
        return 'ok\n'+'\n'.join(resp)+'\n\n'

    def process_data(self, data):
        if data.startswith('get'):
            metric = re.findall('([\S]*)\n', data)
            return self.get_value(metric[0])
        elif data.startswith('put'):
            return self.put_storage(data)
        else:
            return WRONG_RESPONSE

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())



if __name__=='__main_':
    run_server('127.0.0.1', 8181)

