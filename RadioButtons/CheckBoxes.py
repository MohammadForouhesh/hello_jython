import java
import sys
from   java.awt import EventQueue
from   java.awt import FlowLayout
from   javax.swing import JCheckBox
from   javax.swing import JFrame
from   javax.swing import JLabel


class CheckBoxes(java.lang.Runnable):
    def addCB(self, pane, text):
        pane.add(
            JCheckBox(
                text,
                font=("Comic Sans MS", 30, 30),
                itemStateChanged=self.toggle    # even handler
            )
        )

    def run(self):
        frame = JFrame(
            'Check Boxes',
            layout=FlowLayout(),
            size=(350, 200),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        cp = frame.getContentPane()
        self.addCB(cp, 'TST')
        self.addCB(cp, 'BST')
        self.addCB(cp, 'TrieST')
        self.label = frame.add(JLabel('Nothing selected', font=("Comic Sans MS", 30, 30)))
        frame.setVisible(1)

    def toggle(self, event):
        cb = event.getItem()
        text = cb.getText()
        state = ['No', 'Yes'][cb.isSelected()]
        self.label.setText('%s selected? %s' % (text, state))
        print(text)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(CheckBoxes())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
