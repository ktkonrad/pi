"""
mess around with the Wunderground API
"""

__author__ = 'Kyle Konrad'

import subprocess
import wunderground

def say(text):
  """a hacky way to do text to speech"""
  subprocess.call('echo "%s" | festival --tts' % text, shell=True)


if __name__ == '__main__':
  forecast = wunderground.forecast('San Francisco', 'CA')['forecast']
  say(forecast['txt_forecast']['forecastday'][0]['fcttext'])


