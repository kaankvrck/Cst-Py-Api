def CstPickFaceFromPoint(mws, Component, Name, xPoint, yPoint, zPoint):
    pick = mws.Pick

    pick.PickFaceFromPoint((Component + ':' + Name), str(xPoint), str(yPoint), str(zPoint))
