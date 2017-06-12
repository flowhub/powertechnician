var noflo = require('noflo');

exports.getComponent = function() {
  var c = new noflo.Component();
  c.description = 'Serve a list of weather stations';
  c.icon = 'plane';
  c.inPorts.add('req', {
    datatype: 'object',
    description: 'Request'
  });
  c.process(function (input, output) {
    if (!input.hasData('req')) {
      return;
    }
    var req = input.getData('req');
    var stations = require('../stations.json');
    req.res.json(stations);
    output.done();
  });
  return c;
};
