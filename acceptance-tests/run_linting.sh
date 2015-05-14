#################################################################################################
### This shell script is used to run style guide checkers on code in the acceptance-tests     ###
### folder such as Rubocop.                                                                   ###
#################################################################################################

### Run rubocop gem to check acceptance tests against the Ruby style guide.
rubocop -c rubocop.yml
