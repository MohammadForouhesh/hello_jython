import java
import sys
from java.awt import EventQueue
from java.awt.event import ActionListener
from javax.swing import JButton
from javax.swing import JFrame


class ButtonPressed(ActionListener):
    def actionPerformed(self, e):
        print 'button pressed'


class ButtonExtendingActionListener(java.lang.Runnable):
    def run(self):
        frame = JFrame('ButtonDemo_01')
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        button = frame.add(JButton('Press me'))
        button.addActionListener(ButtonPressed())
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(ButtonExtendingActionListener())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
