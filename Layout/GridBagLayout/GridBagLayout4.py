import sys

import java
from   java.awt import EventQueue
from   java.awt import GridBagConstraints
from   java.awt import GridBagLayout
from   javax.swing import JButton
from   javax.swing import JFrame


class GridBagLayout4(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'GridBagLayout4',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )

        self.addComponents(frame.getContentPane())

        frame.pack()
        print frame.getSize()
        frame.setSize(475, 210)
        frame.setVisible(1)

    def addComponents(self, container):
        container.setLayout(GridBagLayout())

        c = GridBagConstraints()
        c.gridx = 0  # first column
        c.gridy = 0  # first row
        container.add(JButton('1'), c)

        c = GridBagConstraints()
        c.gridx = 1  # second column
        c.gridy = 1  # second row
        container.add(JButton('2'), c)

        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.gridx = 2  # third column
        c.gridy = 2  # third row
        c.ipadx = 64  # specify (don't default) width
        c.weightx = 0.0
        c.gridwidth = 3
        container.add(JButton('3 being the third number'), c)

        c = GridBagConstraints()
        c.gridx = 1  # second column
        c.gridy = 3  # forth  row
        c.ipady = 32  # make this one taller
        container.add(JButton('Four shalt thou not count'), c)

        c = GridBagConstraints()
        c.gridx = 1  # second column
        c.gridy = 4  # fifth  row
        c.gridwidth = 3  # make this one 3 columns wide
        container.add(JButton('Five is right out'), c)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(GridBagLayout4())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
