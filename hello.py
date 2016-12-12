from javax.swing import *


def hello(event):
    print "Hello. I'm an event."


def test():
    frame = JFrame("Hello Jython")
    button = JButton("Hello",font=("Currier", 100, 60), actionPerformed=hello)
    frame.add(button)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setSize(300, 300)
    frame.show()


test()
