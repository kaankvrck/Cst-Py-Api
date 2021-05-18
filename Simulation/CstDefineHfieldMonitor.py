def CstDefineHfieldMonitor(mws, Hfieldname, frequency):
    monitor = mws.Monitor

    monitor.Reset()
    monitor.Name(Hfieldname)
    monitor.Dimension('Volume')
    monitor.Domain('Frequency')
    monitor.FieldType('Hfield')
    monitor.Frequency(str(frequency))
    monitor.UseSubvolume('False')
    monitor.SetSubvolume('-209.896229', '229.896229', '-179.896229', '179.896229', '-149.896229', '187.896229')
    monitor.Create()
