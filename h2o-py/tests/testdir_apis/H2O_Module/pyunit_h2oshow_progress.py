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

def h2oshow_progress():
    """
    h2o.show_progress()

    Testing the h2o.show_progress() command here.  Not sure if the clients should be using this command ....
    Command is verified by eyeballing the pyunit test output file and make sure the progress bars are there.
    Here, we will assume the command runs well if there is no error message.

    :return: none if test passes or error message otherwise
    """
    try:
        h2o.show_progress()   # true by default.
        training_data = h2o.import_file(pyunit_utils.locate("smalldata/logreg/benign.csv"))
        Y = 3
        X = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10]
        model = H2OGeneralizedLinearEstimator(family="binomial", alpha=0, Lambda=1e-5)
        model.train(x=X, y=Y, training_frame=training_data)
    except Exception as e:
        assert False, "h2o.show_progress() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oshow_progress)
else:
    h2oshow_progress()
