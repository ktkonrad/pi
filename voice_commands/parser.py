from weathervein import weather
from weathervein.tts import say


def parse(instruction):
  instruction = instruction.lower()
  if instruction.split()[0] == 'what\'s' or instruction.split()[0] == 'whats' or instruction.split()[0] == 'what':
    if 'weather' in instruction.split():
      return weather.say_current
    elif 'forecast' in instruction.split():
      return weather.say_forecast
  elif instruction == 'close the pod bay doors hal':
    return lambda: say('Im sorry dave, im affraid i cant do that')
  return lambda: say('I dont know what that means yet')
