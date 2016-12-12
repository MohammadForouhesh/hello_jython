import java
import sys
from   java.awt import EventQueue
from   javax.swing import JFrame


class Template1:
    def __init__(self):
        frame = JFrame('Title')
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        frame.pack()
        frame.setVisible(1)


class Runnable(java.lang.Runnable):
    def __init__(self, fun):
        self.runner = fun

    def run(self):
        self.runner()


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(Runnable(Template1))
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application: ')
else:
    print '\nError: This script should be executed, not imported.\n'
    if 'JYTHON_JAR' in dir(sys):
        print 'jython %s.py' % __name__
    else:
        print 'Usage: wsadmin -f %s.py' % __name__
    sys.exit()
