var noflo = require('noflo');

exports.getComponent = function() {
  var c = new noflo.Component();
  c.description = 'Get stations for request';
  c.icon = 'forward';
  c.inPorts.add('req', {
    datatype: 'object',
    description: 'Request for stations'
  });
  c.outPorts.add('req', {
    datatype: 'object'
  });
  c.outPorts.add('stations', {
    datatype: 'object'
  });
  c.process(function (input, output) {
    if (!input.hasData('req')) {
      return;
    }
    var req = input.getData('req');
    var stations = require('../stations.json');
    output.send({
      req: req
    });
    output.send({
      stations: stations
    });
    output.done();
  });
  return c;
};
