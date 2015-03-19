/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codigo;

import java.awt.GraphicsConfiguration;
import javax.swing.ImageIcon;
import javax.swing.WindowConstants;

/**
 *
 * @author Braian
 */
public class VentanaPrincipal extends javax.swing.JFrame {

    /**
     * Creates new form VentanaPrincipal
     */
    public VentanaPrincipal() {

        initComponents();
        setIconImage(new ImageIcon(getClass().getResource("/imagenes/icon.png")).getImage());
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setResizable(false);
        setLocationRelativeTo(null);
        setTitle("Menu Principal");

    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        pnlUno = new javax.swing.JPanel();
        btnCrearUsuarios = new javax.swing.JButton();
        btnAsignarVuelos = new javax.swing.JButton();
        btnEstadoVuelos = new javax.swing.JButton();
        btnCrearUsuarios2 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        pnlUno.setBorder(javax.swing.BorderFactory.createTitledBorder(null, "Menu de Usuario", javax.swing.border.TitledBorder.DEFAULT_JUSTIFICATION, javax.swing.border.TitledBorder.DEFAULT_POSITION, new java.awt.Font("Berlin Sans FB", 0, 14))); // NOI18N

        btnCrearUsuarios.setFont(new java.awt.Font("Elected Office", 0, 18)); // NOI18N
        btnCrearUsuarios.setText("Crear Usuarios");
        btnCrearUsuarios.setPreferredSize(new java.awt.Dimension(204, 29));
        btnCrearUsuarios.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnCrearUsuariosActionPerformed(evt);
            }
        });

        btnAsignarVuelos.setFont(new java.awt.Font("Elected Office", 0, 18)); // NOI18N
        btnAsignarVuelos.setText("Asignación de Vuelos");
        btnAsignarVuelos.setPreferredSize(new java.awt.Dimension(204, 29));
        btnAsignarVuelos.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnAsignarVuelosActionPerformed(evt);
            }
        });

        btnEstadoVuelos.setFont(new java.awt.Font("Elected Office", 0, 18)); // NOI18N
        btnEstadoVuelos.setText("Observación de Vuelos");
        btnEstadoVuelos.setPreferredSize(new java.awt.Dimension(204, 29));
        btnEstadoVuelos.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnEstadoVuelosActionPerformed(evt);
            }
        });

        btnCrearUsuarios2.setFont(new java.awt.Font("Elected Office", 0, 18)); // NOI18N
        btnCrearUsuarios2.setLabel("Dar de Baja");
        btnCrearUsuarios2.setPreferredSize(new java.awt.Dimension(204, 29));
        btnCrearUsuarios2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnCrearUsuarios2ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout pnlUnoLayout = new javax.swing.GroupLayout(pnlUno);
        pnlUno.setLayout(pnlUnoLayout);
        pnlUnoLayout.setHorizontalGroup(
            pnlUnoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnlUnoLayout.createSequentialGroup()
                .addGap(39, 39, 39)
                .addGroup(pnlUnoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(btnCrearUsuarios, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(btnEstadoVuelos, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(28, 28, 28)
                .addGroup(pnlUnoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(btnCrearUsuarios2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(btnAsignarVuelos, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(14, Short.MAX_VALUE))
        );
        pnlUnoLayout.setVerticalGroup(
            pnlUnoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnlUnoLayout.createSequentialGroup()
                .addGap(22, 22, 22)
                .addGroup(pnlUnoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btnCrearUsuarios, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(btnAsignarVuelos, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(28, 28, 28)
                .addGroup(pnlUnoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btnEstadoVuelos, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(btnCrearUsuarios2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        btnEstadoVuelos.getAccessibleContext().setAccessibleName("");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(pnlUno, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(pnlUno, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        pnlUno.getAccessibleContext().setAccessibleName("MENU DE USUARIO");

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnCrearUsuariosActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnCrearUsuariosActionPerformed
        CrearUsuarios menu = new CrearUsuarios();
        menu.setVisible(true);
        this.setVisible(false);

        // TODO add your handling code here:
    }//GEN-LAST:event_btnCrearUsuariosActionPerformed

    private void btnAsignarVuelosActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnAsignarVuelosActionPerformed

        Vuelos menu = new Vuelos();
        menu.setVisible(true);
        this.setVisible(false);// TODO add your handling code here:
    }//GEN-LAST:event_btnAsignarVuelosActionPerformed

    private void btnEstadoVuelosActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnEstadoVuelosActionPerformed
        MenuAeropuerto menu = new MenuAeropuerto();
        dispose();
        menu.setVisible(true);        // TODO add your handling code here:
    }//GEN-LAST:event_btnEstadoVuelosActionPerformed

    private void btnCrearUsuarios2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnCrearUsuarios2ActionPerformed
        DarDeBaja menu = new DarDeBaja();
        dispose();
        menu.setVisible(true);
        // TODO add your handling code here:
    }//GEN-LAST:event_btnCrearUsuarios2ActionPerformed


    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnAsignarVuelos;
    private javax.swing.JButton btnCrearUsuarios;
    private javax.swing.JButton btnCrearUsuarios2;
    private javax.swing.JButton btnEstadoVuelos;
    private javax.swing.JPanel pnlUno;
    // End of variables declaration//GEN-END:variables
}
