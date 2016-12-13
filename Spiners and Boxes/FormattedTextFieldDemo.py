import java
import sys
from   java.awt import EventQueue
from   java.awt import GridLayout
from   java.text import NumberFormat
from   javax.swing import JFormattedTextField
from   javax.swing import JFrame
from   javax.swing import JLabel


class FormattedTextFieldDemo(java.lang.Runnable):
    def addFTF(self, name):
        pane = self.frame.getContentPane()
        pane.add(JLabel(name, font=("Comic Sans MS", 30, 30)))
        pane.add(
            JFormattedTextField(
                eval('NumberFormat.' + name),
                font=("Comic Sans MS", 30, 30),
                value=12345.67890,
                columns=10
            )
        )

    def run(self):
        self.frame = frame = JFrame(
            'FormattedTextFieldDemo',
            layout=GridLayout(0, 2),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        self.addFTF('getInstance()')
        self.addFTF('getCurrencyInstance()')
        self.addFTF('getIntegerInstance()')
        self.addFTF('getNumberInstance()')
        self.addFTF('getPercentInstance()')
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(FormattedTextFieldDemo())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
