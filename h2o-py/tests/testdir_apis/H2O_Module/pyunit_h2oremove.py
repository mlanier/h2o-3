from __future__ import print_function
from builtins import str
from builtins import range
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import urllib.parse
from h2o.estimators.glm import H2OGeneralizedLinearEstimator

# DISCLAMINER
#
# The main function of API tests is to make sure that changes to the API are captured
# before the customers do.  This is to prevent breaking the customer code.  If the
# changes are necessary, we will have the chance to warn them about the changes.
#
# All API tests should be short and fast to run.  The main purposes of API tests are to
# make sure that the command in its most popular forms run correctly when user types in
# correct input arguments.  Light weight checking will be provided on the command output
# to make sure that we are getting the correct responses.
#
# For exhaustive tests using all possible combination of input arguments, making sure all
# responses of the API commands are correct, or if in error, the correct error messages
# are sent should be done elsewhere.

def h2oremove():
    """
    h2o.remove(x)

    Testing the h2o.remove() command here.

    :return: none if test passes or error message otherwise
    """
    # call with no arguments
    try:
        training_data = h2o.import_file(pyunit_utils.locate("smalldata/logreg/benign.csv"))
        assert training_data.__class__.__name__ == "H2OFrame", "h2o.import_file() command is not working."
        h2o.remove(training_data)
        training_data.nrow  # this command should generate an error since training_data should have been deleted.
    except Exception as e:
        assert "object has no attribute" in e.args[0], "h2o.remove() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oremove)
else:
    h2oremove()
