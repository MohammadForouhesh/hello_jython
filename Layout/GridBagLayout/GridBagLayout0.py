import sys

import java
from java.awt import EventQueue
from java.awt import GridBagConstraints
from java.awt import GridBagLayout
from javax.swing import JButton
from javax.swing import JFrame


class GridBagLayout0(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'GridBagLayout0',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )

        self.addComponents(frame.getContentPane())

        frame.setSize(600, 300)  # Display grid & some space
        frame.setVisible(1)

    def addComponents(self, container):
        container.setLayout(GridBagLayout())

        names = '1,2,3 being the third number'.split(',')
        for col in range(len(names)):
            c = GridBagConstraints()
            container.add(JButton(names[col], font=("Arabic", 30, 30)), c)

    def buttonPress(self, event):
        print event


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(GridBagLayout0())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
