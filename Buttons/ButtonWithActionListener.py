import java
import sys
from java.awt import EventQueue
from java.awt.event import ActionListener
from java.lang import Runnable
from javax.swing import JButton
from javax.swing import JFrame


class ButtonWithActionListener(Runnable, ActionListener):
    def run(self):
        frame = JFrame('ButtonDemo_02')
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        button = frame.add(JButton('Press me'))
        button.addActionListener(self)
        frame.pack()
        frame.setVisible(1)

    def actionPerformed(self, e):
        print 'button pressed'


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(ButtonWithActionListener())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
