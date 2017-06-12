var noflo = require('noflo');
var express = require('express');

exports.getComponent = function() {
  var c = new noflo.Component();
  c.description = 'Sets up static file serving for Express';
  c.icon = 'file';
  c.inPorts.add('in', {
    datatype: 'object',
    type: 'http://expressjs.com/4x/api.html#app',
    description: 'Express app'
  });
  c.inPorts.add('prefix', {
    datatype: 'string',
    description: 'HTTP path prefix for files to serve',
    default: '/static',
    control: true
  });
  c.inPorts.add('path', {
    datatype: 'string',
    description: 'Path where the files are located',
    default: 'static',
    control: true
  });
  c.outPorts.add('out', {
    datatype: 'object',
    type: 'http://expressjs.com/4x/api.html#app',
  });
  c.process(function (input, output) {
    var path, prefix, app;
    if (!input.hasData('in')) {
      return;
    }
    if (input.attached('path')) {
      if (!input.hasData('path')) {
        return;
      }
      path = input.getData('path');
    } else {
      path = 'static';
    }
    if (input.attached('prefix')) {
      if (!input.hasData('prefix')) {
        return;
      }
      prefix = input.getData('prefix');
    } else {
      prefix = '/static';
    }
    app = input.getData('in');
    app.use(prefix, express.static(path));
    output.sendDone({
      out: app
    });
  });
  return c;
};
