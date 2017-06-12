var noflo = require('noflo');

exports.getComponent = function() {
  var c = new noflo.Component();
  c.description = 'Collect station information';
  c.icon = 'forward';
  c.inPorts.add('stations', {
    datatype: 'all',
  });
  c.inPorts.add('forecast', {
    datatype: 'all',
  });
  c.outPorts.add('ready', {
    datatype: 'array'
  });
  c.outPorts.add('stations', {
    datatype: 'array'
  });
  c.forwardBrackets = {};
  c.process(function (input, output) {
    if (!input.hasData('stations', 'forecast')) {
      return false;
    }
    var forecast = input.getData('forecast');
    var stations = input.getData('stations');
    stations = stations.map(function (station) {
      if (station.icao !== forecast.icao) {
        return;
      }
      station.forecast = forecast.data;
    });
    var missing = stations.filter(function (station) {
      if (station.forecast) {
        return false;
      }
      return true;
    });
    if (missing.length) {
      output.sendDone({
        stations: stations
      });
      return;
    }
    output.sendDone({
      ready: stations
    });
  });
  return c;
};
