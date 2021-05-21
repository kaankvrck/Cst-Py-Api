def CstPlaneWaveExcitation(mws, Normal, EVector, Polarization, ReferenceFrequency, PhaseDifference, CircularDirection,
                           AxialRatio):
    planeWave = mws.PlaneWave

    planeWave.Reset()
    planeWave.Normal(str(Normal(0)), str(Normal(1)), str(Normal(2)))
    planeWave.EVector(str(EVector(0)), str(EVector(1)), str(EVector(2)))
    planeWave.Polarization(Polarization)
    planeWave.ReferenceFrequency(str(ReferenceFrequency))
    planeWave.PhaseDifference(str(PhaseDifference))
    planeWave.CircularDirection(CircularDirection)
    planeWave.AxialRatio(str(AxialRatio))
    planeWave.SetUserDecouplingPlane('False')
    planeWave.Store()
