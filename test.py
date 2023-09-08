from raw_parsers.AdPropertiesParser import *
from raw_parsers.ModeratorPropertiesParser import *
from algorithms.estimators.RevenueRiskBasedValueEstimator import *
from algorithms.allocators.GreedyAllocator import *
from data_builders.AdvertisementStreamBuilder import *
from data_builders.ModeratorListBuilder import *
from managers.AdvertisementManager import *
from managers.ModeratorManager import *
from simulation import *


def simple_test():
  # data from excel, normal distribution in ads stream, greedy allocator
  ad_stream_builder = AdvertisementStreamBuilder(AdPropertiesParser(), RevenueRiskBasedValueEstimator())
  mod_list_builder = ModeratorListBuilder(ModeratorPropertiesParser())
  ad_manager = AdvertisementManager(ad_stream_builder.build_normal_distribution_stream(100, 100))
  mod_manager = ModeratorManager(mod_list_builder.build_random(20))
  print(simulate(ad_manager, mod_manager, GreedyAllocator()))
  
simple_test()