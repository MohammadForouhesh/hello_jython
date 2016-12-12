import java
import sys
from java.awt import Component
from java.awt import EventQueue
from javax.swing import BoxLayout
from javax.swing import JButton
from javax.swing import JFrame
from javax.swing import JPanel
from javax.swing import JTabbedPane


class BoxLayoutDemo(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'BoxLayoutDemo',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )

        self.addTabs(frame.getContentPane())

        frame.setSize(600, 350)
        frame.setVisible(1)

    def addTabs(self, container):
        align = [
            ['Left', Component.LEFT_ALIGNMENT],
            ['Center', Component.CENTER_ALIGNMENT],
            ['Right', Component.RIGHT_ALIGNMENT]
        ]

        names = '1,2,3 being the third number'.split(',')
        tabs = JTabbedPane(font=("Arabic", 30, 320))
        for aName, aConst in align:
            tab = JPanel()
            tab.setLayout(BoxLayout(tab, BoxLayout.Y_AXIS))
            for name in names:
                tab.add(JButton(name,font=("Arabic", 40, 40), alignmentX=aConst))
            tabs.addTab(aName, tab)

        container.add(tabs)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(BoxLayoutDemo())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
