import viz
import vizact
import vizfx
import vizcam
import vizshape
import vizinfo

viz.setMultiSample(4)
viz.fov(60)
viz.go(viz.FULLSCREEN)

viz.clearcolor(viz.SKYBLUE)
#viz.MainView.collision(viz.ON)


#arrow = vizshape.addArrow(length=0.2, color = viz.ORANGE)
#arrowLink = viz.link(mouseTracker,arrow)

scene = vizfx.addChild('LIVING.osgb')
scene.setPosition([0, 0, 0])
scene.setScale([0.01, 0.01, 0.01])

viz.mouse(viz.ON)
viz.mouse.setVisible(viz.ON)
viz.mouse.setCursor(viz.mouse.CURSOR_CROSS)

soccerball = vizfx.addChild('soccerball.osgb')
soccerball.collideBox()
soccerball.setPosition([80 , 15, -40])
soccerball.setScale([10, 10, 10])

tracker = vizcam.addWalkNavigate(moveScale=10.0)
tracker.setPosition([75 , 15, -40])
viz.link(tracker,viz.MainView)
viz.mouse.setVisible(False)

info = vizinfo.InfoPanel('Test description', align=viz.ALIGN_RIGHT_TOP, icon=False)
info.visible(0)

def pickObject():
    object = viz.pick()
    if object.valid():
        pos = object.getPosition()

        info.visible(1)

        if object.valid and object == soccerball:
          info.setTitle("Soccerball")
       
    else:
      info.visible(0)

vizact.onmousedown(viz.MOUSEBUTTON_LEFT, pickObject)