import java
import sys
from   java.awt import EventQueue
from   java.awt import Font
from   java.awt import GridLayout
from   javax.swing import JFrame
from   javax.swing import JLabel
from   javax.swing import JTextField


class TextFonts(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'TextFonts',
            layout=GridLayout(0, 2),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        data = [
            ['Left', JTextField.LEFT, None],
            ['Center', JTextField.CENTER, Font('Courier', Font.BOLD, 12)],
            ['Right', JTextField.RIGHT, Font('Ariel', Font.ITALIC, 14)],
            ['Leading', JTextField.LEADING, Font('Elephant', Font.BOLD | Font.ITALIC, 20)],
            ['Trailing', JTextField.TRAILING, Font('Papyrus', Font.PLAIN, 36)]
        ]
        for label, align, font in data:
            frame.add(JLabel(label))
            text = frame.add(
                JTextField(
                    5,
                    text=str(align),
                    horizontalAlignment=align,
                )
            )
            if font:
                text.setFont(font)
        frame.pack()
        frame.setVisible(1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(TextFonts())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
