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

def h2olazy_import():
    """
    h2o.lazy_import(path)

    Testing the h2o.lazy_import() command here.  Users probably will not be using this command.  So, we
    are doing the minimum here to just call it and make sure there is no error.

    :return: none if test passes or error message otherwise
    """
    try:
        training_data = h2o.lazy_import(pyunit_utils.locate("smalldata/prostate/prostate_cat.csv"))
    except Exception as e:  # some errors are okay like version mismatch
        assert False, "h2o.lazy_import() command not working"


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2olazy_import)
else:
    h2olazy_import()
