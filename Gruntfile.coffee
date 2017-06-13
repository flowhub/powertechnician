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
  runtime = null
  @registerTask 'startRuntime', ->
    done = @async()
    runtime = spawn 'node', [
      "./node_modules/.bin/msgflo"
      "--graph=graphs/main.json"
    ],
      cwd: process.cwd()
      env:
        MSGFLO_BROKER: process.env.MSGFLO_BROKER
        PATH: process.env.PATH
        PORT: 5000
    runtime.stderr.on 'data', (data) ->
      str = data.toString()
      console.error str
    runtime.stdout.on 'data', (data) ->
      str = data.toString()
      console.log str
      if str.indexOf('app.flowhub.io') isnt -1
        setTimeout ->
          done()
        , 2000
      return
  @registerTask 'stopRuntime', ->
    return unless runtime
    done = @async()
    runtime.on 'close', ->
      runtime = null
      done()
    runtime.kill()
