/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codigo;

/**
 *
 * @author Braian
 */
public class nodoUsuario {

    String Nombre, contraseña, nick, direccion, direccionActual;
    int telefono, tarjetaCredito;
    nodoUsuario sig;

    public nodoUsuario() {
        Nombre = "";
        contraseña = "";
        nick = "";
        direccion = "";
        direccionActual = "";
        telefono = 0;
        tarjetaCredito = 0;
        sig = null;
    }

}
