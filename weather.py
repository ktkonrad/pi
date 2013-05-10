"""
mess around with the Wunderground API
"""

__author__ = 'Kyle Konrad'

import sys
import wunderground

from tts import say

if __name__ == '__main__':
  try:
    action = sys.argv[1]
  except IndexError:
    action = 'forecast'

  if action == 'forecast':
    forecast = wunderground.forecast('San Francisco', 'CA')['forecast']
    say('The forecast for today is ' + 
        forecast['txt_forecast']['forecastday'][0]['fcttext'])
  elif action == 'current':
    current = wunderground.conditions('San Francisco', 'CA')['current_observation']
    say("It is %.1f degrees Fairenheit. That's %.1f Celcius, Pete" % (current['temp_f'], current['temp_c']))
  else:
    say("I don't know how to tell you about " + action)

