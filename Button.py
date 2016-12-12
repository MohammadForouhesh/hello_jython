import java
import sys
from java.awt import EventQueue
from javax.swing import JButton
from javax.swing import JFrame


class Button(java.lang.Runnable):
    def run(self):
        frame = JFrame('Title')
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        frame.add(JButton('Press me'))
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(Button_01())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
