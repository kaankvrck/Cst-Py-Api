import win32com.client
import numpy as np
from matplotlib import pyplot as plt

from Home.CstDefineUnits import *
from Home.CstMeshInitiator import *
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
CstMeshInitiator(mws)

CstDefineFrequencyRange(mws, 0.5, 4)

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

Name = 'Groundplane'
component = 'component1'
material = 'PEC'
Xrange = [-40, 40]
Yrange = [-40, 40]
Zrange = [0, 2]

Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

Name = 'Conductor'
OuterRadius = 2
InnerRadius = 0
Xcenter = 0
Ycenter = 0
Zrange = [8, 38]

Cstcylinder(mws, Name, component, material, 'Z', OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange)

PortNumber = 1
SetP1 = [0, 0, 2]
SetP2 = [0, 0, 8]

CstDiscretePort(mws, PortNumber, SetP1, SetP2)

for monitorindex in np.arange(0.5, 4, 0.5):
    CstDefineEfieldMonitor(mws, 'e-field' + str(monitorindex), monitorindex)
    CstDefineFarfieldMonitor(mws, 'farfield' + str(monitorindex), monitorindex)

CstSaveProject(mws)
CstDefineTimedomainSolver(mws, -30)

frequencies_list, [y_real, y_imag], y_list, [x_label, y_label, plot_title] = CstResultParameters(mws, parent_path=r'1D Results\S-Parameters', run_id=0, result_id=0)


export_file_path = 'E:\\demo\\monopole_multi_demo.txt'
CstExportTouchstone(mws, export_file_path)

cst.Quit()