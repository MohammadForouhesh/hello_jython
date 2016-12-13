import java
import sys
from   java.awt import EventQueue
from   java.awt import FlowLayout
from   javax.swing import ButtonGroup
from   javax.swing import JFrame
from   javax.swing import JLabel
from   javax.swing import JToggleButton


class ButtonGroupDemo(java.lang.Runnable):
    def addRB(self, pane, bg, text):
        bg.add(
            pane.add(
                JToggleButton(
                    text,
                    selected=(text == '1'),
                    itemStateChanged=self.toggle,   # event handler
                    font=("Comic Sans MS", 30, 30)
                )
            )
        )

    def run(self):
        frame = JFrame(
            'ToggleButton Group',
            layout=FlowLayout(),
            size=(500, 500),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        cp = frame.getContentPane()
        bg = ButtonGroup()
        for i in range(1, 4):
            self.addRB(cp, bg, `"TST"`)
        self.label = frame.add(JLabel('Selection: `TST`', font=("Comic Sans MS", 30, 30)))
        frame.setVisible(1)

    def toggle(self, event):
        text = event.getItem().getText()
        self.label.setText('Selection: ' + text)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(ButtonGroupDemo())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
