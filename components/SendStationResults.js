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
    datatype: 'number'
  });
  c.process(function (input, output) {
    if (!input.hasData('req', 'stations')) {
      return;
    }
    if (!input.hasStream('data')) {
      return;
    }
    var req = input.getData('req');
    var stations = input.getData('stations');
    var data = input.getStream('data').filter(function (ip) {
      if (ip.type != 'data') {
        return false;
      }
      return true;
    }).map(function (ip, idx) {
      var station = stations[idx];
      return {
        lat: station.lat,
        lon: station.lon,
        data: parseFloat(ip.data)
      };
    });
	req.res.json(data);
    output.done();
  });
  return c;
};
