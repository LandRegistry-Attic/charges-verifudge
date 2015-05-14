# govuk-flask-skeleton

## Testing

### Running the Tests

All of the acceptance tests are contained within the acceptance-tests folder with the feature files under the features folder and the step-definitions under the steps folder.

If you would like to run all of the acceptance tests then navigate into the acceptance-tests folder and run the following command:

'./run_tests.sh'

### Running Rubocop

Rubocop is ruby gem that will check any ruby code in the repository against the ruby style guide and then provide a report of any offenses.

In order to run Rubocop on the acceptance test code then navigate into the acceptance test folder and run the command:

' ./run_linting.sh'

If you wish to amend what cops are used, what files are ignored when running Rubocop then you will need to put this in the rubocop.yml file.
