import win32com.client
from matplotlib import pyplot as plt

from Home.CstMeshInitiator import *
from Home.CstDefineBackroundMaterial import *
from Home.CstDefaultUnits import *
from Home.CstSaveAsProject import *
from Home.CstQuitProject import *
from Materials.CstCopperAnnealedLossy import *
from Materials.CstFR4lossy import *
from Modeling.Cstbrick import *
from Modeling.CstSubtract import *
from Modeling.CstAdd import *
from Modeling.CstPickFace import *
from Simulation.CstDefineFrequencyRange import *
from Simulation.CstDefineOpenBoundary import *
from Simulation.CstWaveguidePort import *
from Simulation.CstDefineHfieldMonitor import *
from Simulation.CstDefineEfieldMonitor import *
from Simulation.CstDefineFarfieldMonitor import *
from Simulation.CstDefineTimedomainSolver import *
from PostProcessing.CstResultParameters import *
from PostProcessing.CstExportTouchstone import *

#cst = win32com.client.Dispatch("CSTStudio.Application")
#mws = cst.NewMWS()

cst = win32com.client.dynamic.Dispatch("CSTStudio.Application")
cst.SetQuietMode(True)
new_mws = cst.NewMWS()
mws = cst.Active3D()

CstDefaultUnits(mws)

CstDefineFrequencyRange(mws, 1.5, 3.5)

CstMeshInitiator(mws)

Xmin = 'expanded open'
Xmax = 'expanded open'
Ymin = 'expanded open'
Ymax = 'expanded open'
Zmin = 'expanded open'
Zmax = 'expanded open'
minfrequency = 1.5
CstDefineOpenBoundary(mws, minfrequency, Xmin, Xmax, Ymin, Ymax, Zmin, Zmax)

XminSpace = 0
XmaxSpace = 0
YminSpace = 0
YmaxSpace = 0
ZminSpace = 0
ZmaxSpace = 0
CstDefineBackroundMaterial(mws, XminSpace, XmaxSpace, YminSpace, YmaxSpace, ZminSpace, ZmaxSpace)

CstCopperAnnealedLossy(mws)
CstFR4lossy(mws)

W = 28.45
L = 28.45
Fi = 9
Wf = 1.137
Gpf = 1
Lg = 2 * L
Wg = 2 * W
Ht = 0.035
Hs = 1.6

Name = 'Groundplane'
component = 'component1'
material = 'Copper (annealed)'
Xrange = [-0.5 * Wg, 0.5 * Wg]
Yrange = [-0.5 * Lg, 0.5 * Lg]
Zrange = [0, Ht]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

Name = 'Substrate'
component = 'component1'
material = 'FR-4 (lossy)'
Xrange = [-0.5 * Wg, 0.5 * Wg]
Yrange = [-0.5 * Lg, 0.5 * Lg]
Zrange = [Ht, Ht + Hs]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

Name = 'Patch'
component = 'component1'
material = 'Copper (annealed)'
Xrange = [-W / 2, W / 2]
Yrange = [-L / 2, L / 2]
Zrange = [Ht + Hs, Ht + Hs + Ht]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

Name = 'Empty space'
component = 'component1'
material = 'Copper (annealed)'
Xrange = [-((Wf / 2) + Gpf), ((Wf / 2) + Gpf)]
Yrange = [-L / 2 + Fi, -L / 2]
Zrange = [Ht + Hs, Ht + Hs + Ht]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

component1 = 'component1:Patch'
component2 = 'component1:Empty space'
CstSubtract(mws, component1, component2)

Name = 'FeedLine'
component = 'component1'
material = 'Copper (annealed)'
Xrange = [-Wf / 2, Wf / 2]
Yrange = [-L / 2 + Fi, -Lg / 2]
Zrange = [Ht + Hs, Ht + Hs + Ht]
Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange)

component1 = 'component1:Patch'
component2 = 'component1:FeedLine'
CstAdd(mws, component1, component2)

Name = 'Substrate'
id = 3
CstPickFace(mws, Name, id)

PortNumber = 1
Xrange = [-36, 36]
Yrange = [-36, -36]
Zrange = [0.035, 1.635]
XrangeAdd = [3 * Wf, 3 * Wf]
YrangeAdd = [0, 0]
ZrangeAdd = [Ht + Hs, 4 * Hs]
Coordinates = 'Picks'
Orientation = 'positive'
CstWaveguidePort(mws, PortNumber, Xrange, Yrange, Zrange, XrangeAdd, YrangeAdd, ZrangeAdd, Coordinates, Orientation)

CstDefineEfieldMonitor(mws, ('e-field' + '2.45'), 2.45)
CstDefineHfieldMonitor(mws, ('h-field' + '2.45'), 2.45)
CstDefineFarfieldMonitor(mws, ('farfield' + '2.45'), 2.45)

CstSaveAsProject(mws, 'E:\\demo\\demo_result\\MicrostripAntenna')

CstDefineTimedomainSolver(mws, -40)

frequencies_list, [y_real, y_imag], y_list, [x_label, y_label, plot_title] = CstResultParameters(mws, parent_path=r'1D Results\S-Parameters', run_id=0, result_id=0)

plt.figure(dpi=300)
plt.plot(frequencies_list, y_real)
plt.plot(frequencies_list, y_imag)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(plot_title)
plt.show()

plt.figure(dpi=300)
plt.plot(frequencies_list, y_list)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(plot_title)
plt.show()


export_file_path = 'E:\\demo\\microstrip_demo.txt'
CstExportTouchstone(mws, export_file_path)

cst.Quit()