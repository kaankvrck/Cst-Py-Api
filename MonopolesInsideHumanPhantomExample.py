import win32com.client
import numpy as np
from matplotlib import pyplot as plt

from Home.CstDefineUnits import *
from Home.CstSaveProject import *
from Home.CstDefineBackroundMaterial import *
from Simulation.CstDefineFrequencyRange import *
from Simulation.CstDefineEfieldMonitor import *
from Simulation.CstDefineFarfieldMonitor import *
from Simulation.CstDiscretePort import *
from Simulation.CstDefineOpenBoundary import *
from Simulation.CstDefineTimedomainSolver import *
from Modeling.Cstbrick import *
from Modeling.Cstcylinder import *
from Modeling.CstSubtract import *
from Modeling.CstAdd import *
from Materials.CstBone import *
from Materials.CstMuscle import *
from Materials.CstTeflonPTFElossy import *
from PostProcessing.CstResultParameters import *
from PostProcessing.CstExportTouchstone import *

#cst = win32com.client.Dispatch("CSTStudio.Application")
#mws = cst.NewMWS()

cst = win32com.client.dynamic.Dispatch("CSTStudio.Application")
cst.SetQuietMode(True)
new_mws = cst.NewMWS()
mws = cst.Active3D()

Geometry = 'mm'
Frequency = 'GHz'
Time = 'ns'
TemperatureUnit = 'Kelvin'
Voltage = 'V'
Current = 'A'
Resistance = 'Ohm'
Conductance = 'S'
Capacitance = 'PikoF'
Inductance = 'NanoH'

CstDefineUnits(mws, Geometry, Frequency, Time, TemperatureUnit, Voltage, Current, Resistance, Conductance, Capacitance,
               Inductance)

Name = 'Muscle'
component = 'component1'
material = 'Muscle'
Xrange = [-65, 65]
Yrange = [-77, 157.5]
Zrange = [4.1, 80]
CstMuscle(mws)
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

Name = 'Bone'
component = 'component1'
material = 'Bone'
OuterRadius = 17.5
InnerRadius = 0
Xcenter = 0
Ycenter = 30
Zrange = [-40, 120]
CstBone(mws)
Cstcylinder(mws, Name, component, material, 'Y', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

component1 = 'component1:Muscle'
component2 = 'component1:Bone'
CstSubtract(mws, component1, component2)
Cstcylinder(mws, Name, component, material, 'Y', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Coat1'
component = 'component1'
material = 'Teflon (PTFE) (lossy)'
OuterRadius = 1.4
InnerRadius = 0
Xcenter = 0
Ycenter = 30
Zrange = [2.1, 45.2]
CstTeflonPTFElossy(mws)
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Coat2'
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

component1 = 'component1:Muscle'
component2 = 'component1:Coat1'
CstSubtract(mws, component1, component2)
component1 = 'component1:Bone'
component2 = 'component1:Coat2'
CstSubtract(mws, component1, component2)

Name = 'Coat1'
component = 'component1'
material = 'Teflon (PTFE) (lossy)'
OuterRadius = 1.4
InnerRadius = 0
Xcenter = 0
Ycenter = 50
Zrange = [2.1, 45.2]
CstTeflonPTFElossy(mws)
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Coat2'
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

component1 = 'component1:Muscle'
component2 = 'component1:Coat1'
CstSubtract(mws, component1, component2)
component1 = 'component1:Bone'
component2 = 'component1:Coat2'
CstSubtract(mws, component1, component2)

Name = 'Coat1'
component = 'component1'
material = 'Teflon (PTFE) (lossy)'
OuterRadius = 1.4
InnerRadius = 0.8
Xcenter = 0
Ycenter = 30
Zrange = [2.1, 45.2]
CstTeflonPTFElossy(mws)
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Coatcap1'
component = 'component1'
material = 'Teflon (PTFE) (lossy)'
OuterRadius = 1.4
InnerRadius = 0
Xcenter = 0
Ycenter = 30
Zrange = [45, 45.2]
CstTeflonPTFElossy(mws)
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Coat2'
component = 'component1'
material = 'Teflon (PTFE) (lossy)'
OuterRadius = 1.4
InnerRadius = 0.8
Xcenter = 0
Ycenter = 50
Zrange = [2.1, 45.2]
CstTeflonPTFElossy(mws)
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Coatcap2'
component = 'component1'
material = 'Teflon (PTFE) (lossy)'
OuterRadius = 1.4
InnerRadius = 0
Xcenter = 0
Ycenter = 50
Zrange = [45, 45.2]
CstTeflonPTFElossy(mws)
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

component1 = 'component1:Coat1'
component2 = 'component1:Coatcap1'
CstAdd(mws, component1, component2)
component1 = 'component1:Coat2'
component2 = 'component1:Coatcap2'
CstAdd(mws, component1, component2)

Name = 'Conductor1'
component = 'component1'
material = 'PEC'
OuterRadius = 0.8
InnerRadius = 0
Xcenter = 0
Ycenter = 30
Zrange = [2, 40]
CstTeflonPTFElossy(mws)
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Conductor2'
component = 'component1'
material = 'PEC'
OuterRadius = 0.8
InnerRadius = 0
Xcenter = 0
Ycenter = 50
Zrange = [2, 40]
CstTeflonPTFElossy(mws)
Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

Name = 'Groundplane1'
component = 'component1'
material = 'PEC'
Xrange = [-40, 40]
Yrange = [-51, 39]
Zrange = [-4, -2]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

Name = 'Groundplane2'
component = 'component1'
material = 'PEC'
Xrange = [-40, 40]
Yrange = [41, 129]
Zrange = [-4, - 2]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

PortNumber = 1
SetP1 = [0, 50, 2]
SetP2 = [0, 50, -2]
CstDiscretePort(mws, PortNumber, SetP1, SetP2)

PortNumber = 2
SetP1 = [0, 30, 2]
SetP2 = [0, 30, -2]
CstDiscretePort(mws, PortNumber, SetP1, SetP2)

CstDefineFrequencyRange(mws, 0.5, 4)

for monitorindex in np.arange(0.5, 4, 0.5):
    CstDefineEfieldMonitor(mws, 'e-field' + str(monitorindex), monitorindex)
    CstDefineFarfieldMonitor(mws, 'farfield' + str(monitorindex), monitorindex)

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

CstSaveProject(mws)
CstDefineTimedomainSolver(mws, -30)

frequencies_list, [y_real, y_imag], y_list, [x_label, y_label, plot_title] = CstResultParameters(mws, parent_path=r'1D Results\S-Parameters', run_id=0, result_id=0)

export_file_path = 'E:\\demo\\monopole_human_phantom_demo.txt'
CstExportTouchstone(mws, export_file_path)

cst.Quit()