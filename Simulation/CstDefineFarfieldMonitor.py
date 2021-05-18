def CstDefineFarfieldMonitor(mws, Farfieldname, frequency):
    monitor = mws.Monitor

    monitor.Reset()
    monitor.Name(Farfieldname)
    monitor.Domain('Frequency')
    monitor.FieldType('Farfield')
    monitor.Frequency(str(frequency))
    monitor.UseSubvolume('False')
    monitor.ExportFarfieldSource('False')
    monitor.SetSubvolume('-53.310273111111', '53.310273111111', '-53.310273111111', '53.310273111111',
                         '-33.310273111111', '71.310273111111')
    monitor.Create()
