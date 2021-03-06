def CstDiscretePort(mws, PortNumber, SetP1, SetP2):
    discretePort = mws.DiscretePort

    discretePort.Reset()
    discretePort.PortNumber(str(PortNumber))
    discretePort.Type('SParameter')
    discretePort.Label('')
    discretePort.Impedance('50')
    discretePort.VoltagePortImpedance('0.0')
    discretePort.Voltage('1.0')
    discretePort.Current('1.0')
    discretePort.SetP1('False', SetP1[0], SetP1[1], SetP1[2])
    discretePort.SetP2('False', SetP2[0], SetP2[1], SetP2[2])
    discretePort.InvertDirection('False')
    discretePort.LocalCoordinates('False')
    discretePort.Monitor('True')
    discretePort.Radius('0.0')
    discretePort.Wire('')
    discretePort.Position('end1')
    discretePort.Create()
    format(discretePort)
