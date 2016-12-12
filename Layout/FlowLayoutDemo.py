import java
import sys
from   java.awt import ComponentOrientation
from   java.awt import EventQueue
from   java.awt import FlowLayout
from   javax.swing import JButton
from   javax.swing import JFrame


class FlowLayoutDemo(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'FlowLayout',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )

        cp = frame.getContentPane()
        cp.setLayout(FlowLayout())  # FlowLayout.CENTER  is the default value
        for name in '1,two,Now is the time...'.split(','):
            frame.add(JButton(name, font=("Arabic", 30, 30)))
        frame.setSize(700, 200)
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(FlowLayoutDemo())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
