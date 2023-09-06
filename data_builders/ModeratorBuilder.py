import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from objects.Moderator import Moderator
from ModeratorProducer import *

class ModeratorListBuilder:
  def __init__(self, producer: ModeratorProducer):
    self.producer = producer
    
  def build_random(self, num):
    pd_mods = self.producer.generate_data(num)
    dic_list = pd_mods.to_dict(orient='records')
    mod_list = list(map(lambda x: Moderator(x), dic_list))
    return mod_list
  

st = ModeratorListBuilder(ModeratorProducer())
st.build_random(10)