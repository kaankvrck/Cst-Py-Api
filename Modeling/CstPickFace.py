def CstPickFace(mws, component, Name, id):
    pick = mws.Pick

    pick.PickFaceFromId((component + ':' + Name), str(id))
