/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codigo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;
import javax.net.ssl.HttpsURLConnection;

/**
 *
 * @author edwin
 */
public class crearConexion {
    
    public static String crearConexion(String request, String protocolo) {

        String responce = "";

        BufferedReader rd = null;

        try {

            URL url = new URL(request);

            if (protocolo.equals("HTTPS")) {

                HttpsURLConnection conn1 = (HttpsURLConnection) url.openConnection();


                rd = new BufferedReader(new InputStreamReader(conn1.getInputStream()));

            } else {

                URLConnection conn2 = url.openConnection();

                rd = new BufferedReader(new InputStreamReader(conn2.getInputStream()));

            }



            String line;



            while ((line = rd.readLine()) != null) {

                //Process line...

                responce += line;

            }



        } catch (Exception e) {

            System.out.println("Web request failed");

        // Web request failed

        } finally {

            if (rd != null) {

                try {

                    rd.close();

                } catch (IOException ex) {

                    System.out.println("Problema al cerrar el objeto lector");

                }

            }

        }



        return responce;

    }
    
}
