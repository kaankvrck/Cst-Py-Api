import win32com.client

from Home.CstDefaultUnits import *
from Home.CstActivateLocalWCS import *
from Home.CstMeshInitiator import *
from Home.CstDefineBackroundMaterial import *
from Home.CstSaveProject import *
from Simulation.CstDefineFrequencyRange import *
from Simulation.CstWaveguidePort import *
from Simulation.CstDefineOpenBoundary import *
from Simulation.CstDefineTimedomainSolver import *
from Materials.CstFR4lossy import *
from Materials.CstCopperPureLossy import *
from Modeling.Cstbrick import *
from Modeling.CstSubtract import *
from Modeling.CstPickMidPoint import *
from Modeling.CstAlignWCSwithPoint import *
from Modeling.CstAlignWCSwithFace import *
from Modeling.CstPickFace import *

cst = win32com.client.Dispatch("CSTStudio.Application")
mws = cst.NewMWS()

CstDefaultUnits(mws)
ComponentList = 'component1'

CstCopperPureLossy(mws)
CstFR4lossy(mws)

g = 3
h = 2.5
l1 = 22
l2 = 15
ls = 25
lw = 1.4
s = 1.5
t = 0.17
w = 2

Name = 'Substrate'
component = 'component1'
material = 'FR-4 (lossy)'
Xrange = [-ls / 2, ls / 2]
Yrange = [-ls / 2, ls / 2]
Zrange = [-h, 0]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

Name = 'Ring1'
component = 'component1'
material = 'Copper (pure)'
Xrange = [-l1 / 2, l1 / 2]
Yrange = [-l1 / 2, l1 / 2]
Zrange = [0, t]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

Name = 'Cut1'
component = 'component1'
material = 'Copper (pure)'
Xrange = [-(l1 / 2) + w, (l1 / 2) - w]
Yrange = [-(l1 / 2) + w, (l1 / 2) - w]
Zrange = [0, t]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

component1 = 'component1:Ring1'
component2 = 'component1:Cut1'
CstSubtract(mws, component1, component2)

Name = 'Ring1'
id = 12
CstPickMidPoint(mws, Name, id)
CstAlignWCSwithPoint(mws)

Name = 'Cut2'
component = 'component1'
material = 'Copper (pure)'
Xrange = [-g / 2, g / 2]
Yrange = [0, w]
Zrange = [0, t]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

component1 = 'component1:Ring1'
component2 = 'component1:Cut2'
CstSubtract(mws, component1, component2)

SetNormal = [0, 0, 1]
SetOrigin = [0, 0, 0]
SetUVector = [1, 0, 0]

CstActivateLocalWCS(mws, SetNormal, SetOrigin, SetUVector, 0)

Name = 'Ring2'
component = 'component1'
material = 'Copper (pure)'
Xrange = [-(l1 / 2) + w + s, (l1 / 2) - w - s]
Yrange = [-(l1 / 2) + w + s, (l1 / 2) - w - s]
Zrange = [0, t]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

Name = 'Cut3'
component = 'component1'
material = 'Copper (pure)'
Xrange = [-(l1 / 2) + 2 * w + s, (l1 / 2) - 2 * w - s]
Yrange = [-(l1 / 2) + 2 * w + s, (l1 / 2) - 2 * w - s]
Zrange = [0, t]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

component1 = 'component1:Ring2'
component2 = 'component1:Cut3'
CstSubtract(mws, component1, component2)

Name = 'Ring2'
id = 10
CstPickMidPoint(mws, Name, id)
CstAlignWCSwithPoint(mws)

Name = 'Cut4'
component = 'component1'
material = 'Copper (pure)'
Xrange = [-g / 2, g / 2]
Yrange = [0, -w]
Zrange = [0, t]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

component1 = 'component1:Ring2'
component2 = 'component1:Cut4'
CstSubtract(mws, component1, component2)

CstActivateLocalWCS(mws, SetNormal, SetOrigin, SetUVector, 0)

Name = 'Substrate'
id = 2
CstPickFace(mws, Name, id)
CstAlignWCSwithFace(mws)

Name = 'Wire'
component = 'component1'
material = 'Copper (pure)'
Xrange = [-(lw / 2), (lw / 2)]
Yrange = [-(ls / 2), (ls / 2)]
Zrange = [0, t]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)
CstActivateLocalWCS(mws, SetNormal, SetOrigin, SetUVector, 0)
CstDefineFrequencyRange(mws, 7, 13)
CstMeshInitiator(mws)
minfrequency = 7

XminSpace = 0
XmaxSpace = 0
YminSpace = 0
YmaxSpace = 0
ZminSpace = ls / 2
ZmaxSpace = ls / 2
CstDefineBackroundMaterial(mws, XminSpace, XmaxSpace, YminSpace, YmaxSpace, ZminSpace, ZmaxSpace)

Xmin = 'open'
Xmax = 'electric'
Ymin = 'electric'
Ymax = 'electric'
Zmin = 'magnetic'
Zmax = 'magnetic'
CstDefineOpenBoundary(mws, minfrequency, Xmin, Xmax, Ymin, Ymax, Zmin, Zmax)

PortNumber = 1
Xrange = [-13, -13]
Yrange = [-13, 13]
Zrange = [-3, 0]
XrangeAdd = [0, 0]
YrangeAdd = [0, 0]
ZrangeAdd = [0, 0]
CstWaveguidePort(mws, PortNumber, Xrange, Yrange, Zrange, XrangeAdd, YrangeAdd, ZrangeAdd, 'Full', 'xmin')

PortNumber = 2
Xrange = [13, 13]
Yrange = [-13, 13]
Zrange = [-3, 0]
XrangeAdd = [0, 0]
YrangeAdd = [0, 0]
ZrangeAdd = [0, 0]
CstWaveguidePort(mws, PortNumber, Xrange, Yrange, Zrange, XrangeAdd, YrangeAdd, ZrangeAdd, 'Full', 'xmax')

CstSaveProject(mws)
CstDefineTimedomainSolver(mws, -40)
