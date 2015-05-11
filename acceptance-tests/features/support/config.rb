### Configure Capybara and Poltergeist
require 'capybara/cucumber'
require 'capybara/poltergeist'

include Capybara::DSL
Capybara.default_selector = :xpath
Capybara.default_wait_time = 10
Capybara.app_host = 'http://localhost:4567'

Capybara.default_driver = :poltergeist
Capybara.javascript_driver = :poltergeist

Capybara.register_driver :poltergeist do |app|
  Capybara::Poltergeist::Driver.new(app, :inspector => true, :js_errors => true)
end

### Configure Assertions
require 'test/unit'
include Test::Unit::Assertions
