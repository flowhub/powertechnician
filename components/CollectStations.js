var noflo = require('noflo');

exports.getComponent = function() {
  var c = new noflo.Component();
  c.description = 'Collect packets into an array';
  c.icon = 'forward';
  c.inPorts.add('in', {
    datatype: 'all',
  });
  c.outPorts.add('out', {
    datatype: 'array'
  });
  c.forwardBrackets = {};
  c.process(function (input, output) {
    if (!input.hasStream('in')) {
      return;
    }
    var data = input.getStream('in').filter(function (ip) {
      if (ip.type != 'data') {
        return false;
      }
      return true;
    }).map(function (ip) {
      return ip.data;
    });
    output.sendDone({
      out: data
    });
  });
  return c;
};
