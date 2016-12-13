
import java
import sys
from   java.awt    import EventQueue
from   java.awt    import FlowLayout
from   javax.swing import JFormattedTextField
from   javax.swing import JFrame
from   javax.swing import JSpinner
from   javax.swing import SpinnerNumberModel
class Spinner3( java.lang.Runnable ) :
    def run( self ) :
        frame = JFrame(
            'Spinner3',
            layout = FlowLayout(),
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE
        )
        frame.add(
            JSpinner(
                SpinnerNumberModel(
                    0,            # Initial value
                    -3141.59,      # Minimum value
                    +3141.59,      # Maximum value
                    3.14159       # stepSize
                ),
                font=("Comic Sans MS", 30, 30)
            )
        )
        frame.pack()
        frame.setVisible( 1 )


if __name__ in [ '__main__', 'main' ] :
    EventQueue.invokeLater( Spinner3() )
    if 'AdminConfig' in dir() :
        raw_input( '\nPress <Enter> to terminate the application:\n' )
else :
    print '\nError: This script should be executed, not imported.\n'
    which = [ 'wsadmin -f', 'jython' ][ 'JYTHON_JAR' in dir( sys ) ]
    print 'Usage: %s %s.py' % ( which, __name__ )
    sys.exit()
