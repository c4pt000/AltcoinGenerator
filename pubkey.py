#!/usr/bin/env python3

import argparse
from blockchain_fundamentals import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate public keys from private key')
    parser.add_argument('privkey', metavar='privkey')
    parser.add_argument('-u', '--uncompressed', action='store_true')
    args = parser.parse_args()

    if args.uncompressed:
        key = ToPublicKey(args.privkey)
    else:
        uncompressedKey = ToPublicKey(args.privkey)
        key = ToCompressedKey(uncompressedKey)

    print(key)
