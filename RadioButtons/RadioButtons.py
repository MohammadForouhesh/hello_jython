import threading

import java
import sys
from   java.awt import EventQueue
from   java.awt import FlowLayout
from   javax.swing import ButtonGroup
from   javax.swing import JFrame
from   javax.swing import JLabel
from   javax.swing import JRadioButton

counter = 0


class RadioButtons(java.lang.Runnable):
    def addRB(self, pane, bg, text):
        bg.add(
            pane.add(
                JRadioButton(
                    text,
                    font=("Comic Sans MS", 30, 30),
                    itemStateChanged=self.toggle  # evant handler
                )
            )
        )

    def run(self):
        frame = JFrame(
            'Radio Buttons',
            layout=FlowLayout(),
            size=(350, 200),
            font=("Comic Sans MS", 30, 30),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        cp = frame.getContentPane()
        bg = ButtonGroup()
        self.addRB(cp, bg, 'TST')
        self.addRB(cp, bg, 'BST')
        self.addRB(cp, bg, 'TrieST')
        self.label = frame.add(JLabel('Nothing selected', font=("Comic Sans MS", 30, 30)))
        frame.setVisible(1)

    def toggle(self, event):
        global counter
        if counter % 2 == 0:
            threading.Timer(threading.current_thread, 100)
            text = event.getItem().getText()
            self.label.setText('Selection: ' + text)
            print(text)
        counter += 1


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(RadioButtons())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
