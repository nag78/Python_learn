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
while True:
    print("\nPlease tell me album:")
    print("(please 'q' at any time to quit)")

    m_name = input("Name musician: ")
    if m_name == 'q':
        break
    m_album = input("Album: ")
    if m_album == 'q':
        break
    m_track = input("No Track: ")
    if m_track == 'q':
        break
    n_album = make_album(m_name,m_album,m_track)
    print(n_album)
##lube = make_album('lube','lube')
##bilan = make_album('bilan','nocnoi huligan')
##allegrova = make_album('allegrova','imperatrica',12)
##print(lube)
##print(bilan)
##print(allegrova)