#!/usr/bin/env python3
import sys

if len(sys.argv) < 1:
    print ("Usage: $ reverse_endian <input-hex>")

line = sys.argv[1]

n = 2
orig_list = [line[i:i+n] for i in range(0, len(line), n)]
reversed_list = orig_list[::-1]
reversed = ''.join(reversed_list)

print (reversed)
