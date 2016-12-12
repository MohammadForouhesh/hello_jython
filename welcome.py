from javax.swing import JFrame


win = JFrame( 'Welcome to Jython Swing' )
win.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE )
win.size = ( 400, 100 )
win.show()
if 'AdminConfig' in dir() :
    raw_input( '\nPress <Enter> to terminate the application: ' )