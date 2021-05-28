#!/usr/bin/env python3

import argparse

def calculateBlockRewards(blocks, subsidy):
    block_rewards = []
    for i, block in enumerate(blocks):
        if len(block_rewards) == 0:
            block_rewards.append(subsidy)
        else:
            block_rewards.append(block_rewards[i-1]/2)
    return block_rewards

def simulateDistribution(halvingIntervalBlocks, subsidy, maxSupply, simulationRounds):
    altcoinCoinCount = 0
    initialHalvingInterval = 210000
    premine = 0 # TODO: add this to the parameters
    blocks = range(0, int(halvingIntervalBlocks) * simulationRounds, int(halvingIntervalBlocks))
    block_rewards = calculateBlockRewards(blocks, subsidy)
    for i, block in enumerate(blocks):
        if altcoinCoinCount == 0 and premine != 0:
            altcoinCoinCount += premine
        else:
            altcoinCoinCount += block_rewards[i-1] * float(halvingIntervalBlocks)
    return altcoinCoinCount

def findHalvingInterval(halvingIntervalBlocks, subsidy, maxSupply):
    error = 10
    while (abs(error) > .001):
        altcoinCoinCount = simulateDistribution(halvingIntervalBlocks, subsidy, maxSupply, 15)
        error = (float(maxSupply) - float(altcoinCoinCount)) / float(maxSupply)
        if (error > 0):
            halvingIntervalBlocks = halvingIntervalBlocks + (error * subsidy)
        if (error < 0):
            halvingIntervalBlocks = halvingIntervalBlocks + (error * subsidy)
    return halvingIntervalBlocks 

if __name__ == '__main__':

    def setupParameters():
        nondefaultArgs = []
        if args.bts != 10 * 60:
            nondefaultArgs.append('bts') 
        if args.subsidy != 50:
            nondefaultArgs.append('subsidy')
        if args.halving != 210000:
            nondefaultArgs.append('halving')
        if args.ttm != 4*12:
            nondefaultArgs.append('ttm')
        if args.max != 21000000:
            nondefaultArgs.append('max')

        return nondefaultArgs

    def calculateParameters(nondefaultArgs):
        if len(nondefaultArgs) == 1:
            if nondefaultArgs[0] == 'max':
                # solve for subsidy
                args.subsidy = (float(args.max) / 21000000) * args.subsidy 
            # TODO: finish other possibilities
                
        if len(nondefaultArgs) == 2:
            if 'max' in nondefaultArgs and 'subsidy' in nondefaultArgs:
                # solve for halving interval
                args.halving = findHalvingInterval(int(args.halving), float(args.subsidy), float(args.max))
            # TODO: finish other possibilities

        if len(nondefaultArgs) == 3:
            # TODO: finish other possibilities
            print('coming soon')

        if len(nondefaultArgs) == 4:
            # TODO: finish other possibilities
            print('coming soon')

    parser = argparse.ArgumentParser(description='Determine distribution paramters for a given target')
    parser.add_argument('-b', '--block_time_secs', dest='bts', default=10*60)
    parser.add_argument('-s', '--init_subsidy_coins', dest='subsidy', default=50)
    parser.add_argument('-i', '--halving_interval_blocks', dest='halving', default=210000)
    parser.add_argument('-t', '--target_time_months', dest='ttm', default=4*12)
    parser.add_argument('-m', '--max_supply', dest='max', default=21000000)
    args = parser.parse_args()

    # determine which parameter is nonzero
    nondefaultArgs = setupParameters()

    if len(nondefaultArgs) == 0:
        print('You must supply at least one target parameter')
        parser.print_help()

    if len(nondefaultArgs) > 3:
        print('Looks like you have all the information you need!')
        parser.print_help()

    # Only one parameter is given
    if len(nondefaultArgs) == 1:
        if nondefaultArgs[0] == 'bts':
            args.subsidy

    calculateParameters(nondefaultArgs)

    print('Results', '===================', sep='\n')
    print('Block Time (sec):', args.bts)
    print('Initial Subsidy:', args.subsidy)
    print('Halving Interval (blocks):', args.halving)
    # print('Target Max Time (months):', args.ttm) # not implemented yet
    print('Max Supply:', args.max)
