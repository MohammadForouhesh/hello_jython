import sys

import java
from java.awt import EventQueue
from java.awt import GridBagConstraints
from java.awt import GridBagLayout
from javax.swing import JButton
from javax.swing import JFrame


class GridBagLayout2(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'GridBagLayout2',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )

        self.addComponents(frame.getContentPane())

        frame.setSize(410, 190)
        frame.setVisible(1)

    def addComponents(self, container):
        container.setLayout(GridBagLayout())

        names = '1,2,3 being the third number'.split(',')
        for col in range(len(names)):
            c = GridBagConstraints()
            c.gridx = col  # gridx is the grid column
            c.gridy = col  # gridy is the grid row #
            container.add(JButton(names[col]), c)

        c = GridBagConstraints()
        c.gridx = 1
        c.gridy = 3  # put this one on the next row
        c.ipady = 32  # make this one taller
        container.add(JButton('Four shalt thou not count'), c)

    def buttonPress(self, event):
        print event


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(GridBagLayout2())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
