**WIP (Experimental roll your own currency)

wget https://github.com/c4pt000/docker-cryptocurrency-builder-AltcoinGenerator-fedora28-node/blob/master/altcoin_generator.sh
<br>
<br>
<br>
build in host directly after build 
```
yum groupinstall "C Development Tools and Libraries" -y
yum install git-core libdb-cxx-devel libdb-cxx libdb-cxx-devel openssl-devel libevent-devel cppzmq-devel qrencode-devel qt5-qtbase-devel protobuf-devel cargo boost-devel miniupnpc-devel diffutils qt-devel qt4-devel wget miniupnpc-devel zeromq-devel boost* qt4-* qt5-* -y

cd -> litecoin (or your coin name dir)

sh autogen.sh 
./configure --enable-sse2 --with-incompatible-bdb --prefix=/usr --disable-tests --disable-bench
make -j24 clean
make -j24

find . -name '*-qt'

./src/qt/litecoin-qt    (or your coin name)

optional make -j24 install -> for direct system path

```

git clone https://github.com/c4pt000/docker-BLOCKCHAIN-GENERATOR

# edit script nano altcoin_generator.sh 



```
./sha256.py "your unique PSZ phrase here"
uyb3yb14u51kybjnob3l79c8zoui84o0m25uyb3yb14u51k         <- where this is the return to generate PUBKEY

./pubkey -u uyb3yb14u51kybjnob3l79c8zoui84o0m25  <-generate MAIN_PUB_KEY
uyb3yb14u51kybjnob3l79c8zoui84o0m25-pubkey-return-longuyb3yb14u51kybjnob3l79c8zoui84o0m25-pubkey-return-long

edit these lines in the script to your pubkey

https://github.com/c4pt000/AltcoinGenerator/edit/master/altcoin_generator.sh

GENESIS_REWARD_PUBKEY=uyb3yb14u51kybjnob3l79c8zoui84o0m25-pubkey-return-longuyb3yb14u51kybjnob3l79c8zoui84o0m25-pubkey-return-long
LITECOIN_PUB_KEY=uyb3yb14u51kybjnob3l79c8zoui84o0m25-pubkey-return-longuyb3yb14u51kybjnob3l79c8zoui84o0m25-pubkey-return-long



date +%s   -> timestamp

for "scrypt type coin nBit type 1e0ffff0
------------------

./generate-genesis -algo scrypt -bits 1e0ffff0 -coins <totalcoinsupply> -psz "your unique PSZ phrase here"" -timestamp 1620011758 -pubkey uyb3yb14u51kybjnob3l79c8zoui84o0m25-pubkey-return-longuyb3yb14u51kybjnob3l79c8zoui84o0m25-pubkey-return-long -threads 24



block hash becomes 
LITECOIN_MAIN_GENESIS_HASH=main-hash-here
merkle hash becomes
LITECOIN_MERKLE_HASH=merkle-hash-here
```

sh altcoin_generator.sh start         to build



<br>
<br>
<br>
<br>
<br>
<br>
<br>

# artwork for projects lives in /src/qt/res/icons
via GIMP editing,
```
artwork for projects lives in /src/qt/res/icons
via GIMP editing,
src/init.cpp holds author info in about license;
```

# Altcoin Generator
Easiest way to create your own cryptocurrency.

## What does this script do?

This script is an experiment to generate new cryptocurrencies (altcoins) based on litecoin.
It will help you creating a git repository with minimal required changes to start your new coin and blockchain.

## What do I have to do?

You need to make sure you have at least docker and git installed in any Linux distribution or MacOS.
If you are using MacOS, then you also need to install gnu-sed using 'brew install gnu-sed'

The other requirements will be installed automatically in a docker container by the script.

Simply open the script and edit the first variables to match your coin requirements (total supply, coin unit, coin name, tcp ports..)
Then simply run the script like this:

```
bash altcoin_generator.sh start
```

To see all possible options run the script like this:

```
bash altcoin_generator.sh
```

## What will happen then?

The script will perform a couple of actions:

  * Create a docker image ready to build and run your new coin nodes
  * Clone GenesisH0 and mine the genesis blocks of main, test and regtest networks in the container (this might take a lot of time)
  * Clone litecoin
  * Rename files and replace variables in litecoin code (genesis hashes, merkle tree hashes, tcp ports, coin name, supply...)
  * Build your new coin
  * Run 4 docker nodes with your coin daemon and connect each other.
    * A directory mapped for each node will be created: miner2, miner3, miner4, miner5. They contain data and configuration of each independent node.
  * The GENESIS_REWARD_PUBKEY will be used in the UTXO of the genesis block. If you don't change it to your own before mining the genesis block you are agreeing to pay me the genesis block reward in case your coin succeeds (Thanks! :p)
  
## What can I do next?

You can first check if your nodes are running and then ask them to generate some blocks.
Instructions on how to do it will be printed once the script execution is done.

## Is there anything I must be aware of?

Yes.

  * This is a very simple script to help you bootstrap. More changes will be needed to launch a cryptocurrency for real.
  * You have to manually change the pictures in mycoin/share/pixmaps.
  * You will need change the checkpoints in mycoin/src/chainparams.cpp.
  * Consider adding a seed node and add it to src/chainparams.cpp as well.
    * Currently all seeds are getting disabled.
  * The script connects to the regression test network by default. This is a special network that will let you mine new blocks almost instantly (nice for testing). To launch the nodes in the main network, simply leave the CHAIN variable empty.
  
## I think something went wrong!

Then you can clean up the mess with:

```
bash altcoin_generator.sh clean_up
```

