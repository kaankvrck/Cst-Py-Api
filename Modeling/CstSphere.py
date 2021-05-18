def CstSphere(mws, Name, component, material, Axis, CenterRadius, TopRadius, BottomRadius, Center):
    sphere = mws.Sphere

    sphere.Reset
    sphere.Name(Name)
    sphere.Component(component)
    sphere.Material(material)
    sphere.Axis(Axis)
    sphere.CenterRadius(str(CenterRadius))
    sphere.TopRadius(str(TopRadius))
    sphere.BottomRadius(str(BottomRadius))
    sphere.Center(str(Center(0)), str(Center(1)), str(Center(2)))
    sphere.Segments('0')
    sphere.Create
