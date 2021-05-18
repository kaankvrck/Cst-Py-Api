def CstActivateLocalWCS(mws, SetNormal, SetOrigin, SetUVector, Activate):
    wcs = mws.WCS

    if Activate == 1:
        wcs.ActivateWCS('local')
        wcs.SetNormal(str(SetNormal(0)), str(SetNormal(1)), str(SetNormal(2)))
        wcs.SetOrigin(str(SetOrigin(0)), str(SetOrigin(1)), str(SetOrigin(2)))
        wcs.SetUVector(str(SetUVector(0)), str(SetUVector(1)), str(SetUVector(2)))
    else:
        wcs.ActivateWCS('Global')
