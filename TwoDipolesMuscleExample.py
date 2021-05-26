import win32com.client
import numpy as np
from matplotlib import pyplot as plt

from Home.CstDefaultUnits import *
from Home.CstMeshInitiator import *
from Home.CstSaveProject import *
from Home.CstDefineBackroundMaterial import *
from Simulation.CstDefineFrequencyRange import *
from Simulation.CstDefineEfieldMonitor import *
from Simulation.CstDefineHfieldMonitor import *
from Simulation.CstDefineFarfieldMonitor import *
from Simulation.CstDefineOpenBoundary import *
from Simulation.CstDefineTimedomainSolver import *
from Simulation.CstDiscreteFacePort import *
from Modeling.Cstcylinder import *
from Modeling.CstAdd import *
from Modeling.CstPickEdge import *
from Modeling.Cstbrick import *
from Modeling.CstSubtract import *
from Materials.CstTeflonPTFElossy import *
from Materials.CstCopperAnnealedLossy import *
from Materials.CstMuscle import *
from PostProcessing.CstResultParameters import *
from PostProcessing.CstExportTouchstone import *
from PostProcessing.CstExportFarfieldSourceAngleStep import *

# cst = win32com.client.Dispatch("CSTStudio.Application")
# mws = cst.NewMWS()

cst = win32com.client.dynamic.Dispatch("CSTStudio.Application")
cst.SetQuietMode(True)
new_mws = cst.NewMWS()
mws = cst.Active3D()

CstDefaultUnits(mws)
CstMeshInitiator(mws)
ComponentList = 'component1'
CstCopperAnnealedLossy(mws)

minfrequency = 0.5
x = 'expanded open'
CstDefineOpenBoundary(mws, minfrequency, x, x, x, x, x, x)
XminSpace = 0
XmaxSpace = 0
YminSpace = 0
YmaxSpace = 0
ZminSpace = 0
ZmaxSpace = 0
CstDefineBackroundMaterial(mws, XminSpace, XmaxSpace, YminSpace, YmaxSpace, ZminSpace, ZmaxSpace)

Name = 'Muscle'
component = 'component1'
material = 'Muscle'
Xrange = [-90, 110]
Yrange = [-60, 60]
Zrange = [-50, 50]
CstMuscle(mws)
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

material = 'Copper (annealed)'
Name = 'Minus1'
OuterRadius = 2
InnerRadius = 0
Xcenter = -30
Ycenter = 0
Zrange = [-31, 31]
Cstcylinder(mws, Name, ComponentList, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Minus2'
OuterRadius = 2
InnerRadius = 0
Xcenter = 50
Ycenter = 0
Zrange = [-31, 31]
Cstcylinder(mws, Name, ComponentList, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

component1 = 'component1:Muscle'
component2 = 'component1:Minus1'
CstSubtract(mws, component1, component2)
component1 = 'component1:Muscle'
component2 = 'component1:Minus2'
CstSubtract(mws, component1, component2)

material = 'Copper (annealed)'
Name = 'Conductor1'
OuterRadius = 1
InnerRadius = 0
Xcenter = -30
Ycenter = 0
Zrange = [-30, 30]
Cstcylinder(mws, Name, ComponentList, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Conductor2'
OuterRadius = 1
InnerRadius = 0
Xcenter = 50
Ycenter = 0
Zrange = [-30, 30]
Cstcylinder(mws, Name, ComponentList, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Gap1'
OuterRadius = 1
InnerRadius = 0
Xcenter = -30
Ycenter = 0
Zrange = [-5, 5]
Cstcylinder(mws, Name, ComponentList, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Gap2'
OuterRadius = 1
InnerRadius = 0
Xcenter = 50
Ycenter = 0
Zrange = [-5, 5]
Cstcylinder(mws, Name, ComponentList, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

position = 1
CstPickEdge(mws, 'Gap1', position)

position = 2
CstPickEdge(mws, 'Gap1', position)

PortNumber = 1
SetP1 = [-29, 0, -5]
SetP2 = [-29, 0, 5]
CstDiscreteFacePort(mws, PortNumber, SetP1, SetP2)

position = 1
CstPickEdge(mws, 'Gap2', position)

position = 2
CstPickEdge(mws, 'Gap2', position)

PortNumber = 2
SetP1 = [51, 0, -5]
SetP2 = [51, 0, 5]
CstDiscreteFacePort(mws, PortNumber, SetP1, SetP2)
CstTeflonPTFElossy(mws)

Name = 'Coat1'
component = 'component1'
material = 'Teflon (PTFE) (lossy)'
OuterRadius = 2
InnerRadius = 1
Xcenter = -30
Ycenter = 0
Zrange = [-30, 30]
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Coat2'
Xcenter = 50
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'CoatCap1a'
component = 'component1'
material = 'Teflon (PTFE) (lossy)'
OuterRadius = 2
InnerRadius = 0
Xcenter = -30
Ycenter = 0
Zrange = [-31, - 30]
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'CoatCap1b'
OuterRadius = 2
InnerRadius = 0
Xcenter = -30
Ycenter = 0
Zrange = [30, 31]
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'CoatCap2a'
component = 'component1'
material = 'Teflon (PTFE) (lossy)'
OuterRadius = 2
InnerRadius = 0
Xcenter = 50
Ycenter = 0
Zrange = [-31, -30]
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'CoatCap2b'
OuterRadius = 2
InnerRadius = 0
Xcenter = 50
Ycenter = 0
Zrange = [30, 31]
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

component1 = 'component1:Coat1'
component2 = 'component1:CoatCap1a'
CstAdd(mws, component1, component2)

component1 = 'component1:Coat1'
component2 = 'component1:CoatCap1b'
CstAdd(mws, component1, component2)

component1 = 'component1:Coat2'
component2 = 'component1:CoatCap2a'
CstAdd(mws, component1, component2)

component1 = 'component1:Coat2'
component2 = 'component1:CoatCap2b'
CstAdd(mws, component1, component2)

CstDefineFrequencyRange(mws, 0.5, 4)

for monitorindex in np.arange(0.5, 4, 0.5):
    CstDefineEfieldMonitor(mws, 'e-field' + str(monitorindex), monitorindex)
    CstDefineHfieldMonitor(mws, 'h-field' + str(monitorindex), monitorindex)
    CstDefineFarfieldMonitor(mws, 'farfield' + str(monitorindex), monitorindex)

CstSaveProject(mws)
CstDefineTimedomainSolver(mws, -30)

frequencies_list, [y_real, y_imag], y_list, [x_label, y_label, plot_title] = CstResultParameters(mws,
                                                                                                 parent_path=r'1D Results\S-Parameters',
                                                                                                 run_id=0, result_id=0)

export_file_path = 'E:\\demo\\two_dipole_muscle_demo.txt'
CstExportTouchstone(mws, export_file_path)

#StepTheta = 0.25
#StepPhi = 0.25
#matrixindex = 1


#for monitorindex in np.arange(0.5, 4, 0.5):
#    port = 1
#    exportpath = 'E:\\demo\\two_dipole_muscle\\farff1' + str(monitorindex) + '.txt'
#    CstExportFarfieldSourceAngleStep(mws, exportpath, monitorindex, port, StepTheta, StepPhi)
#    port = 2
#    exportpath = 'E:\\demo\\two_dipole_muscle\\farff2' + str(monitorindex) + '.txt'
#    CstExportFarfieldSourceAngleStep(mws, exportpath, monitorindex, port, StepTheta, StepPhi)

cst.Quit()
