requires Fedora34/RHEL/CentOS variant

```
./src/radiocoind | grep _ > file.txt && cat file.txt | tail -n 12 > network-hash-assert-replacement.txt && cat network-hash-assert-replacement.txt

assert replacement, main, test, reg
rebuild
make -j24 clean
make -j24
mine block0,block1 cpp_miner
```
 
https://medium.com/@jordan.baczuk/how-to-fork-bitcoin-part-2-59b9eddb49a4

https://jbaczuk.github.io/blockchain_fundamentals/3-Development/3.2-Design.html

https://bitcoin.stackexchange.com/questions/80810/error-acceptblock-high-hash-proof-of-work-failed-code-16

# **WIP (Experimental roll your own currency)  REQUIRES docker-ce

docker install fedora-34
```
sudo dnf -y install dnf-plugins-core
 sudo dnf config-manager \
    --add-repo \
    https://download.docker.com/linux/fedora/docker-ce.repo
    
sudo dnf install docker-ce docker-ce-cli containerd.io
```
git clone https://github.com/c4pt000/docker-BLOCKCHAIN-GENERATOR
<br>
cd docker-BLOCKCHAIN-GENERATOR
<br>
```
./sha256.py "your unique PSZ phrase here" 

./pubkey -u uyb3yb14u51kyoui84o0m25 <-generate MAIN_PUB_KEY 
```
cd ..
<br>
yum install nano -y
<br>
* edit script with PUBKEY from pubkey -u output
* edit script with unique psz phrase  "your unique PSZ phrase here" from sha256.py creation of phrase hash
<br>
nano altcoin_generator.sh
<br>
sh altcoin_generator.sh start
<br>
<br>

# build on host
```
yum groupinstall "C Development Tools and Libraries" -y
yum install git-core libdb-cxx-devel libdb-cxx openssl-devel libevent-devel \
cppzmq-devel qrencode-devel protobuf-devel cargo boost* boost-devel miniupnpc-devel.x86_64 qt-devel qt4-devel -y

change to "yourcoin" to build on host

sh autogen.sh 
./configure --enable-sse2 --with-incompatible-bdb --prefix=/usr --disable-tests --disable-bench
make -j24 clean
make -j24 
./src/qt/yourcoin-qt
 
or make -j24 install       -> for direct install to /usr
yourcoin-qt


make -j24 clean      (to clean project)
make -j24            (to build project)
make -j24 install    (to reinstall to system path /usr)

```
<br>
creating nodes
<br>
https://medium.com/@kay.odenthal_25114/create-a-private-bitcoin-network-with-simulated-mining-b35f5b03e534


# requires mining the first block
<br>
https://bitcoin.stackexchange.com/questions/80810/error-acceptblock-high-hash-proof-of-work-failed-code-16


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

* 05-21-2021
<br>
to do fix automatic assertion point for block 0 for script to auto inject values,

```
 chainparams.cpp:119: CMainParams::CMainParams(): Assertion `consensus.hashGenesisBlock == uint256S("0x829661f4166c0a5da89f184b0ca0c6769db139a04a94fbe001da656c1fa16ffd")' failed.
/bin/bash: line 1:     7 Aborted                 ./src/coind -listen -noconnect -bind=172.18.0.4 -addnode=172.18.0.1 -addnode=172.18.0.2 -addnode=172.18.0.3 -addnode=172.18.0.5
```

```
wget https://raw.githubusercontent.com/c4pt000/AlternativeCryptoCurrencyBuilder/master/altcoin_generator.sh
```

build in host directly after build 
```
yum groupinstall "C Development Tools and Libraries" -y
yum install git-core libdb-cxx-devel libdb-cxx libdb-cxx-devel openssl-devel libevent-devel cppzmq-devel qrencode-devel qt5-qtbase-devel protobuf-devel cargo boost-devel miniupnpc-devel diffutils qt-devel qt4-devel wget miniupnpc-devel zeromq-devel boost* qt4-* -y

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

# edit script 
```
nano altcoin_generator.sh 

./sha256.py "your unique PSZ phrase here"
uyb3yb14u51kybjnob3l79c8zoui84o0m25uyb3yb14u51k         <- where this is the return to generate PUBKEY

./pubkey -u uyb3yb14u51kybjnob3l79c8zoui84o0m25  <-generate MAIN_PUB_KEY
uyb3yb14u51kybjnob3l79c8zoui84o0m25-pubkey-return-longuyb3yb14u51kybjnob3l79c8zoui84o0m25-pubkey-return-long

edit these lines in the script to your pubkey

https://github.com/c4pt000/AltcoinGenerator/edit/master/altcoin_generator.sh

GENESIS_REWARD_PUBKEY=uyb3yb14u51kybjnob3l79c8zoui84o0m25-pubkey-return-longuyb3yb14u51kybjnob3l79c8zoui84o0m25-pubkey-return-long
LITECOIN_PUB_KEY=uyb3yb14u51kybjnob3l79c8zoui84o0m25-pubkey-return-longuyb3yb14u51kybjnob3l79c8zoui84o0m25-pubkey-return-long
```



for "scrypt type coin nBit type 1e0ffff0
------------------
```
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


<br>
<br>
<br>
if you found this useful
<br>
1MxdqrDRu97BNG9n17e8jejBwAUUxRCLhy
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# Altcoin Generator

# an improvement to a pre-existing tool to help designers trying to establish their own cryptocurrency 


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

Yes. one day cryptocurrencies might become worthless from misuse and greed and ripping off developers even when they attempt to do legitimate business and corporations will crumble also from being greedy and ugly and pushing around even legitmate business people in terms of personal snobbyness or as a form of financial control from companies pushing people around with racist employees where companies cant always control their employees like a nutcase dog owner with too many dogs in its yard with rabbies,and the atomsphere will also break and cook and smash those corporate buildings like melting ice on the surface of mercury since nothing is truly indestructible since everything known to exist started as a giant explosion 

  * This is a very simple script to help you bootstrap. More changes will be needed to launch a cryptocurrency for real.
  * You have to manually change the pictures in mycoin/share/pixmaps.
  * You will need change the checkpoints in mycoin/src/chainparams.cpp.
  * Consider adding a seed node and add it to src/chainparams.cpp as well.
    * Currently all seeds are getting disabled.
  * The script connects to the regression test network by default. This is a special network that will let you mine new blocks almost instantly (nice for testing). To launch the nodes in the main network, simply leave the CHAIN variable empty.


