import java
import sys
from   java.awt import EventQueue
from   java.awt import FlowLayout
from   java.util import Date
from   java.util import Calendar
from   javax.swing import JFormattedTextField
from   javax.swing import JFrame
from   javax.swing import JSpinner
from   javax.swing import SpinnerDateModel


class Spinner5(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'Spinner5',
            layout=FlowLayout(),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        frame.add(
            JSpinner(
                SpinnerDateModel(
                    Date(2000, 2, 1),  # zero origin month
                    None,  # minimum
                    None,  # maximum
                    Calendar.DAY_OF_MONTH  # Ignored by GUI
                ),
                font=("Comic Sans MS", 30, 30)
            )
        )
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(Spinner5())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
