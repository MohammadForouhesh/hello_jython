import java
import sys
from java.awt import BorderLayout
from java.awt import Component
from java.awt import EventQueue
from java.awt.event import ActionListener
from javax.swing import JButton
from javax.swing import JComboBox
from javax.swing import JFrame
from javax.swing import JLabel
from javax.swing import JPanel


class DynamicComboBox(java.lang.Runnable, ActionListener):
    def run(self):
        self.frame = frame = JFrame(
            'DynamicComboBox',
            size=(310, 137),
            layout=BorderLayout(),
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        panel = JPanel()
        panel.add(JLabel('Pick one:', font=("Comic Sans MS", 30, 30)))
        self.choices = 'The,quick,brown,fox,jumped'.split(',')
        self.choices.extend('over,the,lazy,spam'.split(','))
        self.ComboBox = ComboBox = JComboBox(
            self.choices,
            font=("Comic Sans MS", 20, 20),
            editable=1
        )
        ComboBox.addActionListener(self)
        panel.add(ComboBox)
        frame.add(panel, BorderLayout.NORTH)
        panel = JPanel()
        self.RemoveButton = JButton(
            'Remove',
            font=("Comic Sans MS", 20, 20),
            actionPerformed=self.remove
        )
        panel.add(self.RemoveButton)
        frame.add(panel, BorderLayout.CENTER)
        panel = JPanel(alignmentX=Component.CENTER_ALIGNMENT, font=("Comic Sans MS", 30, 30))
        self.msg = panel.add(JLabel('Make a selection', font=("Comic Sans MS", 20, 20)))
        frame.add(panel, BorderLayout.SOUTH)
        frame.setVisible(1)

    def actionPerformed(self, event):
        cb = self.ComboBox
        item = cb.getSelectedItem().strip()
        items = [
            cb.getItemAt(i)
            for i in range(cb.getItemCount())
            ]
        if item:
            if item not in items:
                cb.addItem(item)
                self.RemoveButton.setEnabled(1)
            msg = 'Selection: "%s"' % item
            self.msg.setText(msg)
        else:
            cb.setSelectedIndex(0)

    def remove(self, event):
        cb = self.ComboBox
        index = cb.getSelectedIndex()
        item = cb.getSelectedItem()
        try:
            cb.removeItem(item)
            self.msg.setText('Item removed: "%s"' % item)
        except:
            self.msg.setText('Remove request failed')
        self.RemoveButton.setEnabled(cb.getItemCount() > 1)


if __name__ in ['__main__', 'main']:
    EventQueue.invokeLater(DynamicComboBox())
    if 'AdminConfig' in dir():
        raw_input('\nPress <Enter> to terminate the application:\n')
else:
    print '\nError: This script should be executed, not imported.\n'
    which = ['wsadmin -f', 'jython']['JYTHON_JAR' in dir(sys)]
    print 'Usage: %s %s.py' % (which, __name__)
    sys.exit()
