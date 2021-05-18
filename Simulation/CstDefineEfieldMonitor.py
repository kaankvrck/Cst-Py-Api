def CstDefineEfieldMonitor(mws, Efieldname, frequency):
    monitor = mws.Monitor

    monitor.Reset()
    monitor.Name(Efieldname)
    monitor.Dimension('Volume')
    monitor.Domain('Frequency')
    monitor.FieldType('Efield')
    monitor.Frequency(str(frequency))
    monitor.UseSubvolume('False')
    monitor.SetSubvolume('-53.310273111111', '53.310273111111', '-53.310273111111', '53.310273111111',
                         '-33.310273111111', '71.310273111111')
    monitor.Create()
