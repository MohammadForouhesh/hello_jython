import java
import sys
from java.awt import BorderLayout
from java.awt import EventQueue
from java.awt.event import ActionListener
from java.lang import Runnable
from javax.swing import JButton
from javax.swing import JFrame
from javax.swing import JLabel


class ButtonWithLabel(Runnable):
    def run(self):
        frame = JFrame('ButtonDemo_04')
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        button = frame.add(JButton(font=("Arabic", 30, 30), text='Press me'))
        button.actionPerformed = self.buttonPressed
        self.label = JLabel(font=("Arabic", 30, 30), text='button press pending')
        frame.add(self.label, BorderLayout.SOUTH)
        frame.pack()
        frame.setVisible(1)

    def buttonPressed(self, e):
        self.label.setText('button pressed')


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(ButtonWithLabel())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
