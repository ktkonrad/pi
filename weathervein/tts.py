"""
Text to speech

requires festival
"""

__author__ = 'Kyle Konrad'

from subprocess import Popen, PIPE

def say(text):
  """a hacky way to do text to speech"""
  p = Popen(['festival', '--tts'], stdin=PIPE)
  p.communicate(text)
  p.wait()
