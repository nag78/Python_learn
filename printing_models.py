#-------------------------------------------------------------------------------
# Name:        printing models
# Purpose:
#
# Author:      Nag
#
# Created:     16.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import printing_function as pf

unprinted_disign = ['iphone case','robot pendant','dodecahedron']
completed_models = []
pf.print_models(unprinted_disign,completed_models)

pf.show_completed_models(completed_models)
