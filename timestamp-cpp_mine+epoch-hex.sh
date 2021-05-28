#!/bin/bash


#echo 'cpp_miner mine  <version 4B-hex> <hashPrevBlock 32B-hex> <merkleRoot 32B-hex> <time 4B-hex> <nBits 4B-hex> <nonce 4B-hex>'

#echo 'version 0x01'
#printf '0x%x \n' 01000000

#echo 'version 0x02'
#printf '0x%x \n' 02000000




echo 'cpp_miner genesisgen <pubkey 65B-hex> "<coinbase-message 91B-string>" <value 8B-decimal> <time 4B-hex> <nBits 4B-hex> <nonce 4B-hex>'

echo 'pubkey 0x04770ee175cb5530e95cd615c061738719116d871ad9fcc9292ea6b0d396f7d270c12f351ff674b030299b537e9fa062511ac67b8bfc4d68cfcc2fd86158e0e6b3'

echo 'cpp_miner genesisgen 04770ee175cb5530e95cd615c061738719116d871ad9fcc9292ea6b0d396f7d270c12f351ff674b030299b537e9fa062511ac67b8bfc4d68cfcc2fd86158e0e6b3 "RadioCoin music wallet" 50 60b0604c 3b9aca00 1e197848 '


printf 'time in hex \n'
printf '0x%x \n' 1622171724 
printf 'value in hex \n'
printf '0x%x \n' 1000000000 
printf 'nonce in hex \n'
printf '0x%x \n' 504985672
