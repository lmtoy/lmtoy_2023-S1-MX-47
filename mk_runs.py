#! /usr/bin/env python
#
#   script generator for project="2021-S1-US-3"
#
#   lmtinfo.py grep US-3 Science Map | awk '{print $2}' | sort


import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy)
    from lmtoy import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2023-S1-MX-47"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["11863-3703"] =  [ 105120, 105121, 105122,                                         # feb 9
                      105354, 105355, 105356,]                                        # feb 10

on["9487-9102"] = [ 104790, 104791, 104792, 104794, 104795, 104796, 104798, 104799,
                    104800, 104803, 104804, 104805, 104807, 104808, 104809, 104811,
                    104812, 104813, 104828, 104829, 104830, 104832, 104833,           # feb 6
                    104944, 104945, 104946,                                           # feb 8
                    105236, 105237, 105238,]                                          # feb 10

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["11863-3703"] = ""
pars1["9487-9102"] = "xlines=110.7,0.3"


#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["11863-3703"] = ""
pars2["9487-9102"] = "srdp=1 admit=0"

runs.mk_runs(project, on, pars1, pars2)
