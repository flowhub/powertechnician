var noflo = require('noflo');

exports.getComponent = function() {
  var c = new noflo.Component();
  c.description = 'Receive Forecast results';
  c.icon = 'forward';
  c.inPorts.add('stations', {
    datatype: 'object'
  });
  c.inPorts.add('in', {
    datatype: 'array'
  });
  c.outPorts.add('out', {
    datatype: 'array'
  });
  c.process(function (input, output) {
    console.log(input.scope, input.hasData('stations'), input.hasData('in'));
    if (!input.hasData('stations')) {
      return;
    }
    output.done();
    
  });
  return c;
};
