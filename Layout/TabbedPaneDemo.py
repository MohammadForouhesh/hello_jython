import java
import sys
from java.awt import EventQueue
from java.awt import BorderLayout
from javax.swing import JButton
from javax.swing import JFrame
from javax.swing import JLabel
from javax.swing import JPanel
from javax.swing import JTabbedPane


class TabbedPaneDemo(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'TabbedPaneDemo',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )

        self.addTabs(frame.getContentPane())

        frame.setSize(900, 525)
        frame.setVisible(1)

    def addTabs(self, container):
        tab1 = JPanel()
        tab1.add(
            JLabel(
                'The quick brown fox jumped over the lazy dog.'
                , font=("Comic Sans MS", 30, 30)
            )
        )

        tab2 = JPanel()
        for name in 'A,B,C'.split(','):
            tab2.add(JButton(name, font=("Comic Sans MS", 30, 30)))

        tab3 = JPanel()
        tab3.add(
            JLabel(
                'Now is the time for all good men to come to...'
                , font=("Comic Sans MS", 30, 30)
            )
        )

        tabs = JTabbedPane(font=("Comic Sans MS", 30, 30))
        tabs.addTab('Yek', tab1)
        tabs.addTab('Do', tab2)
        tabs.addTab('Se', tab3)

        container.add(tabs)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(TabbedPaneDemo())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
