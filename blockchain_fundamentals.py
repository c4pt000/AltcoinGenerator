import struct
import hashlib
import random
import ecdsa
import codecs
import os

coin = os.environ['COIN']
# Import the coin file
# TODO: Check for file validity (maybe make an interface)
try:
    Coin = __import__(coin, fromlist=['Coin']).Coin()
except ModuleNotFoundError:
    raise ModuleNotFoundError('There is no coin configuration file coins/' + coin)

iseq, bseq, buffer = (
        lambda s: s,
        bytes,
        lambda s: s.buffer,
)

def ToPublicKey(privKey):
    # Error Checking
    if not isHex(privKey):
        raise TypeError('Private Key argument must be valid hex')
    if len(privKey) != 64:
        raise ValueError('Private Key argument must be 32 bytes')

    privateKeyBytes = codecs.decode(privKey, 'hex')
    key = ecdsa.SigningKey.from_string(privateKeyBytes, curve=ecdsa.SECP256k1).verifying_key
    keyBytes = key.to_string()
    keyHex = codecs.encode(keyBytes, 'hex')
    return (bytearray(b'04') + keyHex).decode('utf-8')

def ToCompressedKey(pubKey):
    # Error Checking
    if not isHex(pubKey):
        raise TypeError('Public Key argument must be valid hex')
    if len(pubKey) != 130:
        raise ValueError('Public Key argument must be 65 bytes')
    
    x = pubKey[2:66]
    lastByte = x[-2:]
    lastInt = int(lastByte, 16)
    isOdd = lastInt % 2 != 0

    if isOdd:
        compressedKey = '03' + x
    else:
        compressedKey = '02' + x
    return compressedKey

def ToWIF(privKey, network, compressed=True):
    # Error Checking
    if not isHex(privKey):
        raise TypeError('Private Key argument must be valid hex')
    if len(privKey) != 64:
        raise ValueError('Private Key argument must be 32 bytes')

    if network == 'mainnet':
        if compressed:
            extendedPriv = Coin.wifMainnetPrefix + privKey + Coin.wifCompressedSuffix
        else:
            extendedPriv = Coin.wifMainnetPrefix + privKey
        WIF = base58encode_check(extendedPriv)
    elif network == 'testnet' or network == 'regtest':
        if compressed:
            extendedPriv = Coin.wifTestnetPrefix + privKey + Coin.wifCompressedSuffix
        else:
            extendedPriv = Coin.wifTestnetPrefix + privKey
        WIF = base58encode_check(extendedPriv)
    else:
        raise ValueError('Network must be mainnet, testnet, or regtest')
    return WIF

def ToP2PKH(pubKey, network):
    
    # Error Checking
    if not isHex(pubKey):
        raise TypeError('Public Key argument must be valid hex')
    if len(pubKey) != 66:
        raise ValueError('Public Key argument must be 33 bytes')

    hash = hash160(pubKey).hex()
    if network == 'mainnet':
        extendedHash = Coin.p2pkhMainnetPrefix + hash
        address = base58encode_check(extendedHash)
    elif network == 'testnet' or network == 'regtest':
        extendedHash = Coin.p2pkhTestnetPrefix + hash
        address = base58encode_check(extendedHash)
    else:
        raise ValueError('Network must be mainnet, testnet, or regtest')

    return address

def ToP2SHP2WPKH(pubKey, network):    
    # Error Checking
    if not isHex(pubKey):
        raise TypeError('Public Key argument must be valid hex')
    if len(pubKey) != 66:
        raise ValueError('Public Key argument must be 33 bytes')

    pubkeyHash = hash160(pubKey).hex()
    hash = hash160('0014' + pubkeyHash).hex()
    if network == 'mainnet':
        extendedHash = Coin.p2shMainnetPrefix + hash
        address = base58encode_check(extendedHash)
    elif network == 'testnet' or network == 'regtest':
        extendedHash = Coin.p2shTestnetPrefix + hash
        address = base58encode_check(extendedHash)
    else:
        raise ValueError('Network must be mainnet, testnet, or regtest')

    return address
    
def LE32toBE(value):
    return struct.unpack("<I", struct.pack(">I", value))[0]

def BE256toLE(value):
    valueStr = hex(value)[2:]
    reversedStr = ""
    for i, c in enumerate(valueStr):
        if (i % 2 == 0):
            reversedStr = valueStr[i-1] + c + reversedStr
    return int(reversedStr, 16)

