import java
import sys
from java.awt import EventQueue
from javax.swing import JButton
from javax.swing import JFrame


class AbsoluteLayout(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'AbsoluteLayout',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        frame.setLayout(None)
        data = [
            ['A', 20, 10, 0, 0],
            ['B', 40, 40, 10, 10],
            ['C', 80, 20, 20, 20]]

        insets = frame.getInsets()
        for item in data:
            button = frame.add(JButton(item[0]))
            size = button.getPreferredSize()
            button.setBounds(
                insets.left + item[1],
                insets.top + item[2],
                size.width + item[3],
                size.height + item[4]
            )
        frame.setSize(
            300 + insets.left + insets.right,  # frame width
            150 + insets.top + insets.bottom  # frame height
        )
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(AbsoluteLayout())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
