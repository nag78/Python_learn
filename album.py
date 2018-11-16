#-------------------------------------------------------------------------------
# Name:        album
# Purpose:
#
# Author:      Nag
#
# Created:     15.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def make_album(musician,name_album,track=None):
    album = {'name':musician,'n_album':name_album}
    if track:
        album['track'] = track
    return album
lube = make_album('lube','lube')
bilan = make_album('bilan','nocnoi huligan')
allegrova = make_album('allegrova','imperatrica',12)
print(lube)
print(bilan)
print(allegrova)