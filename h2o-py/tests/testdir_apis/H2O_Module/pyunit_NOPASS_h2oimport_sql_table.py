from __future__ import print_function
from builtins import str
from builtins import range
import sys, os
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

def h2oimport_sql_table():
    """
    h2o.import_sql_table(connection_url, table, username, password, columns=None, optimize=True)

    Testing the h2o.import_sql_table() command here.  Copied from pyunit_NOPASS_import_sql_table.py.

    :return: none if test passes or error message otherwise
    """

    try:
        #conn_url = "jdbc:mysql://172.16.2.178:3306/ingestSQL?&useSSL=false"
        #conn_url = "jdbc:postgresql://mr-0xf2/ingestSQL"
        conn_url = os.getenv("SQLCONNURL")
        table = "citibike20k"

        #figure out username and password
        db_type = conn_url.split(":",3)[1]
        username = password = ""
        if db_type == "mysql":
            username = "root"
            password = "0xdata"
        elif db_type == "postgresql":
            username = password = "postgres"

        citi_sql = h2o.import_sql_table(conn_url, table, username, password, ["starttime", "bikeid"])
        assert citi_sql.nrow == 2e4, "h2o.import_sql_table() command is not working."
        assert citi_sql.ncol == 2, "h2o.import_sql_table() command is not working."

        sql_select = h2o.import_sql_select(conn_url, "SELECT starttime FROM citibike20k", username, password)
        assert sql_select.nrow == 2e4, "h2o.import_sql_table() command is not working."
        assert sql_select.ncol == 1, "h2o.import_sql_table() command is not working."
    except Exception as e:
        assert False, "h2o.import_sql_table() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oimport_sql_table)
else:
    h2oimport_sql_table()
