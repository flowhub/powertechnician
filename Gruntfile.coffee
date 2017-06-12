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
    'mochaTest'
  ]
