import java
import sys

from   java.awt import EventQueue

from   javax.swing import Box
from   javax.swing import JButton
from   javax.swing import JFrame
from   javax.swing import JLabel
from   javax.swing import JSeparator


class vBox(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'verticalBox',
            locationRelativeTo=None,
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        box = Box.createVerticalBox()
        box.add(Box.createGlue())
        box.add(JLabel('<---- Top ---->', font=("Vivaldi", 30, 30)))
        box.add(Box.createVerticalStrut(5))
        box.add(JSeparator())
        box.add(Box.createVerticalStrut(5))
        box.add(JLabel('<---- Mid ---->', font=("Vivaldi", 30, 30)))
        box.add(Box.createVerticalStrut(5))
        box.add(JSeparator())
        box.add(Box.createVerticalStrut(5))
        box.add(JLabel('<---- Bot ---->', font=("Vivaldi", 30, 30)))
        box.add(Box.createGlue())

        frame.add(box)
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(vBox())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
