#!/usr/bin/env python2

import msgflo
from random import *
import sys
sys.path.append('../')
from forecast import predict_consumption
import datetime

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
        dof = datetime.datetime.today().weekday()
        hour = datetime.datetime.today().hour
        # predict_consumption (wdsp,temp,rhum,date_day_code,hour)
        value = predict_consumption(station['wind']['speed'],station['temperature'],78.666667,dof,hour)
        print station
        print value
        forecast['forecast'] = value
        forecast['icao'] = station['station']
        output.append(forecast)

    self.send('out', output)
    self.ack(msg)

if __name__ == '__main__':
  role = sys.argv[1] if len(sys.argv) > 1 else 'Forecast'
  msgflo.main(Forecast, role)
