import java
import sys
from   java.awt import EventQueue
from   java.awt import GridLayout
from   java.text import NumberFormat
from   javax.swing import JFormattedTextField
from   javax.swing import JFrame
from   javax.swing import JLabel
from   javax.swing import JTextField


class NumberFormatInfo(java.lang.Runnable):
    def addFTF(self, name):
        pane = self.frame.getContentPane()
        pane.add(JLabel(name, font=("Comic Sans MS", 30, 30)))
        format = eval('NumberFormat.' + name)
        pane.add(
            JFormattedTextField(
                format,
                value=12345.67890,
                font=("Comic Sans MS", 30, 30)
            )
        )
        pane.add(
            JTextField(
                str(format.getMinimumIntegerDigits()),
                horizontalAlignment=JTextField.CENTER,
                font=("Comic Sans MS", 30, 30)
            )
        )
        pane.add(
            JTextField(
                str(format.getMaximumIntegerDigits()),
                horizontalAlignment=JTextField.CENTER,
                font=("Comic Sans MS", 30, 30)
            )
        )
        pane.add(
            JTextField(
                str(format.getMinimumFractionDigits()),
                horizontalAlignment=JTextField.CENTER,
                font=("Comic Sans MS", 30, 30)
            )
        )
        pane.add(
            JTextField(
                str(format.getMaximumFractionDigits()),
                horizontalAlignment=JTextField.CENTER,
                font=("Comic Sans MS", 30, 30)
            )
        )
        pane.add(
            JTextField(
                str(format.getRoundingMode()),
                horizontalAlignment=JTextField.CENTER,
                font=("Comic Sans MS", 30, 30)
            )
        )
        pane.add(
            JTextField(
                str(format.isGroupingUsed()),
                horizontalAlignment=JTextField.CENTER,
                font=("Comic Sans MS", 30, 30)
            )
        )
        pane.add(
            JTextField(
                str(format.isParseIntegerOnly()),
                horizontalAlignment=JTextField.CENTER,
                font=("Comic Sans MS", 30, 30)
            )
        )

    def run(self):
        self.frame = frame = JFrame(
            'NumberFormatInfo',
            layout=GridLayout(0, 9),
            font=("Comic Sans MS", 30, 30),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        self.addFTF('getInstance()')
        self.addFTF('getCurrencyInstance()')
        self.addFTF('getIntegerInstance()')
        self.addFTF('getNumberInstance()')
        self.addFTF('getPercentInstance()')
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(NumberFormatInfo())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
