import Imports as im

def coOrd():
    __from = []
    for i in im.branch.branches:
        __from.append(im.coordinate.getGeoLocation(i))
    return __from
