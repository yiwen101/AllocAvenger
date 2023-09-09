from raw_parsers.AdPropertiesParser import *
from raw_parsers.ModeratorPropertiesParser import *
from algorithms.estimators.RevenueRiskBasedValueEstimator import *
from algorithms.allocators.GreedyAllocator import *
from algorithms.allocators.GreedyIdleOnlyAllocator import *
from algorithms.allocators.RandomAllocator import *
from data_builders.AdvertisementPropertiesProducer import *
from data_builders.ModeratorPropertiesProducer import *
from data_builders.AdvertisementStreamBuilder import *
from data_builders.ModeratorListBuilder import *
from managers.AdvertisementManager import *
from managers.ModeratorManager import *
from simulation import *
from algorithms.estimators.AccuracyEstimator import *
from algorithms.estimators.RiskEstimator import *
from algorithms.estimators.RevenueEstimator import *
from algorithms.estimators.DurationEstimator import *
from algorithms.estimators.RevenueRiskBasedValueEstimator import *
from algorithms.estimators.ModeratorUnitTimeValueEstimator import *
import argparse

def main():
    parser = argparse.ArgumentParser(description="Options of input advertisement stream")
    parser.add_argument("-d", "--distribution", type=str, help="even | uneven", default="even")
    parser.add_argument("-v", "--volume", type=float, help="advertisement volume (ratio to the original)", default=1)
    parser.add_argument("-p", "--punishment_factor", type=float, help="ratio of punishment for an erroneously acceptted ad", default=2)
    parser.add_argument("-s", "--source", type=str, help="source of advertisement data: raw | synthetic", default="raw")
    parser.add_argument("-a", "--algorithm", type=str, help="algorithm: random | greedy_idle | greedy", default="greedy")

    args = parser.parse_args()
    print(f"Advertisement stream ditribution: {args.distribution}")
    print(f"Advertisement stream volume: {args.volume}")
    print(f"Writing results to the file...")
    ads_producer = AdPropertiesParser()
    mods_producer = ModeratorPropertiesParser()
    if args.source == "synthetic":
      ads_producer = AdvertisementPropertiesProducer()
      mods_producer = ModeratorPropertiesProducer()
    ads_volume = int(10000 * args.volume)
    ad_stream_builder = AdvertisementStreamBuilder(ads_producer, RevenueRiskBasedValueEstimator(RevenueEstimator(), RiskEstimator(), args.punishment_factor))
    mod_list_builder = ModeratorListBuilder(mods_producer)
    stream = ad_stream_builder.build_even_distribution_stream(ads_volume, 1440)
    if args.distribution == "uneven":
      stream = ad_stream_builder.build_uneven_distribution_stream(ads_volume, 1440)
    ad_manager = AdvertisementManager(stream)
    mod_manager = ModeratorManager(mod_list_builder.build_random(350))
    matchEstimator = ModeratorUnitTimeValueEstimator(DurationEstimator(), AccuracyEstimator(), args.punishment_factor)
    allocator = GreedyAllocator(matchEstimator)
    if args.algorithm == "random":
      allocator = RandomAllocator(matchEstimator)
    elif args.algorithm == "greedy_idle":
      allocator = GreedyIdleOnlyAllocator(matchEstimator)
    results = simulateExtended(ad_manager, mod_manager, allocator)
    
    results_dir = 'simulation_results'
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    file_path = os.path.join(results_dir, args.algorithm + '.json')

    with open(file_path, 'w') as f:
        json.dump(results, f)

    print(f"Results saved to {file_path}")

if __name__ == "__main__":
    main()
