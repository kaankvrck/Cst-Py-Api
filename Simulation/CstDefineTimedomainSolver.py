def CstDefineTimedomainSolver(mws, SteadyStateLimit):
    mesh = mws.Mesh
    solver = mws.Solver

    mesh.SetCreator('High Frequency')

    solver.Method('Hexahedral')
    solver.CalculationType('TD-S')
    solver.StimulationPort('All')
    solver.StimulationMode('All')
    solver.SteadyStateLimit(str(SteadyStateLimit))
    solver.MeshAdaption('False')
    solver.NormingImpedance('50')
    solver.CalculateModesOnly('False')
    solver.SParaSymmetry('False')
    solver.StoreTDResultsInCache('False')
    solver.FullDeembedding('False')
    solver.SuperimposePLWExcitation('False')
    solver.UseSensitivityAnalysis('False')
    solver.Start
