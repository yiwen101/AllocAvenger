import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from entities.Moderator import Moderator
from data_builders.ModeratorPropertiesProducer import *
from raw_parsers.ModeratorPropertiesParser import *
from typing import Union

class ModeratorListBuilder:
  def __init__(self, data_producer: Union[ModeratorPropertiesProducer, ModeratorPropertiesParser]):
    self.producer = data_producer
    
  def build_random(self, num):
    mods_dic = self.producer.generate_data(num)
    mods = list(map(lambda x: Moderator(x), mods_dic))
    return mods
  

# st = ModeratorListBuilder(ModeratorProducer())
# print(st.build_random(10))