def CstExportSparametersTXT(mws, exportpath):
    selectTreeItem = mws.SelectTreeItem('1D Results\S-Parameters\S1,1')
    ASCIIExport = mws.ASCIIExport

    ASCIIExport.Reset()
    ASCIIExport.SetVersion('2010')
    ASCIIExport.FileName(exportpath)
    ASCIIExport.Execute()
