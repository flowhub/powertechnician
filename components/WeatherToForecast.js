var noflo = require('noflo');

exports.getComponent = function() {
  var c = new noflo.Component();
  c.description = 'Converts the weather data to Python command';
  c.icon = 'filter';
  c.inPorts.add('in', {
    datatype: 'object',
    description: 'Packet to forward'
  });
  c.outPorts.add('out', {
    datatype: 'string'
  });
  c.process(function (input, output) {
    if (!input.hasData('in')) {
      return;
    }
    var data = input.getData('in');
    var string = "python2 python/calculate.py " + data.ob;
    // Process data and send output
    output.send({
      out: string
    });
    // Deactivate
    output.done();
  });
  return c;
};
