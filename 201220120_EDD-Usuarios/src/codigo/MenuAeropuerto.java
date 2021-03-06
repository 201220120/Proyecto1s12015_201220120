/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codigo;

import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.StringTokenizer;
import javax.swing.ImageIcon;
import static javax.swing.JOptionPane.showMessageDialog;
import javax.swing.WindowConstants;

/**
 *
 * @author Braian
 */
public class MenuAeropuerto extends javax.swing.JFrame {

    /**
     * Creates new form Vuelos
     */
    VentanaPrincipal menu;

    public MenuAeropuerto() {
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
    }

    public void datosVentana() {
        lblError.setText("");

        panelUsuarios.setContentType("text/html");
        panelAeropuertos.setContentType("text/html");
        panelVuelos.setContentType("text/html");
        String url1 = "http://127.0.0.1:5000/get_usuarios";
        String res1 = crearConexion.crearConexion(url1, "HTTP");

        StringTokenizer tokens1 = new StringTokenizer(res1, ",");
        while (tokens1.hasMoreTokens()) {
            String a = tokens1.nextToken();
            boxUsuarios.addItem(a);
        }
        String url = "http://127.0.0.1:5000/get_datos_2/";
        String res = crearConexion.crearConexion(url, "HTTP");
        res = res.replace("-", " ");
        String url4 = "http://127.0.0.1:5000/mostrar_aeropuertos";
        String res4 = crearConexion.crearConexion(url4, "HTTP");
        String contenido = "<html><head></head><body><h1>Vuelos disponibles</h1><table border=\"1\"><tr><td><h2>Id Vuelo</h2></td><td><h2>Lugar de llegada</h2></td><td><h2>Lugar de salida</h2></td><td><h2>Estado</h2></td></tr>"
                + "\n" + res + "\n" + "</table></body></html>";

        panelAeropuertos.setText(contenido);
        panelVuelos.setText(res4);

    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        lbltitulo = new javax.swing.JLabel();
        jPanel1 = new javax.swing.JPanel();
        jScrollPane2 = new javax.swing.JScrollPane();
        panelVuelos = new javax.swing.JTextPane();
        jScrollPane3 = new javax.swing.JScrollPane();
        panelAeropuertos = new javax.swing.JTextPane();
        jPanel2 = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        boxUsuarios = new javax.swing.JComboBox();
        btnComprobar = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        panelUsuarios = new javax.swing.JTextPane();
        lblError = new javax.swing.JLabel();
        btnComprobar3 = new javax.swing.JButton();
        jSeparator2 = new javax.swing.JSeparator();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        lbltitulo.setFont(new java.awt.Font("Elected Office", 0, 22)); // NOI18N
        lbltitulo.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        lbltitulo.setText("Bienvenido, ingrese la información necesaria");

        jPanel1.setBorder(javax.swing.BorderFactory.createTitledBorder("Vuelos - Aeropuertos"));

        jScrollPane2.setViewportView(panelVuelos);

        jScrollPane3.setViewportView(panelAeropuertos);

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jScrollPane3, javax.swing.GroupLayout.DEFAULT_SIZE, 498, Short.MAX_VALUE)
                    .addComponent(jScrollPane2))
                .addContainerGap())
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addComponent(jScrollPane3, javax.swing.GroupLayout.PREFERRED_SIZE, 152, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jScrollPane2)
                .addContainerGap())
        );

        jPanel2.setBorder(javax.swing.BorderFactory.createTitledBorder("Usuarios - Vuelos Asignados"));

        jLabel1.setFont(new java.awt.Font("Berlin Sans FB", 0, 14)); // NOI18N
        jLabel1.setText("Seleccione un usuario:");

        boxUsuarios.setModel(new javax.swing.DefaultComboBoxModel(new String[] { "(Seleccione un Usuario)" }));
        boxUsuarios.setPreferredSize(new java.awt.Dimension(150, 20));

        btnComprobar.setText("BUSCAR");
        btnComprobar.setPreferredSize(new java.awt.Dimension(150, 20));
        btnComprobar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnComprobarActionPerformed(evt);
            }
        });

        jScrollPane1.setViewportView(panelUsuarios);

        lblError.setForeground(new java.awt.Color(255, 0, 0));
        lblError.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        lblError.setText("Por favor escoja un Usuario");
        lblError.setPreferredSize(new java.awt.Dimension(25, 25));

        btnComprobar3.setText("REGRESAR A MENU PRINCIPAL");
        btnComprobar3.setPreferredSize(new java.awt.Dimension(150, 20));
        btnComprobar3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnComprobar3ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2.setLayout(jPanel2Layout);
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addGroup(jPanel2Layout.createSequentialGroup()
                                .addGap(0, 72, Short.MAX_VALUE)
                                .addComponent(lblError, javax.swing.GroupLayout.PREFERRED_SIZE, 366, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(jPanel2Layout.createSequentialGroup()
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 60, Short.MAX_VALUE)
                                .addComponent(jLabel1)
                                .addGap(68, 68, 68)
                                .addComponent(boxUsuarios, javax.swing.GroupLayout.PREFERRED_SIZE, 187, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(jPanel2Layout.createSequentialGroup()
                                .addGap(23, 23, 23)
                                .addComponent(btnComprobar3, javax.swing.GroupLayout.PREFERRED_SIZE, 230, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addComponent(btnComprobar, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                        .addGap(0, 60, Short.MAX_VALUE))
                    .addComponent(jScrollPane1))
                .addContainerGap())
        );
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addGap(12, 12, 12)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel1)
                    .addComponent(boxUsuarios, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btnComprobar, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(btnComprobar3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED, 20, Short.MAX_VALUE)
                .addComponent(lblError, javax.swing.GroupLayout.PREFERRED_SIZE, 20, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 205, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(16, 16, 16))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(20, 20, 20)
                        .addComponent(jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(10, 10, 10)
                        .addComponent(jSeparator2, javax.swing.GroupLayout.PREFERRED_SIZE, 13, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 10, Short.MAX_VALUE)
                        .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(40, 40, 40)
                        .addComponent(lbltitulo, javax.swing.GroupLayout.PREFERRED_SIZE, 469, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(0, 0, Short.MAX_VALUE)))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(lbltitulo, javax.swing.GroupLayout.PREFERRED_SIZE, 27, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jPanel2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jSeparator2))
                .addContainerGap())
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnComprobarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnComprobarActionPerformed
        lblError.setText("");
        String nombre = boxUsuarios.getSelectedItem().toString();
        if (nombre.equals("(Seleccione un Usuario)")) {
            lblError.setText("Por favor escoja un Usuario");
        } else {
            try {

                String url1 = "http://127.0.0.1:5000/user_vuelo/" + nombre;
                String res1 = crearConexion.crearConexion(url1, "HTTP");
                System.out.println("" + res1);
                String inici = "<html><head></head><body><h1>Vuelos asignados - " + nombre + "</h1><table border=\"1\"><tr><td>Id vuelo</td>"
                        + "<td>Lugar de Salida</td>"
                        + "<td>Lugar de Llegada</td>"
                        + "<td>Fecha de llegada</td>"
                        + "</tr>";
                String medio = "";
                String fin = "</table></body></html>";
                StringTokenizer tokens1 = new StringTokenizer(res1, ",");
                while (tokens1.hasMoreTokens()) {
                    String a = tokens1.nextToken();
                    String b = tokens1.nextToken();
                    String llegada = tokens1.nextToken();
                    String salida = tokens1.nextToken();
                    String fecha = tokens1.nextToken();
                    fecha = fecha.replace("-", " ");
                    medio = medio + "<tr><td>" + a + "</td>"
                            + "<td>" + salida + "</td>"
                            + "<td>" + llegada + "</td>"
                            + "<td>" + fecha + "</td>"
                            + "</tr>";
                }
                String contenido = inici + medio + fin;
                panelUsuarios.setText(contenido);

            } catch (Exception e) {
                showMessageDialog(null, "No hay usuarios disponibles");
            }
        }

        // TODO add your handling code here:
    }//GEN-LAST:event_btnComprobarActionPerformed

    private void btnComprobar3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnComprobar3ActionPerformed
        setVisible(false);
        dispose();
        menu.setVisible(true);           // TODO add your handling code here:
    }//GEN-LAST:event_btnComprobar3ActionPerformed

    /**
     * @param args the command line arguments
     */

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JComboBox boxUsuarios;
    private javax.swing.JButton btnComprobar;
    private javax.swing.JButton btnComprobar3;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JScrollPane jScrollPane3;
    private javax.swing.JSeparator jSeparator2;
    private javax.swing.JLabel lblError;
    private javax.swing.JLabel lbltitulo;
    private javax.swing.JTextPane panelAeropuertos;
    private javax.swing.JTextPane panelUsuarios;
    private javax.swing.JTextPane panelVuelos;
    // End of variables declaration//GEN-END:variables
}
