################################################################################
### This file contains the global variables for the various endpoints used   ###
### in acceptance tests, this abstracts the urls so that you will not        ###
### need to change every test when switching environments for example.       ###
################################################################################

# Provides access to URLs to tests
class Urls
  def self.verifudge
    (ENV['DOMAIN'] || 'http://verifudge.dev.service.gov.uk')
  end
end
