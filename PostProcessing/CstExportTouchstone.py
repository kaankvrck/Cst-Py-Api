def CstExportTouchstone(mws, exportpath):
    touchstone = mws.TOUCHSTONE

    touchstone.Reset()
    touchstone.FileName(exportpath)
    touchstone.Impedance('50')
    #touchstone.Format(format)
    touchstone.FrequencyRange('full')
    touchstone.Renormalize('True')
    touchstone.UseARResults('False')
    touchstone.SetNSamples('1001')
    touchstone.Write()