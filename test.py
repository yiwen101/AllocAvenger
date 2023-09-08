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


def simple_test():
  # data from excel, normal distribution in ads stream, greedy allocator
  accuracyEstimator = AccuracyEstimator()
  riskEstimator = RiskEstimator()
  revenueEstimator = RevenueEstimator()
  durationEstimator = DurationEstimator()
  punishingFactor = 2
  ad_stream_builder = AdvertisementStreamBuilder(AdPropertiesParser(), RevenueRiskBasedValueEstimator(revenueEstimator, riskEstimator, punishingFactor))
  mod_list_builder = ModeratorListBuilder(ModeratorPropertiesParser())
  ad_manager = AdvertisementManager(ad_stream_builder.build_normal_distribution_stream(100, 10))
  mod_manager = ModeratorManager(mod_list_builder.build_random(10))
  matchEstimator = ModeratorUnitTimeValueEstimator(durationEstimator, accuracyEstimator, punishingFactor)
  print(simulate(ad_manager, mod_manager, GreedyIdleOnlyAllocator(matchEstimator)))

  
simple_test()