def BitsToTarget(bits):
    bitsInt = int(bits, 16)

    exponent = (bitsInt & 0xff000000) >> 8 * 3
    mantissa = bitsInt & 0x00ffffff

    target = mantissa * 256 ** (exponent - 3)
    return "{0:0{1}x}".format(target, 64)

# TODO:
#def TargetToBits(target):
#    bitsInt = int(bits, 16)
#
#    exponent = (bitsInt & 0xff000000) >> 8 * 3
#    mantissa = bitsInt & 0x00ffffff
#
#    target = mantissa * 256 ** (exponent - 3)
#    return "{0:0{1}x}".format(target, 64)

def ReverseEndian(line):
    n = 2
    orig_list = [line[i:i+n] for i in range(0, len(line), n)]
    reversed_list = orig_list[::-1]
    reversedStr = ''.join(reversed_list)
    return reversedStr

def isHex(value):
    try:
        int(value, 16)
        return True
    except ValueError:
        return False
    except:
        raise

def sha256(value):
    # Assume bytes type
    try:
        return hashlib.sha256(value).digest()
    except TypeError:
        if isHex(value):
            return hashlib.sha256(bytes.fromhex(value)).digest()
        else:
            return hashlib.sha256(value.encode('utf-8')).digest()
    except:
        raise

def hash256(value):
    return sha256(sha256(value))

def ripemd160(value):
    # Assume byte type
    try:
        return hashlib.new('ripemd160', value).digest()
    except TypeError:
        if isHex(value):
            return hashlib.new('ripemd160', bytes.fromhex(value)).digest()
        else:
            return hashlib.new('ripemd160', value.encode('utf-8')).digest()
    except:
        raise

def hash160(value):
    return ripemd160(sha256(value))

def genMsgPrefix():
    networks = ['Mainnet', 'Testnet', 'Regtest']
    for network in networks:
        print(network)
        print("pchMessageStart[0] = ", hex(random.sample(range(0x80, 0xff), 1)[0]), ";", sep='')
        print("pchMessageStart[1] = ", hex(random.sample(range(0x80, 0xff), 1)[0]), ";", sep='')
        print("pchMessageStart[2] = ", hex(random.sample(range(0x80, 0xff), 1)[0]), ";", sep='')
        print("pchMessageStart[3] = ", hex(random.sample(range(0x80, 0xff), 1)[0]), ";", sep='')
        print()

# 58 character alphabet used
alphabet = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
def scrubInput(v):
    if isHex(v):
        v = bytes.fromhex(v)
    elif isinstance(v, str) and not isinstance(v, bytes):
        v = v.encode('utf-8')
    if not isinstance(v, bytes):
        raise TypeError(
            "a bytes-like object is required (also str), not '%s'" %
            type(v).__name__)
    return v

def b58encode_int(i, default_one=True):
    '''Encode an integer using Base58'''
    if not i and default_one:
        return alphabet[0:1]
    string = b""
    while i:
        i, idx = divmod(i, 58)
        string = alphabet[idx:idx+1] + string
    return string

def base58encode(v):
    '''Encode a string using Base58'''
    v = scrubInput(v)
    nPad = len(v)
    v = v.lstrip(b'\0')
    nPad -= len(v)
    p, acc = 1, 0
    for c in iseq(reversed(v)):
        acc += p * c
        p = p << 8
    result = b58encode_int(acc, default_one=False)
    return (alphabet[0:1] * nPad + result)

def b58decode_int(v):
    '''Decode a Base58 encoded string as an integer'''
    decimal = 0
    for char in v:
        decimal = decimal * 58 + alphabet.index(char)
    return decimal


def base58decode(v):
    '''Decode a Base58 encoded string'''
    v = scrubInput(v)
    origlen = len(v)
    v = v.lstrip(alphabet[0:1])
    newlen = len(v)
    acc = b58decode_int(v)
    result = []
    while acc > 0:
        acc, mod = divmod(acc, 256)
        result.append(mod)
    return (b'\0' * (origlen - newlen) + bseq(reversed(result)))

def base58encode_check(v):
    '''Encode a string using Base58 with a 4 character checksum'''
    v = scrubInput(v)
    digest = hash256(v)
    return base58encode(v + digest[:4])

def base58decode_check(v):
    '''Decode and verify the checksum of a Base58 encoded string'''
    v = scrubInput(v)
    result = base58decode(v)
    result, check = result[:-4], result[-4:]
    digest = hash256(result)
    if check != digest[:4]:
        raise ValueError("Invalid checksum")
    return result
