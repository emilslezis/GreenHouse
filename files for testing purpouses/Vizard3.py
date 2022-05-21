"""  
Scroll wheel moves the arrow forward,back.  
Left mouse button draws a ray to highlight.  
Mouse movements control viewpoint orientation.  
Arrow Keys control viewpoint position.  
Space bar changes the highlight mode  
""" 

import viz
import vizact
import vizshape
import vizinfo

viz.setOption('viz.display.stencil',1)

vizinfo.InfoPanel()

viz.setMultiSample(4)
viz.fov(60)
viz.go()

environment = viz.addChild('sky_day.osgb')
soccerball = viz.addChild('soccerball.osgb',pos=[-1,1.8,2])
basketball = viz.addChild('basketball.osgb',pos=[0,1.8,2])
volleyball = viz.addChild('volleyball.osgb',pos=[1,1.8,2])

#Add a model to represent the tool
arrow = vizshape.addArrow(length=0.2, color = viz.ORANGE)

#Initialize the Highlighter and items that can be highlighted
from tools import highlighter
tool = highlighter.Highlighter()
tool.setItems([soccerball,basketball,volleyball])

# update code for highlighter
def updateHighlighter(tool):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        tool.highlight()
    else:
        tool.clear()
tool.setUpdateFunction(updateHighlighter)

#Link the highlighter to an arrow in order to
#visualize it's position
from vizconnect.util import virtual_trackers
mouseTracker = virtual_trackers.ScrollWheel(followMouse = True)
mouseTracker.distance = 0.7
arrowLink = viz.link(mouseTracker,arrow)
arrowLink.postMultLinkable(viz.MainView)
viz.link(arrowLink,tool)

#Cycle the highlight mode with the spacebar
modes = viz.cycle([highlighter.MODE_BOX, highlighter.MODE_ARROW, highlighter.MODE_OUTLINE])
def cycleMode():
    tool.setHighlightMode(modes.next())

vizact.onkeydown(' ',cycleMode)

#Register a callback function for the highlight event
def onHighlight(e):
    if e.new == soccerball:
        print('soccerball is highlighted')
    elif e.old == soccerball:
        print('soccerball is highlighted')
    
viz.callback(highlighter.HIGHLIGHT_EVENT,onHighlight)

import vizcam
vizcam.FlyNavigate()

#Hide the mouse curser
viz.mouse.setVisible(viz.OFF)