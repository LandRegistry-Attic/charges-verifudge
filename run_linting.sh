### Retrieve the current location the script is running
currentLocation="$(cd "$(dirname "$0")"; pwd)"

flake8 $currentLocation

exit $?
