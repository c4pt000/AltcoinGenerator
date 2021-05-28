import hashlib
import decode
import sys

sys.path.append('/opt/')



#A block header contains these fields: Version, hashPrevBlock, hashMerkleRoot, Time, Bits, Nonce.
header_hex = ("01000000" +
  "e4ee5e60b73b8f5bd86a94244198a32e62b9872c61348e45f7a7f0f0ac1bd073" +
  "61767dc007a58088c7762bf9aa9f13207dba85fef6af3c5bfa8af324121ad950" +
  "60af1bda" +
  "3b9aca00" +
  "504365040")

header_bin = header_hex.decode("utf-8")

#hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
#hash.encode('hex_codec')
#'60ce4639bf63532b27e8f8b036b9846f5d2ae18556289f80e38b85a5df4910e1'

#hash[::-1].encode('hex_codec')
#'e11049dfa5858be3809f285685e12a5d6f84b936b0f8e8272b5363bf3946ce60'
