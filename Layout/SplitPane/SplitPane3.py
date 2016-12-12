import java
import sys
from   java.awt import EventQueue
from   javax.swing import JButton
from   javax.swing import JFrame
from   javax.swing import JSplitPane


class SplitPane3(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'SplitPane3',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        frame.add(JSplitPane(
            JSplitPane.VERTICAL_SPLIT,
            JButton('Top'),
            JSplitPane(
                JSplitPane.HORIZONTAL_SPLIT,
                JButton('Left'),
                JButton('Right'),
            )
        )
        )
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(SplitPane3())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
