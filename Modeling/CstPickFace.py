def CstPickFace(mws, Name, id):
    pick = mws.Pick

    pick.PickFaceFromId(('component1:' + Name), str(id))
