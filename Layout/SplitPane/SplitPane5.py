import java
import sys
from   java.awt import EventQueue
from   java.awt import GridLayout
from   javax.swing import JButton
from   javax.swing import JFrame
from   javax.swing import JPanel
from   javax.swing import JSplitPane


class SplitPane5(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'SplitPane5',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        self.sp = JSplitPane(
            JSplitPane.VERTICAL_SPLIT,
            self.sizeOptions(),
            JButton('Bottom', font=("Vivaldi", 30, 30))
        )
        print '\nInitial size:', self.sp.getDividerSize()
        frame.add(self.sp)
        frame.pack()
        frame.setVisible(1)

    def sizeOptions(self):
        pane = JPanel(GridLayout(1, 0))
        pane.add(
            JButton(
                'Small',
                font=("Vivaldi", 30, 30),
                actionPerformed=self.resize
            )
        )
        pane.add(
            JButton(
                'Medium',
                font=("Vivaldi", 30, 30),
                actionPerformed=self.resize
            )
        )
        pane.add(
            JButton(
                'Large',
                font=("Vivaldi", 30, 30),
                actionPerformed=self.resize
            )
        )
        return pane

    def resize(self, event):
        sizes = {
            'Small': 0,
            'Medium': 10,
            'Large': 20
        }
        name = event.getActionCommand()
        self.sp.setDividerSize(sizes[name])


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(SplitPane5())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
