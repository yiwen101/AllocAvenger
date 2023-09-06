import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from objects.Advertisement import Advertisement
from AdvertisementProducer import *
import random

class AdvertisementStreamBuilder:
  def __init__(self, producer: AdvertisementProducer, estimator):
    self.producer = producer
    self.estimator = estimator
    
  def get_ads_list(self, num):
    pd_ads = self.producer.generate_data(num)
    dic_list = pd_ads.to_dict(orient='records')
    ads_list = list(map(lambda x: Advertisement(x, self.estimator), dic_list))
    return ads_list
  
  def build_normal_distribution_stream(self, num_ads, num_time_steps):
    ads_list = self.get_ads_list(num_ads)
    ads_stream = []
    for t in range(num_time_steps):
        mean = num_ads / num_time_steps
        std_dev = mean / 5
        num = int(np.random.normal(mean, std_dev))
        num = max(0, min(num, len(ads_list)))
        print(num)
        selected_objects = random.sample(ads_list, num)
        ads_stream.append(selected_objects)
    return ads_stream
  
  def build_exponential_distribution_stream(self, num_ads, num_time_steps):
    ads_list = self.get_ads_list(num_ads)
    ads_stream = []
    nums = np.random.exponential(2, num_time_steps)
    actual_sum = np.sum(nums)
    scaled_nums = (nums / actual_sum) * num_ads
    for t in range(num_time_steps):
        num = max(0, min(int(scaled_nums[t]), len(ads_list)))
        selected_objects = random.sample(ads_list, num)
        ads_stream.append(selected_objects)
    return ads_stream


