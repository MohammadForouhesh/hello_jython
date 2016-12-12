import java
import sys
from   java.awt import EventQueue
from   java.awt import GridLayout
from   javax.swing import BoxLayout
from   javax.swing import JButton
from   javax.swing import JFrame
from   javax.swing import JLabel
from   javax.swing import JPanel


class GridLayoutDemo(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'GridLayoutDemo',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )

        main = JPanel()
        main.setLayout(BoxLayout(main, BoxLayout.Y_AXIS))
        self.panes = []
        self.addButtons(main, 'Horizontal:')
        self.addButtons(main, 'Vertical:')
        frame.add(main)

        frame.setSize(1000, 1000)
        frame.setVisible(1)

    def addButtons(self, container, prefix):
        pane = JPanel(GridLayout(0, 3))
        self.panes.append(pane)
        for size in '0,2,4,8,16'.split(','):
            pane.add(
                JButton(
                    '%s %s' % (prefix, size),
                    font=("Arabic", 30, 30),
                    actionPerformed=self.buttonPress
                )
            )
        container.add(pane)

    def buttonPress(self, event):
        dir, size = event.getActionCommand().split(' ')
        if dir[0] == 'H':
            for pane in self.panes:
                layout = pane.getLayout()
                layout.setHgap(int(size))
                layout.layoutContainer(pane)
        else:
            for pane in self.panes:
                layout = pane.getLayout()
                layout.setVgap(int(size))
                layout.layoutContainer(pane)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(GridLayoutDemo())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
