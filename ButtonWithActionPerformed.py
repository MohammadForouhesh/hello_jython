import java
import sys
from java.awt import EventQueue
from java.lang import Runnable
from javax.swing import JButton
from javax.swing import JFrame


class ButtonWithActionPerformed(Runnable):
    def run(self):
        frame = JFrame('ButtonDemo_03')
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        button = frame.add(JButton('Press me'))
        button.actionPerformed = self.buttonPressed
        frame.pack()
        frame.setVisible(1)

    def buttonPressed(self, e):
        print e
        print 'button pressed'


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(ButtonWithActionPerformed())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
