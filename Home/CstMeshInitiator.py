def CstMeshInitiator(mws):
    FDSolver = mws.FDSolver
    mesh = mws.Mesh
    meshSetting = mws.MeshSettings
    meshAdaption3D = mws.MeshAdaption3D
    PostProcess1D = mws.PostProcess1D

    FDSolver.ExtrudeOpenBC('True')

    mesh.MergeThinPECLayerFixpoints('True')
    mesh.RatioLimit('20')
    mesh.AutomeshRefineAtPecLines('True', '6')
    mesh.FPBAAvoidNonRegUnite('True')
    mesh.ConsiderSpaceForLowerMeshLimit('False')
    mesh.MinimumStepNumber('5')
    mesh.AnisotropicCurvatureRefinement('True')
    mesh.AnisotropicCurvatureRefinementFSM('True')

    meshSetting.SetMeshType('Hex')
    meshSetting.Set('RatioLimitGeometry', '20')
    meshSetting.Set('EdgeRefinementOn', '1')
    meshSetting.Set('EdgeRefinementRatio', '6')

    meshSetting.SetMeshType('HexTLM')
    meshSetting.Set('RatioLimitGeometry', '20')

    meshSetting.SetMeshType('Tet')
    meshSetting.Set('VolMeshGradation', '1.5')
    meshSetting.Set('SrfMeshGradation', '1.5')

    meshAdaption3D.SetAdaptionStrategy('Energy')

    meshSetting.SetMeshType('Hex')
    meshSetting.Set('Version', '1%')

    mesh.MeshType('PBA')

    PostProcess1D.ActivateOperation('vswr', 'true')
    PostProcess1D.ActivateOperation('yz-matrices', 'true')
