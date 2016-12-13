import java
import sys
from   java.awt import EventQueue
from   java.awt import FlowLayout
from   javax.swing import JFormattedTextField
from   javax.swing import JFrame
from   javax.swing import JSpinner
from   javax.swing import SpinnerDateModel


class Spinner4(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'Spinner4',
            layout=FlowLayout(),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        frame.add(
            JSpinner(
                SpinnerDateModel(
                ),
                font = ("Comic Sans MS", 30, 30)
        )
        )
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(Spinner4())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
