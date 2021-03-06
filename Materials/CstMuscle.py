def CstMuscle(mws):
    material = mws.Material

    material.Reset()
    material.Name('Muscle')
    material.FrqType('all')
    material.Type('Normal')
    material.MaterialUnit('Frequency', 'GHz')
    material.MaterialUnit('Geometry', 'mm')
    material.Epsilon('1.0')
    material.Mu('1.0')
    material.Sigma('0.0')
    material.TanD('0.0')
    material.TanDFreq('0.0')
    material.TanDGiven('False')
    material.TanDModel('ConstSigma')
    material.ConstTanDModelOrderEps('1')
    material.ReferenceCoordSystem('global')
    material.CoordSystemType('Cartesian')
    material.SigmaM('0.0')
    material.TanDM('0.0')
    material.TanDMFreq('0.0')
    material.TanDMGiven('False')
    material.TanDMModel('ConstSigma')
    material.ConstTanDModelOrderMu('1')
    material.DispModelEps('None')
    material.DispModelMu('None')
    material.DispersiveFittingSchemeEps('Nth Order')
    material.MaximalOrderNthModelFitEps('3')
    material.ErrorLimitNthModelFitEps('0.01')
    material.DispersiveFittingSchemeMue('Nth Order')
    material.AddDispersionFittingValueEps('0.1', '65.9724916504545', '127.192797239797', '1.0')
    material.AddDispersionFittingValueEps('0.2', '60.2280314197783', '66.7852481428503', '1.0')
    material.AddDispersionFittingValueEps('0.3', '58.2010632452303', '46.1678385280381', '1.0')
    material.AddDispersionFittingValueEps('0.4', '57.1286659331816', '35.7847612362403', '1.0')
    material.AddDispersionFittingValueEps('0.422222222222222', '56.9527716128403', '34.1456274103791', '1.0')
    material.AddDispersionFittingValueEps('0.5', '56.4454886710024', '29.5676459467637', '1.0')
    material.AddDispersionFittingValueEps('0.6', '55.9594825719793', '25.4598232248452', '1.0')
    material.AddDispersionFittingValueEps('0.7', '55.5870383230944', '22.5688659080254', '1.0')
    material.AddDispersionFittingValueEps('0.744444444444444', '55.4460666146869', '21.5480357567376', '1.0')
    material.AddDispersionFittingValueEps('0.8', '55.2857933341328', '20.4441081345782', '1.0')
    material.AddDispersionFittingValueEps('0.9', '55.0319456602686', '18.8331012626125', '1.0')
    material.AddDispersionFittingValueEps('1.06666666666667', '54.6774425815976', '16.9010535749291', '1.0')
    material.AddDispersionFittingValueEps('1.38888888888889', '54.1285131484409', '14.7095990740045', '1.0')
    material.AddDispersionFittingValueEps('1.71111111111111', '53.6680496124579', '13.5891943396758', '1.0')
    material.AddDispersionFittingValueEps('2.03333333333333', '53.2476410075004', '13.0261988069251', '1.0')
    material.AddDispersionFittingValueEps('2.35555555555556', '52.8455894055116', '12.7858457903486', '1.0')
    material.AddDispersionFittingValueEps('2.67777777777778', '52.4509933654632', '12.74554913806', '1.0')
    material.AddDispersionFittingValueEps('3', '52.057997686553', '12.8350615969651', '1.0')
    material.UseGeneralDispersionEps('True')
    material.UseGeneralDispersionMu('False')
    material.NLAnisotropy('False')
    material.NLAStackingFactor('1')
    material.NLADirectionX('1')
    material.NLADirectionY('0')
    material.NLADirectionZ('0')
    material.Rho('1041')
    material.ThermalType('Normal')
    material.ThermalConductivity('0.53')
    material.HeatCapacity('3.546')
    material.MetabolicRate('480')
    material.BloodFlow('2700')
    material.VoxelConvection('0')
    material.MechanicsType('Unused')
    material.Colour('0.784314', '0.470588', '0.470588')
    material.Wireframe('False')
    material.Reflection('False')
    material.Allowoutline('False')
    material.Transparentoutline('False')
    material.Transparency('0')
    material.Create()
    format(material)
