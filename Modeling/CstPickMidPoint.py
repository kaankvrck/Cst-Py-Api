def CstPickMidPoint(mws, Name, id):
    pick = mws.Pick

    pick.PickMidpointFromId(('component1:' + Name), str(id))
