# -*- coding: utf-8 -*-
from paddingoracle import BadPaddingException, PaddingOracle
from base64 import b64encode, b64decode
import requests


class PadBuster(PaddingOracle):
    def __init__(self, **kwargs):
        super(PadBuster, self).__init__(**kwargs)

    def oracle(self, data, **kwargs):
        check(data)


def check(data):
    b64data = b64encode(data)
    url = "http://127.0.0.1:8890/checkData"
    resp = requests.post(url=url, json={"encryptedText": b64data.decode()})
    result = resp.json()
    if not result["err"]:
        return
    raise BadPaddingException
    

if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.DEBUG)

    padbuster = PadBuster()

    enc = b64decode("/gerWmODMLIjp6d/pA6mbXkZp2ZtfNfer41oe7Vay4s=")
    res = padbuster.decrypt(enc, block_size=16, iv=bytearray(16))

    print(res)
