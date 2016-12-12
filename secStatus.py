import java
import sys
from java.awt import EventQueue
from javax.swing import JFrame
from javax.swing import JLabel


class SecStatus(java.lang.Runnable):
    def run(self):
        frame = JFrame('Global Security')
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        security = AdminConfig.list('Security')
        status = AdminConfig.showAttribute(security, 'enabled')
        frame.add(JLabel('Security enabled: ' + status))
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    if 'AdminConfig' in dir():
        EventQueue.invokeLater(SecStatus())
        raw_input('\nPress <Enter> to terminate the application: ')
    else:
        print 'Error: This script must be executed by the WebSphere Application'
        print '       Server wsadmin utility.\n'
        print 'wsadmin -f SecStatus.py'
else:
    print 'Error: This script should be executed, not imported.\n'
    if 'JYTHON_JAR' in dir(sys):
        print 'Error: This script must be executed by the WebSphere Application'
        print '       Server wsadmin utility.\n'
    print 'Usage: wsadmin -f %s.py' % __name__
    sys.exit()
