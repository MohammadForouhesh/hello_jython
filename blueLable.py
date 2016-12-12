import java
import sys

from   java.awt import Color
from   java.awt import Dimension
from   java.awt import EventQueue
from   javax.swing import JFrame
from   javax.swing import JLabel


class BlueLabel(java.lang.Runnable):
    def run(self):
        frame = JFrame('BlueLabel')  # Create a JFrame with a title
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)

        Label = JLabel()  # Create an empty label
        Label.setOpaque(1)  # Must be opaque for color to be seen
        Label.setBackground(Color.BLUE)  # Make the label blue
        Label.setPreferredSize(Dimension(200, 200))

        frame.getContentPane().add(Label)  # Add the label to the content pane

        frame.pack()  # Size frame to display the contents
        frame.setVisible(1)  # Finally, make the frame visible


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(BlueLabel())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application: ')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
