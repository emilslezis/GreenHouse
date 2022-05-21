# Module imports
import viz
import vizact
import vizshape
import vizinfo
import viztask
import vizfx

# Set basic settinga
viz.go(viz.FULLSCREEN)
viz.setMultiSample(4)
viz.fov(60)

# Launch Vizard
viz.go()

# Define variables

# define scene
scene = vizfx.addChild('./assets/house.osgb')
scene.setPosition([0, 0, 0])
scene.setScale([0.01, 0.01, 0.01])
viz.clearcolor(viz.SKYBLUE)

# Define lamp
lamp = viz.addChild('./assets/table lamp_light_up.osgb')
lamp.setPosition([10, 8.5, -46])
lamp.setScale([1, 1, 1])

# Define TV
tv = viz.addChild('./assets/flat-screen-tv.osgb')
tv.setPosition([120 , 12, -22.5])
tv.setScale([700, 700, 700])
tv.setAxisAngle( [0, 1, 0 , 90] )

# Define car keys
carKeys = viz.addChild('./assets/bmw-car-keys.osgb')
carKeys.setPosition([39, 9.5, -7])
carKeys.setScale([0.001, 0.001, 0.001])

# Define outlet
outlet = viz.addChild('./assets/electrical-outlet.osgb')
outlet.setPosition([72, 5, 0])
outlet.setScale([0.003, 0.003, 0.003])

# Define sneakers
sneakers = viz.addChild('./assets/sneakers.osgb')
sneakers.setPosition([73 , 0, -45])
sneakers.setScale([0.2, 0.2, 0.2])

# Define soap
soap = viz.addChild('./assets/soap.osgb')
soap.setPosition([24, 9.2, -7])
soap.setScale([0.1, 0.1, 0.1])

# Define pot
pot = viz.addChild('./assets/pot.osgb')
pot.setPosition([20, 8.5, -46])
pot.setScale([0.1, 0.1, 0.1])

#Add a model to represent the tool
arrow = vizshape.addArrow(length=0.2, color = viz.ORANGE)

#Initialize the Highlighter and items that can be highlighted
from tools import highlighter
tool = highlighter.Highlighter()
tool.setItems([lamp, tv, carKeys, outlet, sneakers, soap, pot])

panel = vizinfo.InfoPanel('',align=viz.ALIGN_CENTER,fontSize=22,icon=False,key=None)
panel.visible(0)

# update code for highlighter
def updateHighlighter(tool):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        tool.highlight()
    else:
        tool.clear()
        panel.visible(0)
        
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

status_bar = viz.addTexQuad(parent=viz.ORTHO)
status_bar.color(viz.BLACK)
status_bar.alpha(0.5)
status_bar.alignment(viz.ALIGN_LEFT_BOTTOM)
status_bar.drawOrder(-1)
viz.link(viz.MainWindow.LeftTop,status_bar,offset=[0,-80,0])
viz.link(viz.MainWindow.WindowSize,status_bar,mask=viz.LINK_SCALE)

#Registera callback function for the highlight event
def onHighlight(e):  
        
    # Customize panel for each of the items
    
    if e.new == lamp:
        panel.visible(1)
        panel.setTitle("Lampa")
        panel.setText("ja nelietojiet lampu, izslēdziet to! Aptuveni 65% eletrības katru gadu tiek lieki iztērēta, jo tiek lieki atstāta gaisma")
        
    elif e.new == tv:
        panel.visible(1)
        panel.setTitle("Televizors")
        panel.setText("Atstāj ieslēgtas tikai tās ierīces ar kurām tagad strādā. Ieslēgts televizors nepalīdzēs ne dabai, ne tavam maciņam.")
        
    elif e.new == carKeys:
        panel.visible(1)
        panel.setTitle("Automašīnas atslēgas")
        panel.setText("Maziem attālumiem izvēlies pārvietoties ar velosipēdu un izmanto sabiedriskos transtsportlīdzekļus, ja iespējams. 2021. gadā eletriskās mašīnas lietotāji izvairījās no 8.4 miljoniem tonnu CO2")
        
    elif e.new == outlet:
        panel.visible(1)
        panel.setTitle("Elektriskā rozete")
        panel.setText("Atslēdzot nelietotās ierīces no kontaktligzdas var ietaupīt līdz pat 44 centiem stundā.")
        
    elif e.new == sneakers:
        panel.visible(1)
        panel.setTitle("Apavi")
        panel.setText("Apģērba izvēlē jāizraugās, lai tas ir izveidots no videi draudzīgiem materiāliem. Ar apģērba daudzumu arī nevajag pārspīlēt.")
        
    elif e.new == soap:
        panel.visible(1)
        panel.setTitle("Trauku mazgājamais līdzeklis")
        panel.setText("Lai pasargātu vidi ir jāizmanto videi draudzīgas ziepes, kas izgatavotas no naturāliem materiāliem. Tās nekaitē ne tev ne dabai.")
        
    elif e.new == pot:
        panel.visible(1)
        panel.setTitle("Augs podā")
        panel.setText("Stādiet un audzējiet paši savus dārzeņus un augļus! Pašizaudzēti augi gan uzlabo apkārtējo vidi, gan rada prieku.")
    
viz.callback(highlighter.HIGHLIGHT_EVENT, onHighlight, )

import vizcam
vizcam.FlyNavigate()

#Hide the mouse cursor
viz.mouse.setVisible(viz.OFF)


# WASD movment
tracker = vizcam.addWalkNavigate(moveScale=10.0)
tracker.setPosition([75 , 15, -40])
viz.link(tracker,viz.MainView)
viz.mouse.setVisible(False)
