from raw_parsers.AdPropertiesParser import *
from raw_parsers.ModeratorPropertiesParser import *
from algorithms.estimators.RevenueRiskBasedValueEstimator import *
from algorithms.allocators.GreedyAllocator import *
from algorithms.allocators.GreedyIdleOnlyAllocator import *
from algorithms.allocators.RandomAllocator import *
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
import os


def quick_start():
  # data from excel, normal distribution in ads stream, greedy allocator
    accuracyEstimator = AccuracyEstimator()
    riskEstimator = RiskEstimator()
    revenueEstimator = RevenueEstimator()
    durationEstimator = DurationEstimator()
    punishingFactor = 2
    ad_stream_builder = AdvertisementStreamBuilder(AdPropertiesParser(), RevenueRiskBasedValueEstimator(revenueEstimator, riskEstimator, punishingFactor))
    mod_list_builder = ModeratorListBuilder(ModeratorPropertiesParser())
    ad_manager = AdvertisementManager(ad_stream_builder.build_normal_distribution_stream(10000, 250))
    mod_manager = ModeratorManager(mod_list_builder.build_random(350))
    matchEstimator = ModeratorUnitTimeValueEstimator(durationEstimator, accuracyEstimator, punishingFactor)
    results = simulateExtended(ad_manager, mod_manager, RandomAllocator(matchEstimator))
    results = simulateExtended(ad_manager, mod_manager, RandomAllocator(matchEstimator))

    # Directory where you want to save the results
    results_dir = 'simulation_results'
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # File path to save the results
    file_path = os.path.join(results_dir, 'results.json')

    # Save the results to a JSON file
    with open(file_path, 'w') as f:
        json.dump(results, f)

    print(f"Results saved to {file_path}")

quick_start()
