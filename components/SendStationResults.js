var noflo = require('noflo');

exports.getComponent = function() {
  var c = new noflo.Component();
  c.description = '';
  c.icon = 'forward';
  c.inPorts.add('req', {
    datatype: 'object'
  });
  c.inPorts.add('stations', {
    datatype: 'array'
  });
  c.inPorts.add('data', {
    datatype: 'array'
  });
  c.process(function (input, output) {
    if (!input.hasData('req', 'stations', 'data')) {
      return;
    }
    var req = input.getData('req');
    var stations = input.getData('stations');
    var data = input.getData('data').map(function (d, idx) {
      var station = stations[idx];
      return {
        lat: station.lat,
        lon: station.lon,
        data: parseFloat(d.forecast)
      };
    });
	req.res.json(data);
    output.done();
  });
  return c;
};
