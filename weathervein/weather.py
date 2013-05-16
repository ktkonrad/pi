"""
mess around with the Wunderground API
"""

__author__ = 'Kyle Konrad'

import sys
import wunderground

from tts import say


def say_forecast():
  forecast = wunderground.forecast('San Francisco', 'CA')['forecast']
  say('The forecast for today is ' +
      forecast['txt_forecast']['forecastday'][0]['fcttext'])


def say_current():
  current = wunderground.conditions('San Francisco', 'CA')['current_observation']
  say("It is %.1f degrees Fairenheit. That's %.1f sell sea us, Pete" % (current['temp_f'], current['temp_c']))

if __name__ == '__main__':
  try:
    action = sys.argv[1]
  except IndexError:
    action = 'forecast'

  if action == 'forecast':
    say_forecast()
  elif action == 'current':
    say_current()
  else:
    say("I don't know how to tell you about " + action)
