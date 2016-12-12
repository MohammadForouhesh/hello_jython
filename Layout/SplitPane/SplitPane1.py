
import java
import sys
from java.awt import EventQueue
from javax.swing import JButton
from javax.swing import JFrame
from javax.swing import JSplitPane


class SplitPane1(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'SplitPane1',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        frame.add(JSplitPane(
            JSplitPane.HORIZONTAL_SPLIT,
            JButton('Left', font=("Vivaldi", 30, 30)),
            JButton('Right', font=("Vivaldi", 30, 30))
        )
        )
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(SplitPane1())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
