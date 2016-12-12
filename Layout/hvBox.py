import java
import sys

from   java.awt import EventQueue

from   javax.swing import Box
from   javax.swing import JButton
from   javax.swing import JFrame


class hvBox(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'horizontalBox',
            locationRelativeTo=None,
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )

        vert = Box.createVerticalBox()
        vert.add(Box.createGlue())
        vert.add(JButton('<>', font=("Vivaldi", 30, 30)))
        vert.add(Box.createVerticalStrut(5))
        vert.add(JButton('<>', font=("Vivaldi", 30, 30)))
        vert.add(Box.createVerticalStrut(5))
        vert.add(JButton('<>', font=("Vivaldi", 30, 30)))
        vert.add(Box.createGlue())

        hor = Box.createHorizontalBox()
        hor.add(Box.createGlue())
        hor.add(JButton('<>', font=("Vivaldi", 30, 30)))
        hor.add(Box.createHorizontalStrut(5))

        hor.add(vert)

        hor.add(Box.createHorizontalStrut(5))
        hor.add(JButton('<>', font=("Vivaldi", 30, 30)))
        hor.add(Box.createGlue())

        frame.add(hor)
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(hvBox())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
