"""
Wunderground API wrapper
"""

import requests
import os
filename = os.path.join(os.path.dirname(__file__), 'wunderground.cfg')
# read key from config file
with open(filename) as f:
  _KEY = f.readline()

# the endpoint format for all weather features
_ENDPOINT = 'http://api.wunderground.com/api/%s/%%(feature)s/q/%%(state)s/%%(city)s.json' % _KEY

def _feature(feature):
  """
  returns a function to make an API call for the given feature
  """
  def get_feature(city, state):
    url = _ENDPOINT % {'feature': feature, 'state': state.upper(), 'city': city.replace(' ', '_')}
    res = requests.get(url)
    # TODO: error handling
    return res.json()
  return get_feature

# create module level functions for the following features
for feature in """
conditions
forecast
""".split():
  globals()[feature] = _feature(feature)
