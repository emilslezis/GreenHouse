import viz
import vizact
import vizinfo
import vizcam
import vizfx

viz.setMultiSample(4)
viz.fov(60)
viz.go(viz.FULLSCREEN)

viz.clearcolor(viz.SKYBLUE)

soccerball = viz.addChild('soccerball.osgb')
basketball = viz.addChild('basketball.osgb')
volleyball = viz.addChild('volleyball.osgb')

 
soccerball.setPosition([-0.5,2,1.5])
basketball.setPosition([0,2,1.5])
volleyball.setPosition([0.5,2,1.5])

info = vizinfo.InfoPanel('Test description', align=viz.ALIGN_RIGHT_TOP, icon=False)
info.visible(0)

viz.mouse(viz.OFF)
object = viz.pick()

# Test keyboard movement
#tracker = vizcam.addWalkNavigate(moveScale=2.0)
#tracker.setPosition([0,1.8,0])
#viz.link(tracker,viz.MainView)
#viz.mouse.setVisible(False)

def pickObject():
    object = viz.pick()
    if object.valid():
        pos = object.getPosition()

        info.visible(1)

        if object.valid and object == soccerball:
          info.setTitle("Soccerball")

        if object.valid and object == basketball:
          info.setTitle("Basketball")

        if object.valid and object == volleyball:
          info.setTitle("Volleyball")
       
    else:
      info.visible(0)

vizact.onmousedown(viz.MOUSEBUTTON_LEFT, pickObject)