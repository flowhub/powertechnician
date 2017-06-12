#!/usr/bin/env python2

import msgflo
import sys
from random import *

class Forecast(msgflo.Participant):
  def __init__(self, role):
    d = {
      'component': 'powertechnician/Forecast',
      'label': 'Generate a forecast for a weather report',
      'icon': 'bolt',
      'inports': [
        { 'id': 'in', 'type': 'array' },
      ],
      'outports': [
        { 'id': 'out', 'type': 'array' },
      ],
    }
    msgflo.Participant.__init__(self, d, role)

  def process(self, inport, msg):
    output = []
    for station in msg.data:
        forecast = station.copy()
        # TODO: Plug in real forecast
        forecast['data'] = random()
        forecast['icao'] = station['station']
        output.append(forecast)

    self.send('out', output)
    self.ack(msg)

if __name__ == '__main__':
  role = sys.argv[1] if len(sys.argv) > 1 else 'Forecast'
  msgflo.main(Forecast, role)
