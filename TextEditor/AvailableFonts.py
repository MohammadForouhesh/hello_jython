import java
import sys

from   java.awt import EventQueue
from   java.awt import GraphicsEnvironment

from   javax.swing import JFrame
from   javax.swing import JTextArea
from   javax.swing import JScrollPane


class AvailableFonts(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'Available Fonts',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        lge = GraphicsEnvironment.getLocalGraphicsEnvironment()
        fontNames = lge.getAvailableFontFamilyNames()

        # The JTextArea will be used to hold the names of the available fonts.
        # Unfortunately, we don't know, for certain, how many font names are
        # present.  So, we need to have the JTextArea be within a JScrollPane,
        # "just in case" too many names exist for us to display at one time.
        frame.add(
            JScrollPane(
                JTextArea(
                    '\n'.join(fontNames),
                    font=("Comic Sans MS", 30, 30),
                    editable=0,
                    rows=8,
                    columns=32
                )
            )
        )

        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(AvailableFonts())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
