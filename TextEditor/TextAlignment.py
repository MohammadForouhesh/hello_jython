import java
import sys
from   java.awt import EventQueue
from   java.awt import GridLayout
from   javax.swing import JFrame
from   javax.swing import JLabel
from   javax.swing import JTextField


class TextAlignment(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'TextAlignment',
            layout=GridLayout(0, 2),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        data = [
            ['Left', JTextField.LEFT],
            ['Center', JTextField.CENTER],
            ['Right', JTextField.RIGHT],
            ['Leading', JTextField.LEADING],
            ['Trailing', JTextField.TRAILING]
        ]
        for label, align in data:
            frame.add(JLabel(label, font=("Comic Sans MS", 30, 30)))
            text = frame.add(
                JTextField(
                    5,
                    font=("Comic Sans MS", 30, 30),
                    text=str(align),
                    horizontalAlignment=align
                )
            )
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(TextAlignment())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
