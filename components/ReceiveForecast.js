var noflo = require('noflo');

exports.getComponent = function() {
  var c = new noflo.Component();
  c.description = 'Receive Forecast results';
  c.icon = 'forward';
  c.inPorts.add('stations', {
    datatype: 'bang'
  });
  c.inPorts.add('in', {
    datatype: 'array'
  });
  c.outPorts.add('out', {
    datatype: 'array'
  });
  c.outPorts.add('received', {
    datatype: 'array'
  });
  c.forecastScopes = [];
  c.tearDown = function (callback) {
    c.forecastScopes = [];
    callback();
  };
  c.forwardBrackets = {
    in: ['received']
  };
  c.process(function (input, output) {
    if (input.hasData('stations')) {
      // We need the request scope
      input.getData('stations');
      c.forecastScopes.push(input.scope);
      return output.done();
    }
    if (!input.hasStream('in')) {
      return;
    }
    var data = input.getData('in');
    output.send({
      out: new noflo.IP('data', data, {
        scope: c.forecastScopes.shift()
      })
    });
    output.send({
      received: data
    });
    output.done();
    
  });
  return c;
};
