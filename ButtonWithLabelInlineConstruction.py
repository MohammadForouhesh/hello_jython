import java
import sys
from java.awt import BorderLayout
from java.awt import EventQueue
from java.lang import Runnable
from javax.swing import JButton
from javax.swing import JFrame
from javax.swing import JLabel


class ButtonWithLabelInlineConstruction(Runnable):
    def run(self):
        frame = JFrame(
            'ButtonDemo_04',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        frame.add(
            JButton(
                font=("Arabic", 30, 30),
                text='Press me',
                actionPerformed=self.buttonPressed
            )
        )
        self.label = JLabel(font=("Arabic", 30, 30), text='button press pending')
        frame.add(self.label, BorderLayout.SOUTH)
        frame.pack()
        frame.setVisible(1)

    def buttonPressed(self, e):
        self.label.text = 'button pressed'


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(ButtonWithLabelInlineConstruction())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
