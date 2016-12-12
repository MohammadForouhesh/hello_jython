import java
import sys
from java.awt import BorderLayout
from java.awt import Dimension
from java.awt import EventQueue
from javax.swing import JButton
from javax.swing import JFrame


class BorderLayoutDemo(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'BorderLayout',
            layout=BorderLayout(),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )

        data = [
            ['PAGE_START', BorderLayout.PAGE_START],
            ['PAGE_END', BorderLayout.PAGE_END],
            ['LINE_START', BorderLayout.LINE_START],
            ['LINE_END', BorderLayout.LINE_END],
        ]

        for name, pos in data:
            frame.add(JButton(name), pos)

        big = JButton(
            'CENTER',
            preferredSize=Dimension(256, 128)
        )
        frame.add(big, BorderLayout.CENTER)

        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(BorderLayoutDemo())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
