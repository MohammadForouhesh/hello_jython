import java
import sys

from java.awt import Dimension
from java.awt import EventQueue
from java.awt import Toolkit

from javax.swing import Box
from javax.swing import JButton
from javax.swing import JFrame
from javax.swing import JLabel
from javax.swing import JTextField


class fBox(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'flexible Box',
            locationRelativeTo=None,
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        print '\nscreenSize:', Toolkit.getDefaultToolkit().getScreenSize()

        box = Box.createHorizontalBox()
        box.add(Box.createGlue())
        box.add(Box.createRigidArea(Dimension(5, 5)))
        box.add(JLabel(text='Name:', font=("Arabic", 30, 30)))
        box.add(Box.createRigidArea(Dimension(5, 5)))
        self.tf = box.add(
            JTextField(
                30,
                font=("Arabic", 30, 30)
            )
        )
        box.add(Box.createRigidArea(Dimension(5, 5)))
        box.add(
            JButton(
                'Submit',
                font=("Arabic", 30, 30),
                actionPerformed=self.buttonPress
            )
        )
        box.add(Box.createRigidArea(Dimension(5, 5)))
        box.add(Box.createGlue())

        frame.add(box)
        frame.pack()
        frame.setVisible(1)

    def buttonPress(self, event):
        tf = self.tf
        print 'Width curr: %4d  min: %4d  max: %4d  pref: %4d' % (
            tf.getSize().getWidth(),
            tf.getMinimumSize().getWidth(),
            tf.getMaximumSize().getWidth(),
            tf.getPreferredSize().getWidth()
        )


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(fBox())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
