#------------------------------------------------------------------------------
# connect.py (Section 1.2 and 1.3)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright (c) 2017, 2018, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

from __future__ import print_function

import cx_Oracle
#import db_config
from samples.tutorial import db_config

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
print("Database version:", con.version)
