/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codigo;

import datechooser.beans.DateChooserDialog;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import javax.swing.ImageIcon;
import javax.swing.WindowConstants;

/**
 *
 * @author Braian
 */
public class CrearVuelo extends javax.swing.JFrame {

    /**
     * Creates new form CrearUsuarios
     */
    VentanaPrincipal menu;

    public CrearVuelo() {

        initComponents();
        datosVentana();
        setIconImage(new ImageIcon(getClass().getResource("/imagenes/icon.png")).getImage());

        setResizable(false);
        menu = new VentanaPrincipal();
        setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE);

        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {

                setDefaultCloseOperation(
                        WindowConstants.DISPOSE_ON_CLOSE);
                setVisible(false);
                dispose();
                menu.setVisible(true);

            }
        });
        setLocationRelativeTo(null);
        setTitle("Menu - Crear Usuario");
    }

    public void datosVentana() {
        lblError.setVisible(false);

    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel1 = new javax.swing.JLabel();
        jSeparator1 = new javax.swing.JSeparator();
        btnGuardar = new javax.swing.JButton();
        btnCancelar = new javax.swing.JButton();
        lblNick1 = new javax.swing.JLabel();
        lblDirec1 = new javax.swing.JLabel();
        combAeropuerto = new javax.swing.JComboBox();
        comboLugarLlegada = new javax.swing.JComboBox();
        lblDirec2 = new javax.swing.JLabel();
        lblDirec3 = new javax.swing.JLabel();
        jSeparator2 = new javax.swing.JSeparator();
        lblError = new javax.swing.JLabel();
        pnlPrimera1 = new javax.swing.JPanel();
        jLabel4 = new javax.swing.JLabel();
        txtNoAsientos1 = new javax.swing.JTextField();
        jLabel5 = new javax.swing.JLabel();
        txtCostoA1 = new javax.swing.JTextField();
        pnlTercera = new javax.swing.JPanel();
        jLabel8 = new javax.swing.JLabel();
        txtNoAsientos3 = new javax.swing.JTextField();
        jLabel9 = new javax.swing.JLabel();
        txtCostoA3 = new javax.swing.JTextField();
        dateChooserCombo1 = new datechooser.beans.DateChooserCombo();
        pnlTercera1 = new javax.swing.JPanel();
        jLabel10 = new javax.swing.JLabel();
        txtNoAsientos2 = new javax.swing.JTextField();
        jLabel11 = new javax.swing.JLabel();
        txtCostoA2 = new javax.swing.JTextField();
        dateChooserCombo2 = new datechooser.beans.DateChooserCombo();
        lblDirec4 = new javax.swing.JLabel();
        lblID = new javax.swing.JLabel();
        lblDirec5 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jLabel1.setFont(new java.awt.Font("Elected Office", 0, 22)); // NOI18N
        jLabel1.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel1.setText("Bienvenido, ingrese la información necesaria");

        btnGuardar.setText("Crear Vuelo");
        btnGuardar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnGuardarActionPerformed(evt);
            }
        });

        btnCancelar.setText("Cancelar");
        btnCancelar.setMaximumSize(new java.awt.Dimension(117, 23));
        btnCancelar.setMinimumSize(new java.awt.Dimension(117, 23));
        btnCancelar.setPreferredSize(new java.awt.Dimension(117, 23));
        btnCancelar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnCancelarActionPerformed(evt);
            }
        });

        lblNick1.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        lblNick1.setText("Nombre del Aeropuerto");

        lblDirec1.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        lblDirec1.setText("Lugar de Llegada:");

        combAeropuerto.setModel(new javax.swing.DefaultComboBoxModel(new String[] { "(Seleccione un Aeropuerto)" }));

        comboLugarLlegada.setModel(new javax.swing.DefaultComboBoxModel(new String[] { "(Seleccione un Aeropuerto)" }));

        lblDirec2.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        lblDirec2.setText("Hora y Fecha de Salida:");

        lblDirec3.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        lblDirec3.setText("Hora y Fecha de Llegada:");

        lblError.setForeground(new java.awt.Color(255, 0, 0));
        lblError.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        lblError.setText("Por favor llene todos los campos para continuar.");
        lblError.setPreferredSize(new java.awt.Dimension(25, 25));

        pnlPrimera1.setBorder(javax.swing.BorderFactory.createTitledBorder("Vuelos Primera Clase"));
        pnlPrimera1.setRequestFocusEnabled(false);

        jLabel4.setFont(new java.awt.Font("Berlin Sans FB", 0, 14)); // NOI18N
        jLabel4.setText("No. de Asientos:");

        txtNoAsientos1.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyTyped(java.awt.event.KeyEvent evt) {
                txtNoAsientos1KeyTyped(evt);
            }
        });

        jLabel5.setFont(new java.awt.Font("Berlin Sans FB", 0, 14)); // NOI18N
        jLabel5.setText("Costo por Asiento:");

        txtCostoA1.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyTyped(java.awt.event.KeyEvent evt) {
                txtCostoA1KeyTyped(evt);
            }
        });

        javax.swing.GroupLayout pnlPrimera1Layout = new javax.swing.GroupLayout(pnlPrimera1);
        pnlPrimera1.setLayout(pnlPrimera1Layout);
        pnlPrimera1Layout.setHorizontalGroup(
            pnlPrimera1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnlPrimera1Layout.createSequentialGroup()
                .addGap(40, 40, 40)
                .addComponent(jLabel4)
                .addGap(30, 30, 30)
                .addComponent(txtNoAsientos1, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 73, Short.MAX_VALUE)
                .addComponent(jLabel5)
                .addGap(30, 30, 30)
                .addComponent(txtCostoA1, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(30, 30, 30))
        );
        pnlPrimera1Layout.setVerticalGroup(
            pnlPrimera1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnlPrimera1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(pnlPrimera1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel4)
                    .addComponent(txtNoAsientos1, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel5)
                    .addComponent(txtCostoA1, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(19, Short.MAX_VALUE))
        );

        pnlTercera.setBorder(javax.swing.BorderFactory.createTitledBorder("Vuelos Clase Ejecutiva"));

        jLabel8.setFont(new java.awt.Font("Berlin Sans FB", 0, 14)); // NOI18N
        jLabel8.setText("No. de Asientos:");

        txtNoAsientos3.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyTyped(java.awt.event.KeyEvent evt) {
                txtNoAsientos3KeyTyped(evt);
            }
        });

        jLabel9.setFont(new java.awt.Font("Berlin Sans FB", 0, 14)); // NOI18N
        jLabel9.setText("Costo por Asiento:");

        txtCostoA3.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyTyped(java.awt.event.KeyEvent evt) {
                txtCostoA3KeyTyped(evt);
            }
        });

        javax.swing.GroupLayout pnlTerceraLayout = new javax.swing.GroupLayout(pnlTercera);
        pnlTercera.setLayout(pnlTerceraLayout);
        pnlTerceraLayout.setHorizontalGroup(
            pnlTerceraLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnlTerceraLayout.createSequentialGroup()
                .addGap(40, 40, 40)
                .addComponent(jLabel8)
                .addGap(30, 30, 30)
                .addComponent(txtNoAsientos3, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 73, Short.MAX_VALUE)
                .addComponent(jLabel9)
                .addGap(30, 30, 30)
                .addComponent(txtCostoA3, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(30, 30, 30))
        );
        pnlTerceraLayout.setVerticalGroup(
            pnlTerceraLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnlTerceraLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(pnlTerceraLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel8)
                    .addComponent(txtNoAsientos3, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel9)
                    .addComponent(txtCostoA3, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(19, Short.MAX_VALUE))
        );

        dateChooserCombo1.addSelectionChangedListener(new datechooser.events.SelectionChangedListener() {
            public void onSelectionChange(datechooser.events.SelectionChangedEvent evt) {
                dateChooserCombo1OnSelectionChange(evt);
            }
        });

        pnlTercera1.setBorder(javax.swing.BorderFactory.createTitledBorder("Vuelos Clase Ejecutiva"));

        jLabel10.setFont(new java.awt.Font("Berlin Sans FB", 0, 14)); // NOI18N
        jLabel10.setText("No. de Asientos:");

        txtNoAsientos2.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyTyped(java.awt.event.KeyEvent evt) {
                txtNoAsientos2KeyTyped(evt);
            }
        });

        jLabel11.setFont(new java.awt.Font("Berlin Sans FB", 0, 14)); // NOI18N
        jLabel11.setText("Costo por Asiento:");

        txtCostoA2.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyTyped(java.awt.event.KeyEvent evt) {
                txtCostoA2KeyTyped(evt);
            }
        });

        javax.swing.GroupLayout pnlTercera1Layout = new javax.swing.GroupLayout(pnlTercera1);
        pnlTercera1.setLayout(pnlTercera1Layout);
        pnlTercera1Layout.setHorizontalGroup(
            pnlTercera1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnlTercera1Layout.createSequentialGroup()
                .addGap(40, 40, 40)
                .addComponent(jLabel10)
                .addGap(30, 30, 30)
                .addComponent(txtNoAsientos2, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 73, Short.MAX_VALUE)
                .addComponent(jLabel11)
                .addGap(30, 30, 30)
                .addComponent(txtCostoA2, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(30, 30, 30))
        );
        pnlTercera1Layout.setVerticalGroup(
            pnlTercera1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnlTercera1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(pnlTercera1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel10)
                    .addComponent(txtNoAsientos2, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel11)
                    .addComponent(txtCostoA2, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(19, Short.MAX_VALUE))
        );

        dateChooserCombo2.addSelectionChangedListener(new datechooser.events.SelectionChangedListener() {
            public void onSelectionChange(datechooser.events.SelectionChangedEvent evt) {
                dateChooserCombo2OnSelectionChange(evt);
            }
        });

        lblDirec4.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        lblDirec4.setText("Id. Vuelo:");

        lblID.setText("01");

        lblDirec5.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        lblDirec5.setText("Estado Inicial");

        jLabel2.setText("En Aeropuerto");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(20, 20, 20)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jSeparator1, javax.swing.GroupLayout.PREFERRED_SIZE, 471, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 456, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(25, Short.MAX_VALUE))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGap(0, 0, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(pnlTercera1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(pnlTercera, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(pnlPrimera1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jSeparator2, javax.swing.GroupLayout.PREFERRED_SIZE, 466, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(19, 19, 19))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addComponent(lblError, javax.swing.GroupLayout.PREFERRED_SIZE, 366, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(74, 74, 74))))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(btnGuardar)
                .addGap(97, 97, 97)
                .addComponent(btnCancelar, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(97, 97, 97))
            .addGroup(layout.createSequentialGroup()
                .addGap(40, 40, 40)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(lblDirec1)
                            .addComponent(lblNick1)
                            .addComponent(lblDirec2))
                        .addGap(29, 29, 29)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(combAeropuerto, 0, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(comboLugarLlegada, 0, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(dateChooserCombo1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(lblDirec3)
                            .addComponent(lblDirec4)
                            .addComponent(lblDirec5))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(dateChooserCombo2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(lblID)
                                    .addComponent(jLabel2))
                                .addGap(0, 0, Short.MAX_VALUE)))))
                .addGap(28, 28, 28))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 27, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(14, 14, 14)
                .addComponent(jSeparator1, javax.swing.GroupLayout.PREFERRED_SIZE, 14, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lblNick1)
                    .addComponent(combAeropuerto, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(10, 10, 10)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lblDirec1)
                    .addComponent(comboLugarLlegada, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(10, 10, 10)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(lblDirec2)
                    .addComponent(dateChooserCombo1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(7, 7, 7)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(lblDirec3)
                    .addComponent(dateChooserCombo2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(10, 10, 10)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(lblDirec4)
                    .addComponent(lblID))
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(10, 10, 10)
                        .addComponent(lblDirec5))
                    .addGroup(layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(jLabel2)))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jSeparator2, javax.swing.GroupLayout.PREFERRED_SIZE, 14, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(pnlPrimera1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(pnlTercera1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(11, 11, 11)
                .addComponent(pnlTercera, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(lblError, javax.swing.GroupLayout.PREFERRED_SIZE, 20, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btnGuardar)
                    .addComponent(btnCancelar, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnCancelarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnCancelarActionPerformed
        menu.setVisible(true);
        dispose();
        // TODO add your handling code here:
    }//GEN-LAST:event_btnCancelarActionPerformed

    private void btnGuardarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnGuardarActionPerformed
        lblError.setText("");
        if (validarCampos() == false) {
            lblError.setText("Por favor llene todos los campos para continuar.");
            lblError.setVisible(true);
        } else {

        }
        // TODO add your handling code here:
    }//GEN-LAST:event_btnGuardarActionPerformed

    private void txtNoAsientos1KeyTyped(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_txtNoAsientos1KeyTyped
        char c = evt.getKeyChar();

        if (Character.isLetter(c)) {
            getToolkit().beep();

            evt.consume();

            lblError.setText("En este campo solo puede ingresar números.");
            lblError.setVisible(true);

        } else {
            lblError.setVisible(false);

        }         // TODO add your handling code here:
    }//GEN-LAST:event_txtNoAsientos1KeyTyped

    private void txtCostoA1KeyTyped(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_txtCostoA1KeyTyped
        char c = evt.getKeyChar();

        if (Character.isLetter(c)) {
            getToolkit().beep();

            evt.consume();

            lblError.setText("En este campo solo puede ingresar números.");
            lblError.setVisible(true);

        } else {
            lblError.setVisible(false);

        }         // TODO add your handling code here:
    }//GEN-LAST:event_txtCostoA1KeyTyped

    private void txtNoAsientos3KeyTyped(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_txtNoAsientos3KeyTyped
        char c = evt.getKeyChar();

        if (Character.isLetter(c)) {
            getToolkit().beep();

            evt.consume();

            lblError.setText("En este campo solo puede ingresar números.");
            lblError.setVisible(true);

        } else {
            lblError.setVisible(false);

        }         // TODO add your handling code here:
    }//GEN-LAST:event_txtNoAsientos3KeyTyped

    private void txtCostoA3KeyTyped(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_txtCostoA3KeyTyped
        char c = evt.getKeyChar();

        if (Character.isLetter(c)) {
            getToolkit().beep();

            evt.consume();

            lblError.setText("En este campo solo puede ingresar números.");
            lblError.setVisible(true);

        } else {
            lblError.setVisible(false);

        }         // TODO add your handling code here:
    }//GEN-LAST:event_txtCostoA3KeyTyped

    private void dateChooserCombo1OnSelectionChange(datechooser.events.SelectionChangedEvent evt) {//GEN-FIRST:event_dateChooserCombo1OnSelectionChange
        // TODO add your handling code here:
    }//GEN-LAST:event_dateChooserCombo1OnSelectionChange

    private void txtNoAsientos2KeyTyped(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_txtNoAsientos2KeyTyped
        char c = evt.getKeyChar();

        if (Character.isLetter(c)) {
            getToolkit().beep();

            evt.consume();

            lblError.setText("En este campo solo puede ingresar números.");
            lblError.setVisible(true);

        } else {
            lblError.setVisible(false);

        } // TODO add your handling code here:
    }//GEN-LAST:event_txtNoAsientos2KeyTyped

    private void txtCostoA2KeyTyped(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_txtCostoA2KeyTyped
        char c = evt.getKeyChar();

        if (Character.isLetter(c)) {
            getToolkit().beep();

            evt.consume();

            lblError.setText("En este campo solo puede ingresar números.");
            lblError.setVisible(true);

        } else {
            lblError.setVisible(false);

        }         // TODO add your handling code here:
    }//GEN-LAST:event_txtCostoA2KeyTyped

    private void dateChooserCombo2OnSelectionChange(datechooser.events.SelectionChangedEvent evt) {//GEN-FIRST:event_dateChooserCombo2OnSelectionChange
        // TODO add your handling code here:
    }//GEN-LAST:event_dateChooserCombo2OnSelectionChange

    public boolean validarCampos() {
        if (txtCostoA1.getText().equals("") || txtCostoA2.getText().equals("") || txtCostoA3.getText().equals("")
                || txtNoAsientos1.getText().equals("") || txtNoAsientos2.getText().equals("") || txtNoAsientos3.getText().equals("")
                || (combAeropuerto.getModel().getSelectedItem()=="") | (comboLugarLlegada.getModel().getSelectedItem()!="") || dateChooserCombo1.getText().equals("")) {
            System.out.println("falso");
            return false;

        } else {
            System.out.println("cierto");
            return true;
        }
    }

    /**
     * @param args the command line arguments
     */

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnCancelar;
    private javax.swing.JButton btnGuardar;
    private javax.swing.JComboBox combAeropuerto;
    private javax.swing.JComboBox comboLugarLlegada;
    private datechooser.beans.DateChooserCombo dateChooserCombo1;
    private datechooser.beans.DateChooserCombo dateChooserCombo2;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JSeparator jSeparator1;
    private javax.swing.JSeparator jSeparator2;
    private javax.swing.JLabel lblDirec1;
    private javax.swing.JLabel lblDirec2;
    private javax.swing.JLabel lblDirec3;
    private javax.swing.JLabel lblDirec4;
    private javax.swing.JLabel lblDirec5;
    private javax.swing.JLabel lblError;
    private javax.swing.JLabel lblID;
    private javax.swing.JLabel lblNick1;
    private javax.swing.JPanel pnlPrimera1;
    private javax.swing.JPanel pnlSegunda1;
    private javax.swing.JPanel pnlTercera;
    private javax.swing.JPanel pnlTercera1;
    private javax.swing.JTextField txtCostoA1;
    private javax.swing.JTextField txtCostoA2;
    private javax.swing.JTextField txtCostoA3;
    private javax.swing.JTextField txtNoAsientos1;
    private javax.swing.JTextField txtNoAsientos2;
    private javax.swing.JTextField txtNoAsientos3;
    private javax.swing.JTextField txtNoAsientos4;
    private javax.swing.JTextField txtNoAsientos5;
    // End of variables declaration//GEN-END:variables
}
