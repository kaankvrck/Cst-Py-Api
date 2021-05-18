def Cstcylinder(mws, Name, component, material, Axis, OuterRadius, InnerRadius, Xcenter, Ycenter, Zrange):
    cylinder = mws.Cylinder

    cylinder.Reset()
    cylinder.Name(Name)
    cylinder.Component(component)
    cylinder.Material(material)
    cylinder.Axis(Axis)
    cylinder.Outerradius(OuterRadius)
    cylinder.Innerradius(InnerRadius)

    if Axis == 'Z':
        cylinder.Xcenter(str(Xcenter))
        cylinder.Ycenter(str(Ycenter))
        cylinder.Zrange(str(Zrange[0]), str(Zrange[1]))
    elif Axis == 'X':
        cylinder.Ycenter(str(Ycenter))
        cylinder.Zcenter(str(Xcenter))
        cylinder.Xrange(str(Zrange[0]), str(Zrange[1]))
    elif Axis == 'Y':
        cylinder.Xcenter(str(Xcenter))
        cylinder.Zcenter(str(Ycenter))
        cylinder.Yrange(str(Zrange[0]), str(Zrange[1]))

    cylinder.Create()
    format(cylinder)
