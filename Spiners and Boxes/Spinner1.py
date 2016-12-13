import java
import sys
from   java.awt import EventQueue
from   java.awt import FlowLayout
from   java.text import DateFormatSymbols as DFS
from   javax.swing import JFormattedTextField
from   javax.swing import JFrame
from   javax.swing import JSpinner
from   javax.swing import SpinnerListModel


class Spinner1(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'Spinner1',
            layout=FlowLayout(),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        daysOfWeek = [dow for dow in DFS().getWeekdays() if dow]
        frame.add(JSpinner(SpinnerListModel(daysOfWeek), font=("Comic Sans MS", 30, 30)))
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(Spinner1())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
