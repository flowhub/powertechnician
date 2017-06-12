var noflo = require('noflo');
var MetarFetcher = require('metar-taf').MetarFetcher;
var metarFetcher = new MetarFetcher();
var metarParser = require('metar');

exports.getComponent = function() {
  var c = new noflo.Component();
  c.description = 'Get METAR information for a station';
  c.icon = 'cloud';
  c.inPorts.add('in', {
    datatype: 'object'
  });
  c.outPorts.add('out', {
    datatype: 'object'
  });
  c.process(function (input, output) {
    if (!input.hasData('in')) {
      return;
    }
    var station = input.getData('in');
    metarFetcher.getData(station.icao).then(function (data) {
      var clean = data.split("\n")[1];
      output.sendDone({
        out: metarParser(clean)
      });
    }, function (err) {
      output.done(err);
    });
  });
  return c;
};
