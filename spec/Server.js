var http = require('http');
var stations = require('../stations.json');
var chai = require('chai');

describe('Server', function () {
  var req = function (path, callback) {
    var options = {
      hostname: 'localhost',
      port: 5000,
      method: 'GET',
      path: path
    };
    http.get(options, function (res) {
      if (res.statusCode !== 200) {
        return callback(new Error("Returned " + res.statusCode));
      }
      var data = '';
      res.on('data', function (chunk) {
        data += chunk;
      });
      res.on('end', function () {
        var result = JSON.parse(data);
        callback(null, result);
      });
    });
  };
  describe('serving stations list', function () {
    it('should return a list like configured on server', function (done) {
      this.timeout(4000);
      req('/', function (err, result) {
        if (err) {
          return done(err);
        }
        chai.expect(result).to.eql(stations);
        done();
      });
    });
  });
});
