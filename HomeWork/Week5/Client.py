from time import time
import re
import socket

WRONG_RESPONSE = 'error\nwrong command\n\n'

class ClientError(Exception):
    pass

class Client:
    def __init__(self, host, port, timeout=None):
        self.sock = socket.create_connection((host, port),timeout=timeout)

    def __enter__(self):
        return self

    def __exit__(self):
        self.sock.close()

    def put(self, metric, value, timestamp=str(int(time()))):
        data = 'put {key} {value} {timestamp}\n'.format(key=metric,
                                                         value=value,
                                                         timestamp=timestamp)
        try:
            self.sock.sendall(data.encode())
            self._check_response()
        except socket.error:
            raise ClientError("Connection unavailable.")

    @staticmethod
    def _resp_to_dict(resp):
        dict_container = {}
        if resp:
            for metric, value, timestamp in resp:
                dict_container[metric] = dict_container.get(metric, list())+\
                                         [(int(timestamp), float(value))]
            return dict_container
        else:
            return {}

    def _check_response(self):
        resp = self.sock.recv(1024).decode()
        if resp == WRONG_RESPONSE:
            raise ClientError('Wrong command.')
        else:
            return resp

    def get(self, key):
        msg = 'get {key}\n'.format(key=key)
        try:
            self.sock.sendall(msg.encode())
            response = re.findall('\n([\S]*) ([\.\d]*) ([\d]*)', self._check_response())
        except socket.error:
            raise ClientError("Connection unavailable.")
        return self._resp_to_dict(response)
