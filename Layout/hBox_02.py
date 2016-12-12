import java
import sys

from   java.awt import EventQueue

from   javax.swing import Box
from   javax.swing import JButton
from   javax.swing import JFrame
from   javax.swing import JLabel


class hBox(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'horizontalBox',
            locationRelativeTo=None,
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        box = Box.createHorizontalBox()
        box.add(Box.createGlue())
        box.add(JLabel(font=("Vivaldi", 30, 30),text='<---- Left ---->'))
        box.add(Box.createHorizontalStrut(5))
        box.add(JLabel(font=("Vivaldi", 30, 30),text='<---- Middle ---->'))
        box.add(Box.createHorizontalStrut(5))
        box.add(JLabel(font=("Vivaldi", 30, 30),text='<---- Right ---->'))
        box.add(Box.createGlue())

        frame.add(box)
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(hBox())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
