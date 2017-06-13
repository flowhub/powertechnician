{spawn} = require 'child_process'

module.exports = ->
  # Project configuration
  @initConfig
    pkg: @file.readJSON 'package.json'

    # BDD tests on Node.js
    mochaTest:
      nodejs:
        src: ['spec/*.coffee', 'spec/*.js']
        options:
          reporter: 'spec'
          grep: process.env.TESTS

  # Grunt plugins used for testing
  @loadNpmTasks 'grunt-mocha-test'

  @registerTask 'test', [
    'startRuntime'
    'mochaTest'
    'stopRuntime'
  ]
  @registerTask 'startRuntime', ->
    done = @async()
    runtime = spawn 'node', [
      "./node_modules/.bin/msgflo --graph=graphs/main.json"
    ]
    setTimeout ->
      done()
    , 4000
  @registerTask 'stopRuntime', ->
    return unless runtime
    done = @async()
    runtime.on 'close', ->
      runtime = null
      done()
    runtime.kill()
