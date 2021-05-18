def Cstbrick(mws, Name, component, material, Xrange, Yrange, Zrange):
    brick = mws.Brick

    brick.Reset()
    brick.Name(Name)
    brick.component(component)
    brick.Material(material)
    brick.Xrange(str(Xrange[0]), str(Xrange[1]))
    brick.Yrange(str(Yrange[0]), str(Yrange[1]))
    brick.Zrange(str(Zrange[0]), str(Zrange[1]))
    brick.Create
    format(brick)
