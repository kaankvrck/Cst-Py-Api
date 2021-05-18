def CstDiscreteFacePort(mws, PortNumber, SetP1, SetP2):
    discreteFacePort = mws.DiscreteFacePort

    discreteFacePort.Reset()
    discreteFacePort.PortNumber(PortNumber)
    discreteFacePort.Type('SParameter')
    discreteFacePort.Label('')
    discreteFacePort.Impedance('50')
    discreteFacePort.VoltagePortImpedance('0.0')
    discreteFacePort.VoltageAmplitude('1.0')
    discreteFacePort.SetP1('True', SetP1[0], SetP1[1], SetP1[2])
    discreteFacePort.SetP2('True', SetP2[0], SetP2[1], SetP2[2])
    discreteFacePort.InvertDirection('False')
    discreteFacePort.LocalCoordinates('False')
    discreteFacePort.Monitor('True')
    discreteFacePort.CenterEdge('True')
    discreteFacePort.UseProjection('False')
    discreteFacePort.ReverseProjection('False')
    discreteFacePort.Create()
    format(discreteFacePort)
