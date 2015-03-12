/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codigo;

import javax.swing.UIManager;

/**
 *
 * @author Braian
 */
public class Constructor {
    public static void main(String[] args) {
        try {
            UIManager.setLookAndFeel("com.sun.java.swing.plaf.nimbus.NimbusLookAndFeel");

        } catch (Exception e) {
            e.printStackTrace();
        }
        VentanaPrincipal menu = new VentanaPrincipal();
        menu.setVisible(true);
    }
    
}
