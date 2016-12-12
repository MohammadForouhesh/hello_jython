import java
import sys

from java.awt import Color
from java.awt import FlowLayout
from java.awt import EventQueue

from java.awt.event import ItemEvent
from java.awt.event import ItemListener
from java.awt.event import MouseEvent

from javax.swing import JButton
from javax.swing import JCheckBox
from javax.swing import JComponent
from javax.swing import JFrame
from javax.swing import JMenu
from javax.swing import JMenuBar
from javax.swing import JMenuItem
from javax.swing import SwingUtilities

from javax.swing.event import MouseInputAdapter


class GlassPaneDemo(java.lang.Runnable):
    def run(self):
        frame = JFrame('GlassPaneDemo')
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        # -----------------------------------------------------------------------
        changeButton = JCheckBox('Glass pane "visible"')
        changeButton.setSelected(0)
        # -----------------------------------------------------------------------
        contentPane = frame.getContentPane()
        contentPane.setLayout(FlowLayout())
        contentPane.add(changeButton)
        contentPane.add(JButton('Button 1'))
        contentPane.add(JButton('Button 2'))
        # -----------------------------------------------------------------------
        menuBar = JMenuBar()
        menu = JMenu('Menu')
        menu.add(JMenuItem('Do nothing'))
        menuBar.add(menu)
        frame.setJMenuBar(menuBar)

        # -----------------------------------------------------------------------
        myGlassPane = MyGlassPane(changeButton, menuBar, contentPane)
        changeButton.addItemListener(myGlassPane)
        frame.setGlassPane(myGlassPane)

        frame.pack()
        frame.setVisible(1)


class CBListener(MouseInputAdapter):
    def __init__(self, liveButton, menuBar, glassPane, contentPane):
        self.liveButton = liveButton
        self.menuBar = menuBar
        self.glassPane = glassPane
        self.contentPane = contentPane

    def mouseMoved(self, e):
        self.redispatchMouseEvent(e, 0)

    def mouseDragged(self, e):
        self.redispatchMouseEvent(e, 0)

    def mouseClicked(self, e):
        self.redispatchMouseEvent(e, 0)

    def mouseEntered(self, e):
        self.redispatchMouseEvent(e, 0)

    def mouseExited(self, e):
        self.redispatchMouseEvent(e, 0)

    def mousePressed(self, e):
        self.redispatchMouseEvent(e, 0)

    def mouseReleased(self, e):
        self.redispatchMouseEvent(e, 1)

    # A basic implementation of redispatching events.
    def redispatchMouseEvent(self, e, repaint):
        glassPanePoint = e.getPoint()
        container = self.contentPane
        containerPoint = SwingUtilities.convertPoint(
            self.glassPane,
            glassPanePoint,
            self.contentPane
        )

        if containerPoint.y < 0:  # we're not in the content pane
            if containerPoint.y + self.menuBar.getHeight() >= 0:
                # The mouse event is over the menu bar. Could handle specially.
                pass
            else:
                pass
        else:
            # The mouse event is probably over the content pane.
            # Find out exactly which component it's over.
            component = SwingUtilities.getDeepestComponentAt(
                container,
                containerPoint.x,
                containerPoint.y
            )

            if component and component == self.liveButton:
                # Forward events over the check box.
                componentPoint = SwingUtilities.convertPoint(
                    self.glassPane,
                    glassPanePoint,
                    component
                )
                component.dispatchEvent(MouseEvent(component,
                                                   e.getID(),
                                                   e.getWhen(),
                                                   e.getModifiers(),
                                                   componentPoint.x,
                                                   componentPoint.y,
                                                   e.getClickCount(),
                                                   e.isPopupTrigger()
                                                   )
                                        )

        # Update the glass pane if requested.
        if repaint:
            self.glassPane.setPoint(glassPanePoint)
            self.glassPane.repaint()


class MyGlassPane(JComponent, ItemListener):
    # React to change button clicks.
    def itemStateChanged(self, e):
        self.setVisible(e.getStateChange() == ItemEvent.SELECTED)

    def paintComponent(self, g):
        if self.point:
            g.setColor(Color.red)
            g.fillOval(self.point.x - 10, self.point.y - 10, 20, 20)

    def setPoint(self, p):
        self.point = p

    def __init__(self, aButton, menuBar, contentPane):
        self.point = None
        listener = CBListener(aButton, menuBar, self, contentPane)
        self.addMouseListener(listener)
        self.addMouseMotionListener(listener)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(GlassPaneDemo())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application: ')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
