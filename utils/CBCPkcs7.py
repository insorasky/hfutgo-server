import base64
from Crypto.Cipher import DES3


class CBCPkcs7:
    def __init__(self, key):
        self.key = key
        self.length = DES3.block_size
        self.des3 = DES3.new(self.key[0:24].encode('utf-8'), DES3.MODE_CBC, iv='activate'.encode())
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):
        res = self.des3.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData):
        res = base64.decodebytes(decrData.encode("utf8"))
        msg = self.des3.decrypt(res).decode("utf8")
        return self.unpad(msg)


if __name__ == '__main__':
    print(CBCPkcs7('eb68748e-b33a-461f-8916-e0f6a48861a9').encrypt('Bokura2020'))
