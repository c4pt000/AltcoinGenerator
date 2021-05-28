Coin Distribution
Max supply
Let’s make the max supply a more round number, instead of 21M coins, let’s do 10M for the sake of learning. There is no fixed max supply parameter that we can easily change. This is because of the distribution algorithm of Bitcoin. The total supply of bitcoin is designed to level off just below 21M coins, but the parameters that determine this are the block subsidy (miner reward) and the block halving interval. How long it takes to level off to the max supply is determined by the block time.
Bitcoin parameters:
Initial block subsidy: 50BTC
Block halving interval: 210,000 (blocks)
Let’s do some quick math. If we want our max supply to be 10M coins, we could just change the initial mining subsidy. In order to find out what it will need to be, we can use this script:
$ distribution -m 10000000
Assumptions
===================
Target Max Time (months): 48
Halving Interval (blocks): 210000
Results
===================
Block Time (sec): 600
Initial Subsidy: 23.809523809523807
Halving Interval (blocks): 210000
Target Max Time (months): 48
Max Supply: 10000000
If we only provide the max supply parameter, the tool assumes default target max time and halving interval. If we make the initial subsidy equal to or above 23.81, we can be sure the max supply will never be greater than 10M Forkcoin. We’re going to make a few more changes first before we edit the code.
Block rewards
Let’s say we want the block rewards to be an even number, one that will be easy to remember, and easy to calculate in the future (after halvings). Let’s go with 100 coins, and update our calculation:
$ distribution -m 10000000 -s 100
Results
===================
Block Time (sec): 600
Initial Subsidy: 100
Halving Interval (blocks): 50051.379461857425
Target Max Time (months): 48
Max Supply: 10000000
Then, we update this parameter in src/validation.cpp:
// Line 1169:
CAmount nSubsidy = 100 * COIN;
Subsidy halving interval
Now we have a subsidy halving interval of 50,050. This means after every time 50,050 blocks are mined, the block reward will be cut in half. Let’s update this parameter in src/chainparams.cpp:
// Mainnet: Line 77
consensus.nSubsidyHalvingInterval = 50050;
// Testnet: Line 191
consensus.nSubsidyHalvingInterval = 50050;
For regtest, we will just leave it at 150.
