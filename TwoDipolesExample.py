import win32com.client
import numpy as np

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
from Materials.CstTeflonPTFElossy import *
from Materials.CstCopperAnnealedLossy import *

cst = win32com.client.Dispatch("CSTStudio.Application")
mws = cst.NewMWS()

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

material = 'Copper (annealed)'
Name = 'Conductor1'
OuterRadius = 1
InnerRadius = 0
Xcenter = 0
Ycenter = 0
Zrange = [-30, 30]
Cstcylinder(mws, Name, ComponentList, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Conductor2'
OuterRadius = 1
InnerRadius = 0
Xcenter = 0
Ycenter = 240
Zrange = [-30, 30]
Cstcylinder(mws, Name, ComponentList, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Gap1'
OuterRadius = 1
InnerRadius = 0
Xcenter = 0
Ycenter = 0
Zrange = [-5, 5]
Cstcylinder(mws, Name, ComponentList, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Gap2'
OuterRadius = 1
InnerRadius = 0
Xcenter = 0
Ycenter = 240
Zrange = [-5, 5]
Cstcylinder(mws, Name, ComponentList, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

position = 1
CstPickEdge(mws, 'Gap1', position)

position = 2
CstPickEdge(mws, 'Gap1', position)

PortNumber = 1
SetP1 = [1, 0, -5]
SetP2 = [1, 0, 5]
CstDiscreteFacePort(mws, PortNumber, SetP1, SetP2)

position = 1
CstPickEdge(mws, 'Gap2', position)

position = 2
CstPickEdge(mws, 'Gap2', position)

PortNumber = 2
SetP1 = [0, 241, -5]
SetP2 = [0, 241, 5]
CstDiscreteFacePort(mws, PortNumber, SetP1, SetP2)
CstTeflonPTFElossy(mws)

Name = 'Coat1'
component = 'component1'
material = 'Teflon (PTFE) (lossy)'
OuterRadius = 2
InnerRadius = 1
Xcenter = 0
Ycenter = 0
Zrange = [-30, 30]
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Coat2'
Ycenter = 240
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'CoatCap1a'
component = 'component1'
material = 'Teflon (PTFE) (lossy)'
OuterRadius = 2
InnerRadius = 0
Xcenter = 0
Ycenter = 0
Zrange = [-31, -30]
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'CoatCap1b'
OuterRadius = 2
InnerRadius = 0
Xcenter = 0
Ycenter = 0
Zrange = [30, 31]
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'CoatCap2a'
component = 'component1'
material = 'Teflon (PTFE) (lossy)'
OuterRadius = 2
InnerRadius = 0
Xcenter = 0
Ycenter = 240
Zrange = [-31, -30]
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'CoatCap2b'
OuterRadius = 2
InnerRadius = 0
Xcenter = 0
Ycenter = 240
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
