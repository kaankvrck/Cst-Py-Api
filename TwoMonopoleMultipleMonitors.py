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
from Simulation.CstDiscretePort import *
from Simulation.CstDefineTimedomainSolver import *
from Modeling.Cstcylinder import *
from Modeling.Cstbrick import *
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

Name = 'Groundplane1'
material = 'Copper (annealed)'
Xrange = [-60, 0]
Yrange = [-30, 30]
Zrange = [0, 2]
Cstbrick(mws, Name, ComponentList, material, Xrange, Yrange, Zrange)

Name = 'Groundplane2'
material = 'Copper (annealed)'
Xrange = [20, 80]
Yrange = [-30, 30]
Zrange = [0, 2]
Cstbrick(mws, Name, ComponentList, material, Xrange, Yrange, Zrange)

Name = 'Conductor1'
OuterRadius = 2
InnerRadius = 0
Xcenter = -30
Ycenter = 0
Zrange = [8, 38]
Cstcylinder(mws, Name, ComponentList, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Conductor2'
OuterRadius = 2
InnerRadius = 0
Xcenter = 50
Ycenter = 0
Zrange = [8, 38]
Cstcylinder(mws, Name, ComponentList, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

PortNumber = 1
SetP1 = [-30, 0, 2]
SetP2 = [-30, 0, 8]
CstDiscretePort(mws, PortNumber, SetP1, SetP2)

PortNumber = 2
SetP1 = [50, 0, 2]
SetP2 = [50, 0, 8]
CstDiscretePort(mws, PortNumber, SetP1, SetP2)

CstDefineFrequencyRange(mws, 0.5, 4)

for monitorindex in np.arange(0.5, 4, 0.5):
    CstDefineEfieldMonitor(mws, 'e-field' + str(monitorindex), monitorindex)
    CstDefineHfieldMonitor(mws, 'h-field' + str(monitorindex), monitorindex)
    CstDefineFarfieldMonitor(mws, 'farfield' + str(monitorindex), monitorindex)

CstSaveProject(mws)
CstDefineTimedomainSolver(mws, -30)
