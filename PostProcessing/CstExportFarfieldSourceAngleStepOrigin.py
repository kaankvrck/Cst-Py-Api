def CstExportFarfieldSourceAngleStepOrigin(mws, exportpath, frequency, port, StepTheta, StepPhi, Origin, Position):
    farfieldPlot = mws.FarfieldPlot

    farfieldPlot.Plottype('3D')
    farfieldPlot.Vary('angle1')
    farfieldPlot.Theta('90')
    farfieldPlot.Phi('90')
    farfieldPlot.Step(str(StepTheta))
    farfieldPlot.Step2(str(StepPhi))
    farfieldPlot.SetLockSteps('False')
    farfieldPlot.SetPlotRangeOnly('False')
    farfieldPlot.SetThetaStart('0')
    farfieldPlot.SetThetaEnd('180')
    farfieldPlot.SetPhiStart('0')
    farfieldPlot.SetPhiEnd('360')
    farfieldPlot.SetTheta360('False')
    farfieldPlot.SymmetricRange('False')
    farfieldPlot.SetTimeDomainFF('False')
    farfieldPlot.SetFrequency(str(frequency))
    farfieldPlot.SetTime('0')
    farfieldPlot.SetColorByValue('True')
    farfieldPlot.DrawStepLines('False')
    farfieldPlot.DrawIsoLongitudeLatitudeLines('False')
    farfieldPlot.ShowStructure('False')
    farfieldPlot.SetStructureTransparent('False')
    farfieldPlot.SetFarfieldTransparent('False')
    farfieldPlot.SetSpecials('enablepolarextralines')
    farfieldPlot.SetPlotMode('efield')
    farfieldPlot.Distance('1')
    farfieldPlot.UseFarfieldApproximation('True')
    farfieldPlot.SetScaleLinear('True')
    farfieldPlot.SetLogRange('40')
    farfieldPlot.SetLogNorm('0')
    farfieldPlot.DBUnit('0')
    farfieldPlot.EnableFixPlotMaximum('False')
    farfieldPlot.SetFixPlotMaximumValue('1')
    farfieldPlot.SetInverseAxialRatio('False')
    farfieldPlot.SetAxesType('user')
    farfieldPlot.SetAntennaType('unknown')
    farfieldPlot.Phistart('1.000000e+000', '0.000000e+000', '0.000000e+000')
    farfieldPlot.Thetastart('0.000000e+000', '0.000000e+000', '1.000000e+000')
    farfieldPlot.PolarizationVector('0.000000e+000', '1.000000e+000', '0.000000e+000')
    farfieldPlot.SetCoordinateSystemType('spherical')
    farfieldPlot.SetAutomaticCoordinateSystem('True')
    farfieldPlot.SetPolarizationType('linear')
    farfieldPlot.SlantAngle('0.000000e+000')
    if Origin == 'bbox':
        farfieldPlot.Origin('bbox')
        farfieldPlot.Userorigin('0.000000e+000', '0.000000e+000', '0.000000e+000')
    if Origin == 'free':
        farfieldPlot.Origin('free')
        farfieldPlot.Userorigin(str(Position(0)), str(Position(1)), str(Position(2)))
    farfieldPlot.SetUserDecouplingPlane('False')
    farfieldPlot.UseDecouplingPlane('False')
    farfieldPlot.DecouplingPlaneAxis('x')
    farfieldPlot.DecouplingPlanePosition('0.000000e+000')
    farfieldPlot.LossyGround('False')
    farfieldPlot.GroundEpsilon('1')
    farfieldPlot.GroundKappa('0')
    farfieldPlot.EnablePhaseCenterCalculation('False')
    farfieldPlot.SetPhaseCenterAngularLimit('3.000000e+001')
    farfieldPlot.SetPhaseCenterComponent('boresight')
    farfieldPlot.SetPhaseCenterPlane('both')
    farfieldPlot.ShowPhaseCenter('True')
    farfieldPlot.StoreSettings()

    selectTreeItem = mws.SelectTreeItem('Farfields/farfield' + str(frequency) + ' ' + '[' + str(port) + ']')

    farfieldPlot.ASCIIExportAsSource(exportpath)

