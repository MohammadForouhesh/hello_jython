import java
import re
import sys

from   java.awt import BorderLayout
from   java.awt import EventQueue

from   javax.swing import JLabel
from   javax.swing import JFrame
from   javax.swing import JTextArea
from   javax.swing import JScrollPane


class SimpleEditor(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'Simple Editor',
            layout=BorderLayout(),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )

        # -----------------------------------------------------------------------
        # The JTextArea will be used to hold the user entered text.
        # -----------------------------------------------------------------------
        self.area = JTextArea(
            font=("Comic Sans MS", 30, 30),
            rows=8,
            columns=32,
            caretUpdate=self.caretUpdate
        )
        frame.add(JScrollPane(self.area), BorderLayout.CENTER)
        self.words = JLabel('# words: 0  # lines: 0', font=("Comic Sans MS", 15, 15))
        frame.add(self.words, BorderLayout.SOUTH)

        frame.pack()
        frame.setVisible(1)

    # ---------------------------------------------------------------------------
    # Role: Build and display our graphical application
    # Note: This is a brute force implementation, just to demonstrate some ideas
    # ---------------------------------------------------------------------------
    def caretUpdate(self, event, regexp=None):
        if not regexp:
            regexp = re.compile('\W+', re.MULTILINE)
        pos = event.getDot()
        text = self.area.getText()
        if text.strip() == '':
            words = lines = 0
        else:
            words = len(re.split(regexp, text))
            lines = len(text.splitlines())
        msg = '# words: %d  # lines: %d' % (words, lines)
        self.words.setText(msg)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(SimpleEditor())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
