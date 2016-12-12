import java
import sys

from java.awt import Dimension
from java.awt import EventQueue

from javax.swing import Box
from javax.swing import JButton
from javax.swing import JFrame


class Box1(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'Box1',
            locationRelativeTo=None,
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        name = 'A'
        size = Dimension(46, 26)
        vBox = Box.createVerticalBox()
        for row in range(5):
            hBox = Box.createHorizontalBox()
            for col in range(5):
                button = JButton(name, font=("Arabic", 30, 30))

                hBox.add(button)
                self.showSizes(name, button)
                name = chr(ord(name) + 1)
            vBox.add(hBox)
        frame.add(vBox)
        frame.pack()
        frame.setVisible(1)

    def showSizes(self, name, obj):
        text = name
        size = obj.getSize()
        text += ' %2d %2d ' % (size.width, size.height)
        size = obj.getMinimumSize()
        text += ' %2d %2d ' % (size.width, size.height)
        size = obj.getMaximumSize()
        text += ' %2d %2d ' % (size.width, size.height)
        size = obj.getPreferredSize()
        text += ' %2d %2d ' % (size.width, size.height)
        print text


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(Box1())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
