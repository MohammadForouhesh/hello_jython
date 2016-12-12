import java
import sys
from   java.awt import EventQueue
from   javax.swing import JButton
from   javax.swing import JFrame
from   javax.swing import JSplitPane


class SplitPane4(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'SplitPane4',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        button = self.button
        frame.add(
            JSplitPane(
                JSplitPane.VERTICAL_SPLIT,
                button('Top'),
                JSplitPane(
                    JSplitPane.HORIZONTAL_SPLIT,
                    button('Left'),
                    button('Right'),
                )
            )
        )
        frame.pack()
        frame.setVisible(1)

    def button(self, text):
        return JButton(text, font=("Vivaldi", 30, 30), actionPerformed=self.debug)

    def debug(self, event):
        b = event.getSource()
        print '\n%6s:' % b.getActionCommand(),
        s = b.getSize()
        print 'current %3d %3d' % (s.width, s.height),
        s = b.getMinimumSize()
        print 'min %3d %3d' % (s.width, s.height),
        s = b.getMaximumSize()
        print 'max %3d %3d' % (s.width, s.height),
        s = b.getPreferredSize()
        print 'preferred %3d %3d' % (s.width, s.height),


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(SplitPane4())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
