import java
import sys
from java.awt import BorderLayout
from java.awt import Dimension
from java.awt import EventQueue
from javax.swing import JButton
from javax.swing import JFrame


class BorderLayoutGap(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'BorderLayoutGap',
            layout=BorderLayout(16, 8),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )

        data = [
            BorderLayout.NORTH,
            BorderLayout.SOUTH,
            BorderLayout.EAST,
            BorderLayout.WEST
        ]

        for pos in data:
            frame.add(JButton(pos), pos)

        big = JButton(
            font=("Arabic", 40, 40),
            text="Center",
            preferredSize=Dimension(256, 128)
        )
        frame.add(big, BorderLayout.CENTER)

        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(BorderLayoutGap())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
