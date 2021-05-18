def CstDefineUnits(mws, Geometry, Frequency, Time, TemperatureUnit, Voltage, Current, Resistance, Conductance,
                   Capacitance, Inductance):
    units = mws.Units

    units.Geometry(Geometry)
    units.Frequency(Frequency)
    units.TemperatureUnit(TemperatureUnit)
    units.Time(Time)
    units.Voltage(Voltage)
    units.Current(Current)
    units.Resistance(Resistance)
    units.Conductance(Conductance)
    units.Capacitance(Capacitance)
    units.Inductance(Inductance)
