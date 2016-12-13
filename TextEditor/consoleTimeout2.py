import java
import re
import sys

from   java.awt import EventQueue
from   java.awt import FlowLayout

from   javax.swing import BoxLayout
from   javax.swing import JFrame
from   javax.swing import JLabel
from   javax.swing import JPanel
from   javax.swing import JTextField
from   javax.swing import SwingWorker


def getTimeout():
    dep = AdminConfig.getid('/Deployment:isclite/')
    if not dep:
        timeout = None
    else:
        appDep = AdminConfig.list('ApplicationDeployment', dep)
        appConfig = AdminConfig.list('ApplicationConfig', appDep)
        if not appConfig:
            appConfig = AdminConfig.create('ApplicationConfig', appDep, [])
        sesMgmt = AdminConfig.list('SessionManager', appDep)
        if not sesMgmt:
            sesMgmt = AdminConfig.create('SessionManager', appConfig, [])
        tuningParms = AdminConfig.showAttribute(sesMgmt, 'tuningParams')
        if not tuningParms:
            timeout = None
            print "Error: tuningParams object doesn't exist."
        else:
            timeout = AdminConfig.showAttribute(
                tuningParms,
                'invalidationTimeout'
            )
    return timeout


def setTimeout(value):
    dep = AdminConfig.getid('/Deployment:isclite/')
    if not dep:
        result = 'Deployment object not found: isclite'
    else:
        appDep = AdminConfig.list('ApplicationDeployment', dep)
        appConfig = AdminConfig.list('ApplicationConfig', appDep)
        if not appConfig:
            appConfig = AdminConfig.create('ApplicationConfig', appDep, [])
        sesMgmt = AdminConfig.list('SessionManager', appDep)
        if not sesMgmt:
            sesMgmt = AdminConfig.create('SessionManager', appConfig, [])
        tuningParms = AdminConfig.showAttribute(sesMgmt, 'tuningParams')
        if not tuningParms:
            timeout = None
            result = "Error: tuningParams object doesn't exist."
        else:
            AdminConfig.modify(
                tuningParms,
                [['invalidationTimeout', value]]
            )
            AdminConfig.save()
            result = 'Update successful.'
    return result


class WSAStask(SwingWorker):
    def __init__(self, textField, labelField):
        self.text = textField  # Save the references
        self.label = labelField
        SwingWorker.__init__(self)

    def doInBackground(self):
        self.text.setEnabled(0)  # Disable input field
        self.label.setText('working...')  # Inform user of status
        value = self.text.getText().strip()
        if not re.search(re.compile('^\d+$'), value):
            msg = 'Invalid numeric value "%s".' % value
            self.label.setText(msg)
            self.text.setText(getTimeout())
        else:
            self.label.setText(setTimeout(value))

    def done(self):
        self.text.setEnabled(1)  # Enable input field


class consoleTimeout2(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'Console timeout',
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        )
        cp = frame.getContentPane()
        cp.setLayout(BoxLayout(cp, BoxLayout.Y_AXIS))
        input = JPanel(layout=FlowLayout())
        input.add(JLabel('Timeout:'))
        self.text = JTextField(3, actionPerformed=self.update)
        input.add(self.text)
        self.text.setText(getTimeout())
        input.add(JLabel('minutes'))
        cp.add(input)
        self.msg = cp.add(JLabel())

        frame.setSize(290, 100)
        frame.setVisible(1)

    def update(self, event):
        WSAStask(self.text, self.msg).execute()


if __name__ in ['__main__', 'main']:
    if 'AdminConfig' in globals().keys():
        EventQueue.invokeLater(consoleTimeout2())
        raw_input('\nPress <Enter> to terminate the application: ')
    else:
        print '\nError: This script requires a WebSphere Application Server.\n'
        print 'Usage: wsadmin -f consoleTimeout2.py'
else:
    print '\nError: This script should be executed, not imported.\n'
    print 'Usage: wsadmin -f %s.py' % __name__
    sys.exit()
