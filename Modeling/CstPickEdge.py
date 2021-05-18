def CstPickEdge(mws, ComponentName, position):
    pick = mws.Pick

    pick.PickEdgeFromId(('component1:' + ComponentName), str(position), str(position))
