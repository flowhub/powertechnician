var noflo = require('noflo');
var MetarFetcher = require('metar-taf').MetarFetcher;
var metar = new MetarFetcher();

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
    metar.getDecodedData(station.icao).then(function (data) {
      output.sendDone({
        out: data
      });
    }, function (err) {
      output.done(err);
    });
  });
  return c;
};
