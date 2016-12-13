import java
import sys
from   java.awt import EventQueue
from   java.awt import FlowLayout
from   javax.swing import JFrame
from   javax.swing import JLabel
from   javax.swing import JToggleButton


class ToggleButton(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'Toggle Button',
            layout=FlowLayout(),
            size=(275, 85),
            font=("Comic Sans MS", 30, 30),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )

        button = JToggleButton(  # Make a toggle button
            'Off',  # Initial button text
            font=("Comic Sans MS", 30, 30),
            itemStateChanged=self.toggle  # Event handler
        )

        frame.add(button)
        frame.setVisible(1)

    def toggle(self, event):
        button = event.getItem()
        button.setText(['Off', 'On'][button.isSelected()])
        print(int(button.isSelected()))


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(ToggleButton())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
