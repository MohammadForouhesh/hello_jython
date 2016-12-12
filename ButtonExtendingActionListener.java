
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class ButtonExtendingActionListener {
    public static void main( String[] args ) {
        javax.swing.SwingUtilities.invokeLater( new Runnable() {
            public void run() {
                JFrame frame = new JFrame( "ButtonDemo" );
                frame.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );
                JButton button = new JButton( "Press me" );
                frame.add( button );
                frame.pack();
                frame.setVisible( true );
            }
        });
    }
}
