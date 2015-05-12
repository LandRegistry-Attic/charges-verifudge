#################################################################################################
### This file contains the global variables for the various endpoints used in acceptance      ###
### tests, this abstracts the urls in the tests so that you will not need to change every     ###
### test when switching environments for example.                                             ###
#################################################################################################

$HELLOWORLD_DOMAIN = (ENV['HELLOWORLD_DOMAIN'] || 'http://localhost:5000')
