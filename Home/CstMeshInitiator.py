def CstMeshInitiator(mws):
    FDSolver = mws.FDSolver
    mesh = mws.Mesh
    meshSetting = mws.MeshSettings
    meshAdaption3D = mws.MeshAdaption3D
    PostProcess1D = mws.PostProcess1D

    FDSolver.ExtrudeOpenBC('True')

    mesh.MeshType('PBA')
    mesh.SetCreator('High Frequency')

    meshSetting.SetMeshType('Hex')
    meshSetting.Set('Version', '1%')

    # MAX CELL - WAVELENGTH REFINEMENT
    meshSetting.Set('StepsPerWaveNear', '20')
    meshSetting.Set('StepsPerWaveFar', '20')
    meshSetting.Set('WavelengthRefinementSameAsNear', '1')

    # MAX CELL - GEOMETRY REFINEMENT
    meshSetting.Set('StepsPerBoxNear', '20')
    meshSetting.Set('StepsPerBoxFar', '1')
    meshSetting.Set('MaxStepNear', '0')
    meshSetting.Set('MaxStepFar', '0')
    meshSetting.Set('ModelBoxDescrNear', 'maxedge')
    meshSetting.Set('ModelBoxDescrFar', 'maxedge')
    meshSetting.Set('UseMaxStepAbsolute', '0')
    meshSetting.Set('GeometryRefinementSameAsNear', '0')

    # MIN CELL
    meshSetting.Set('UseRatioLimitGeometry', '1')
    meshSetting.Set('RatioLimitGeometry', '20')
    meshSetting.Set('MinStepGeometryX', '0')
    meshSetting.Set('MinStepGeometryY', '0')
    meshSetting.Set('MinStepGeometryZ', '0')
    meshSetting.Set('UseSameMinStepGeometryXYZ', '1')

    meshSetting.Set('PlaneMergeVersion', '2')

    meshSetting.SetMeshType('Hex')
    meshSetting.Set('EdgeRefinementOn', '1')
    meshSetting.Set('EdgeRefinementRatio', '6')

    mesh.MergeThinPECLayerFixpoints('True')
    mesh.RatioLimit('20')
    mesh.AutomeshRefineAtPecLines('True', '6')
    mesh.FPBAAvoidNonRegUnite('True')
    mesh.ConsiderSpaceForLowerMeshLimit('False')
    mesh.MinimumStepNumber('5')
    mesh.AnisotropicCurvatureRefinement('True')
    mesh.AnisotropicCurvatureRefinementFSM('True')

    meshSetting.SetMeshType('HexTLM')
    meshSetting.Set('RatioLimitGeometry', '20')

    meshSetting.SetMeshType('Tet')
    meshSetting.Set('VolMeshGradation', '1.5')
    meshSetting.Set('SrfMeshGradation', '1.5')

    meshAdaption3D.SetAdaptionStrategy('Energy')

    PostProcess1D.ActivateOperation('vswr', 'true')
    PostProcess1D.ActivateOperation('yz-matrices', 'true')
