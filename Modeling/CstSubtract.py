def CstSubtract(mws, component1, component2):
    solid = mws.Solid

    solid.Subtract(component1, component2)
