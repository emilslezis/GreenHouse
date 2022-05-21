import viz

viz.go(viz.FULLSCREEN)
viz.MainWindow.fov(60)

piazza = viz.addChild('piazza.osgb')

#lightbulb = viz.addChild('export.osgb')
#lightbulb.setPosition([4, 0, 6])
#lightbulb.setScale([0.1, 0.08, 0.1])

lightbulb = viz.addChild('./assets/table lamp_light_up.osgb')
lightbulb.setPosition([4, 0, 6])
lightbulb.setScale([0.1, 0.08, 0.1])

lightbulb2 = viz.addChild('./assets/table lamp.osgb')
lightbulb2.setPosition([2, 0, 6])
lightbulb2.setScale([0.1, 0.08, 0.1])