from Crypto.Cipher import AES
import re
key = 'wrdvpnisthebest!'
iv = 'wrdvpnisthebest!'


def AES_128_CFB(String):
    cryptor = AES.new(key=key.encode('utf-8'), mode=AES.MODE_CFB, IV=iv.encode('utf-8'), segment_size=128)
    ciphertext = cryptor.encrypt(String.encode('utf-8'))
    return ciphertext


def AES_128_CFB_decode(String):
    decode = String.decode('hex')
    cryptor = AES.new(key=key.encode('utf-8'), mode=AES.MODE_CFB, IV=iv.encode('utf-8'), segment_size=128)
    plain_text = cryptor.decrypt(decode.encode('utf-8'))
    return plain_text


def textRightAppend(text, mode):
    segmentByteSize = 16 if mode == 'utf8' else 32
    if len(text) % segmentByteSize == 0:
        return text
    appendLength = segmentByteSize - len(text) % segmentByteSize
    i = 1
    while i < appendLength:
        i += 1
        text += '0'
    return text


def encrypt(text):
    textLength = len(text)
    text = textRightAppend(text, 'utf8')
    encryptBytes = AES_128_CFB(text).hex()
    return iv.encode().hex() + encryptBytes[0: textLength * 2]


def encrypUrl(protorol, url):
    port = ''
    segments = ''
    if url[0: 7] == 'http://':
        url = url[7:]
    elif url[0: 8] == 'https://':
        url = url[8:]
    v6 = ''
    match = re.match(r'/\[[0-9a-fA-F:]+?\]/', url)
    if match:
        v6 = match[0]
        url = url[slice(match[0].length)]
    segments = url.split('?')[0].split(':')
    if len(segments) > 1:
        port = segments[1].split('/')[0]
        url = url[0: len(segments[0])] + url[len(segments[0]) + len(port) + 1:]
    if protorol != 'connection':
        i = url.find('/')
        if i == -1:
            if v6 != '':
                url = v6
            url = encrypt(url)
        else:
            host = url[0: i]
            path = url[i:]
            if v6 != '':
                host = v6
            url = encrypt(host) + path
    if port != '':
        url = '/' + protorol + '-' + port + '/' + url
    else:
        url = '/' + protorol + '/' + url
    return url
