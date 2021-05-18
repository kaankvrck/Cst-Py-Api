def CstDefineFrequencyRange(mws, frange1, frange2):
    Solver = mws.Solver
    mesh = mws.Mesh

    Solver.FrequencyRange(str(frange1), str(frange2))

    meshSettings = mws.MeshSettings
    meshSettings.SetMeshType('Hex')
    meshSettings.Set('Version', '1%')

    mesh.MeshType('PBA')
