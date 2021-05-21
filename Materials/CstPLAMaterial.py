def CstPLAMaterial(mws):
    material = mws.Material

    material.Reset()
    material.Name('PLA')
    material.FrqType('all')
    material.Type('Normal')
    material.MaterialUnit('Frequency', 'GHz')
    material.MaterialUnit('Geometry', 'mm')
    material.Epsilon('2.54')
    material.Mu('1.0')
    material.Kappa('0.0')
    material.TanD('0.015')
    material.TanDFreq('10.0')
    material.TanDGiven('True')
    material.TanDModel('ConstTanD')
    material.KappaM('0.0')
    material.TanDM('0.0')
    material.TanDMFreq('0.0')
    material.TanDMGiven('False')
    material.TanDMModel('ConstKappa')
    material.DispModelEps('None')
    material.DispModelMu('None')
    material.DispersiveFittingSchemeEps('General 1st')
    material.DispersiveFittingSchemeMu('General 1st')
    material.UseGeneralDispersionEps('False')
    material.UseGeneralDispersionMu('False')
    material.Rho('0.0')
    material.ThermalType('Normal')
    material.ThermalConductivity('0')
    material.SetActiveMaterial('all')
    material.Colour('0', '1', '1')
    material.Wireframe('False')
    material.Transparency('0')
    material.Create()
    format(material)
