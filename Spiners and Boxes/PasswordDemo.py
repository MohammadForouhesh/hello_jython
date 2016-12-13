import jarray
import java
import sys
from   java.awt import EventQueue
from   java.awt import FlowLayout
from   javax.swing import JFrame
from   javax.swing import JLabel
from   javax.swing import JPasswordField


class PasswordDemo(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'PasswordDemo',
            size=(430, 200),
            layout=FlowLayout(),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        frame.add(JLabel('Password:', font=("Comic Sans MS", 30, 30)))
        self.pwd = frame.add(
            JPasswordField(
                10,
                actionPerformed=self.enter,
                font=("Comic Sans MS", 30, 30)
            )
        )
        self.msg = frame.add(JLabel(font=("Comic Sans MS", 30, 30)))
        frame.setVisible(1)

    def enter(self, event):
        print 'ActionCommand: "%s"' % event.getActionCommand()
        pwd = self.pwd.getPassword()
        if pwd == jarray.array('test', 'c'):
            result = 'correct'
        else:
            result = 'wrong!'
        self.msg.setText('Password is %s' % result)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(PasswordDemo())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
