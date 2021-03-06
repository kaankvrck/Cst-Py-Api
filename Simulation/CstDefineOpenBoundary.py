def CstDefineOpenBoundary(mws, minfrequency, Xmin, Xmax, Ymin, Ymax, Zmin, Zmax):
    boundary = mws.Boundary
    plot = mws.Plot

    boundary.Xmin(Xmin)
    boundary.Xmax(Xmax)
    boundary.Ymin(Ymin)
    boundary.Ymax(Ymax)
    boundary.Zmin(Zmin)
    boundary.Zmax(Zmax)
    boundary.Xsymmetry('none')
    boundary.Ysymmetry('none')
    boundary.Zsymmetry('none')
    boundary.XminThermal('isothermal')
    boundary.XmaxThermal('isothermal')
    boundary.YminThermal('isothermal')
    boundary.YmaxThermal('isothermal')
    boundary.ZminThermal('isothermal')
    boundary.ZmaxThermal('isothermal')
    boundary.XsymmetryThermal('none')
    boundary.YsymmetryThermal('none')
    boundary.ZsymmetryThermal('none')
    boundary.ApplyInAllDirections('False')
    boundary.ApplyInAllDirectionsThermal('False')
    boundary.XminTemperature('')
    boundary.XminTemperatureType('None')
    boundary.XmaxTemperature('')
    boundary.XmaxTemperatureType('None')
    boundary.YminTemperature('')
    boundary.YminTemperatureType('None')
    boundary.YmaxTemperature('')
    boundary.YmaxTemperatureType('None')
    boundary.ZminTemperature('')
    boundary.ZminTemperatureType('None')
    boundary.ZmaxTemperature('')
    boundary.ZmaxTemperatureType('None')
    if Xmin == 'unit cell':
        boundary.XPeriodicShift('0.0')
        boundary.YPeriodicShift('0.0')
        boundary.ZPeriodicShift('0.0')
        boundary.PeriodicUseConstantAngles('False')
        boundary.SetPeriodicBoundaryAngles('0.0', '0.0')
        boundary.SetPeriodicBoundaryAnglesDirection('outward')
        boundary.UnitCellFitToBoundingBox('True')
        boundary.UnitCellDs1('0.0')
        boundary.UnitCellDs2('0.0')
        boundary.UnitCellAngle('90.0')
    if Xmin == 'expanded open':
        boundary.ReflectionLevel('0.0001')
        boundary.MinimumDistanceType('Fraction')
        boundary.MinimumDistancePerWavelengthNewMeshEngine('4')
        boundary.MinimumDistanceReferenceFrequencyType('CenterNMonitors')
        boundary.FrequencyForMinimumDistance(str(minfrequency))
        boundary.SetAbsoluteDistance('0.0')
        plot.DrawBox('True')
