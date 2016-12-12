import sys

import java
from java.awt import EventQueue
from java.awt import GridBagConstraints
from java.awt import GridBagLayout
from javax.swing import JButton
from javax.swing import JFrame


class GridBagLayout1(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'GridBagLayout1',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )

        self.addComponents(frame.getContentPane())

        frame.setSize(300, 150)
        frame.setVisible(1)

    def addComponents(self, container):
        container.setLayout(GridBagLayout())

        c = GridBagConstraints()  # Start with the default constraints
        print '\n default constraints:'
        print '     gridx:', c.gridx
        print '     gridy:', c.gridx
        print ' gridwidth:', c.gridwidth
        print 'gridheight:', c.gridheight
        print '   weightx:', c.weightx
        print '   weighty:', c.weighty
        print '    anchor:', c.anchor
        print '      fill:', c.fill
        print '    insets:', c.insets
        print '     ipadx:', c.ipadx
        print '     ipady:', c.ipady

        names = '1,2,3 being the third number'.split(',')
        for col in range(len(names)):
            c = GridBagConstraints()
            c.fill = GridBagConstraints.HORIZONTAL
            c.gridx = col
            c.gridy = col
            container.add(JButton(names[col]), c)

    def buttonPress(self, event):
        print event


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(GridBagLayout1())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
