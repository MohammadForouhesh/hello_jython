import java
import sys
from   java.awt import EventQueue
from   java.awt import FlowLayout
from   java.awt.event import ActionListener
from   javax.swing import JComboBox
from   javax.swing import JFrame
from   javax.swing import JLabel


# need more development
class EditableComboBox(java.lang.Runnable, ActionListener):
    def run(self):
        frame = JFrame(
            'EditableComboBox',
            size=(210, 100),
            layout=FlowLayout(),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        frame.add(JLabel('Pick one:', font=("Comic Sans MS", 30, 30)))
        self.choices = 'The,quick,brown,fox,jumped'.split(',')
        self.choices.extend('over,the,lazy,spam'.split(','))
        ComboBox = frame.add(
            JComboBox(
                self.choices,
                font=("Comic Sans MS", 30, 30),
                editable=1
            )
        )
        ComboBox.addActionListener(self)
        self.msg = frame.add(JLabel(font=("Comic Sans MS", 20, 20)))
        frame.setVisible(1)

    def actionPerformed(self, event):
        ComboBox = event.getSource()
        msg = 'Selection: ' + ComboBox.getSelectedItem()
        self.msg.setText(msg)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(EditableComboBox())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
