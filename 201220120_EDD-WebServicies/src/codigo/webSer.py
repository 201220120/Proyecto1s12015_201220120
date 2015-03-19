#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask
import math
import os
import random
app = Flask(__name__)
#from soaplib.core.wsdl import WSDL

class nodoListaAeropuerto():
    def __init__(nodoRaiz, nom, p, pa):
        nodoRaiz.nombre = nom
        nodoRaiz.pais   = p
        nodoRaiz.password = pa
        nodoRaiz.siguiente = None
        nodoRaiz.anterior = None


class listaAeropuerto():
    def __init__(nodoRaiz):
        nodoRaiz.cabeza = None
        nodoRaiz.fin    = None
        nodoRaiz.Grafica = ""

    def insertar(nodoRaiz, nombre, pais, password):
        nuevo = nodoListaAeropuerto(nombre, pais, password)
        if nodoRaiz.cabeza == None:
            nodoRaiz.cabeza = nuevo
            nodoRaiz.fin    = nuevo
        else:
            nuevo.siguiente = nodoRaiz.cabeza
            nodoRaiz.cabeza.anterior = nuevo
            nodoRaiz.cabeza = nuevo
            
    def dibujar2(self):
        iterador = self.cabeza
        self.Grafica = ""
        contenido = ""
        while iterador != None:
            if iterador.siguiente != None:
                contenido = contenido + "\"" + iterador.nombre + "\"  -- \"" + iterador.siguiente.nombre + "\" \n"
                
                contenido = contenido + "\"" + iterador.siguiente.nombre + "\"  -- \"" + iterador.nombre + "\" \n"
            iterador = iterador.siguiente
        self.Grafica = contenido 
        
                
    def getDireccionAeropuerto(nodoRaiz, nombre):
        iterador = nodoRaiz.cabeza
        nom = ""
        while iterador != None:

            if iterador.nombre == nombre:
                nom = iterador.pais

                break
            iterador = iterador.siguiente
        return "%s" % nom
        
    def mostrar(nodoRaiz):
        iterador = nodoRaiz.cabeza
        while iterador != None:
            print "Nombre = %s   Pais = %s   Password = %s" % (iterador.nombre, iterador.pais, iterador.password)
            iterador = iterador.siguiente
        print "------------------------------------------------------------------------------------------"

    def eliminar(nodoRaiz, n):
        iterador = nodoRaiz.cabeza
        while iterador != None:
            if iterador.nombre == n:
                if iterador == nodoRaiz.cabeza:
                    if iterador.siguiente != None:
                        iterador.siguiente.anterior == None
                        nodoRaiz.cabeza = iterador.siguiente
                    else:
                        nodoRaiz.cabeza = nodoRaiz.fin = None
                else:
                    if iterador == nodoRaiz.fin:
                        iterador.anterior.siguiente = None
                        nodoRaiz.fin = iterador.anterior
                    else:
                        aux1 = iterador.anterior
                        aux2 = iterador.siguiente
                        aux1.siguiente = aux2
                        aux2.anterior = aux1
            iterador = iterador.siguiente

    def dibujarAeropuerto(nodoRaiz):
        iterador = nodoRaiz.cabeza
        print hola
        contenido = ""
        while iterador != None:
            if iterador.siguiente != None:
                print contenido
                contenido = contenido + "\"" + iterador.nombre + "\"  -- \"" + iterador.siguiente.nombre + "\" \n" 
                contenido = contenido + "\"" + iterador.siguiente.nombre + "\"  -- \"" + iterador.nombre + "\" \n"
            print contenido
            iterador = iterador.siguiente
        contenido = "%s" % contenido
        print contenido
        return contenido

    def modifcar(nodoRaiz, nombre, nuevoNombre, pais, password):
        nodoRaiz.eliminar(nombre)
        nodoRaiz.insertar(nuevoNombre, pais, password)

    def dibujar(nodoRaiz):
        iterador = nodoRaiz.cabeza
        contenido = ""
        while iterador != None:
            contenido = contenido + "\"" + iterador.nombre + "\"" + "--"
            iterador = iterador.siguiente
        contenido = contenido + "Fin"
        nodoRaiz.Grafica = contenido
 

    def mostrar1(nodoRaiz):
        iterador = nodoRaiz.cabeza
        respuesta = ""
        inicio = "<html><head></head><body><h1>Aeropuertos Disponibles</h1><table border=\"1\"><tr><td><h2>Nombre</h2></td><td><h2>Pais</h2></td></tr>"
        fin = "</table></body></html>"
        while iterador != None:
            respuesta = respuesta + "<tr><td>" + iterador.nombre + "</td>" + "<td>" + iterador.pais + "</td></tr>"
            iterador = iterador.siguiente
        contenido = "%s \n %s \n %s" % (inicio, respuesta, fin)
        return contenido

    def mostrar(nodoRaiz):
        iterador = nodoRaiz.cabeza
        respuesta = ""
        while iterador != None:
            respuesta = respuesta + iterador.nombre + ","
            iterador = iterador.siguiente

        return respuesta
            




#-----------------------------------------------------------------ARBOL DE USUARIOS-----------------------------------------------------------

class nodoUsuarios():
    def __init__(nodoRaiz, nombre, password, user, direccion, telefono, tarjeta, direcionActual):
        nodoRaiz.nombre = nombre
        nodoRaiz.password = password
        nodoRaiz.user = user
        nodoRaiz.direccion = direccion
        nodoRaiz.telefono = telefono
        nodoRaiz.tarjeta = tarjeta
        nodoRaiz.direcionActual = direcionActual
        nodoRaiz.fe = 0
        nodoRaiz.izquierda = None
        nodoRaiz.derecha = None
    
    def toString(nodoRaiz):
        cadena = "\"" + nodoRaiz.user + "\""
        return cadena

class arbolUsuarios():

    def __init__(nodoRaiz):
        nodoRaiz.raiz = None
        nodoRaiz.recorrido = ""
        nodoRaiz.Grafica = ""



    def buscar(nodoRaiz, nomUser, r):
        try:
            if nodoRaiz.raiz == None:
                return None;
            else:
                if r.user == nomUser:
                    return r;
                else:
                    if r.user < nomUser:
                        return nodoRaiz.buscar(nomUser, r.derecha)
                    else:
                        return nodoRaiz.buscar(nomUser, r.izquierda)
        except Exception, e:
            return None

        
    def modificar(nodoRaiz, n, p, d, t, tar, da, userViejo):
        nodo = nodoRaiz.buscar(userViejo, nodoRaiz.raiz)
        if nodo != None:
            nodo.nombre = n
            nodo.password = p
            #nodo.user = u
            nodo.direccion = d
            nodo.telefono = t
            nodo.tarjeta = tar
            nodo.direcionActual = da
        else: 
            print "El usuario no existe"

    def set_direcionActual(nodoRaiz, userViejo, dirActual):
        print userViejo
        print dirActual
        nodo = nodoRaiz.buscar(userViejo, nodoRaiz.raiz)
        if nodo != None:
            nodo.direcionActual = dirActual
            print nodo.direcionActual
            
    def getDatosPDF(nodoRaiz, nombre, cod=0):
        nodo = nodoRaiz.buscar(nombre, nodoRaiz.raiz)
        contenido = ""
        if nodo != None:
            if cod == 0:
                nombre = "%s" % nodo.nombre
                password = "%s" % nodo.password
                user = "%s" % nodo.user
                direccion = "%s" % nodo.direccion
                telefono = "%s" % nodo.telefono
                tarjeta = "%s" % nodo.tarjeta
                direcionActual = "%s" % nodo.direcionActual
                inicio = nombre + "," + password + "," + user + "," + direccion + "," + telefono + "," + tarjeta + "," + direcionActual
                contenido = "%s" % inicio


        return contenido

    
    def getDatos(nodoRaiz, nombre, cod=0):
        nodo = nodoRaiz.buscar(nombre, nodoRaiz.raiz)
        contenido = ""
        if nodo != None:
            if cod == 0:
                nombre = "%s" % nodo.nombre
                password = "%s" % nodo.password
                user = "%s" % nodo.user
                direccion = "%s" % nodo.direccion
                telefono = "%s" % nodo.telefono
                tarjeta = "%s" % nodo.tarjeta
                direcionActual = "%s" % nodo.direcionActual
                inicio = "<html><head></head><body><h1></h1><table border=\"1\">"
                inici2 = "<tr><td>Nombre</td> <td>Password</td> <td>User</td> <td>Direccion</td> <td>Telefono</td> <td>Tarjeta</td><td>Direcion Actual</td></tr>"
                fin = "</table></body></html>"
                medio = "<tr>" + "<td>" + nombre + "</td>" + "<td>" + password + "</td>" + "<td>" + user + "</td>" + "<td>" + direccion + "</td>" + "<td>" + telefono + "</td>" + "<td>" + tarjeta + "</td>" + "<td>" + direcionActual + "</td>" + "</tr>"
                contenido = "%s %s %s %s" % (inicio, inici2, medio, fin)
            else:
                nombre = "%s" % nodo.nombre
                password = "%s" % nodo.password
                user = "%s" % nodo.user
                direccion = "%s" % nodo.direccion
                telefono = "%s" % nodo.telefono
                tarjeta = "%s" % nodo.tarjeta
                direcionActual = "%s" % nodo.direcionActual
                inicio = "<table border=\"1\">"
                inici2 = "<tr><td>Nombre</td> <td>Password</td> <td>User</td> <td>Direccion</td> <td>Telefono</td> <td>Tarjeta</td><td>Direcion Actual</td></tr>"
                medio = "<tr>" + "<td>" + nombre + "</td>" + "<td>" + password + "</td>" + "<td>" + user + "</td>" + "<td>" + direccion + "</td>" + "<td>" + telefono + "</td>" + "<td>" + tarjeta + "</td>" + "<td>" + direcionActual + "</td>" + "</tr>"
                fin = "</table>"
                contenido = " %s %s %s %s <br><br>" % (inicio, inici2, medio, fin)


        return contenido


        

    def get_fe(nodoRaiz, x):
        if x == None:
            return -1
        else:
            return x.fe

    def rotacionIzquierda(nodoRaiz, c):
        aux = c.izquierda
        c.izquierda = aux.derecha
        aux.derecha = c
        c.fe = (max (nodoRaiz.get_fe(c.izquierda), nodoRaiz.get_fe(c.derecha))) + 1
        aux.fe = (max (nodoRaiz.get_fe(aux.izquierda), nodoRaiz.get_fe(aux.derecha))) + 1
        return aux

    def rotacionDerecha(nodoRaiz, c):
        aux = c.derecha
        c.derecha = aux.izquierda
        aux.izquierda = c
        c.fe = (max(nodoRaiz.get_fe(c.izquierda), nodoRaiz.get_fe(c.derecha))) + 1
        aux.fe = (max (nodoRaiz.get_fe(aux.izquierda), nodoRaiz.get_fe(aux.derecha))) + 1 
        return aux

    def rotacionDobleIzquierda(nodoRaiz, c):
        c.izquierda = nodoRaiz.rotacionDerecha(c.izquierda)
        temporal = nodoRaiz.rotacionIzquierda(c)
        return temporal

    def rotacionDobleDerecha(c):
        c.derecha = nodoRaiz.rotacionIzquierda(c.derecha)
        temporal = nodoRaiz.rotacionDerecha()
        return temporal

    def insertarAVL(nodoRaiz, nuevo, subAr):
        nuevoPadre = subAr
        if nuevo.user < subAr.user:
            if subAr.izquierda == None:
                subAr.izquierda = nuevo
            else:
                subAr.izquierda = nodoRaiz.insertarAVL(nuevo, subAr.izquierda)
                tmp = nodoRaiz.get_fe(subAr.izquierda) - nodoRaiz.get_fe(subAr.derecha)
                if tmp == 2:
                    if nuevo.user < subAr.izquierda.user:
                        nuevoPadre = nodoRaiz.rotacionIzquierda(subAr)
                    else:
                        nuevoPadre = rotacionDobleIzquierda(subAr)
        else:
            if nuevo.user > subAr.user:
                if subAr.derecha == None:
                    subAr.derecha = nuevo;
                else:
                    subAr.derecha = nodoRaiz.insertarAVL(nuevo, subAr.derecha)
                    tmp1 = nodoRaiz.get_fe(subAr.derecha) - nodoRaiz.get_fe(subAr.izquierda)
                    if tmp1 == 2:
                        if nuevo.user > subAr.derecha.user:
                            nuevoPadre = nodoRaiz.rotacionDerecha(subAr)
                        else:
                            nuevoPadre = nodoRaiz.rotacionDobleDerecha(subAr)
        
        if subAr.izquierda == None and subAr.derecha != None:
            subAr.fe = subAr.derecha.fe + 1
        else:
            if subAr.derecha == None and subAr.izquierda != None:
                subAr.fe = subAr.izquierda.fe + 1
            else:
                subAr.fe = (max (nodoRaiz.get_fe(subAr.izquierda), nodoRaiz.get_fe(subAr.derecha))) + 1

        return nuevoPadre

    def insertar(nodoRaiz, nombre, password, user, direccion, telefono, tarjeta, direcionActual):
        n = nodoUsuarios(nombre, password, user, direccion, telefono, tarjeta, direcionActual)
        if nodoRaiz.raiz == None:
            nodoRaiz.raiz = n
        else:
            nodoRaiz.raiz = nodoRaiz.insertarAVL(n, nodoRaiz.raiz)



    def preorden (nodoRaiz, r):
        if (r != None):
            print "  %s " % r.nombre
            nodoRaiz.preorden(r.izquierda)
            nodoRaiz.preorden(r.derecha)



    def ToDot(nodoRaiz, node):
        cont = ""
        if node.izquierda != None:
            cont = cont + node.toString() + "--" + node.izquierda.toString() + "\n"
            cont = cont + nodoRaiz.ToDot(node.izquierda)
        if node.derecha != None:
            cont = cont + node.toString() + "--" + node.derecha.toString() + "\n"
            cont = cont + nodoRaiz.ToDot(node.derecha)
        return cont

    def ToDotGraph(nodoRaiz):
        contenido = ""
        if nodoRaiz.raiz == None:
            contenido = " Arbol_Vacio"
            nodoRaiz.Grafica = contenido 
        else:
            if nodoRaiz.raiz.izquierda == None and nodoRaiz.raiz.derecha == None:
                contenido = nodoRaiz.raiz.user 
                nodoRaiz.Grafica = contenido 
            else:
                contenido = nodoRaiz.ToDot(nodoRaiz.raiz)
                nodoRaiz.Grafica = contenido 



    def usuarioExiste(nodoRaiz, username):
        iterador = nodoRaiz.raiz
        respuesta = False
        while iterador != None:
            if iterador.user == username:
                respuesta = True
                break
            if iterador.user < username:
                iterador = iterador.derecha
            else:
                iterador = iterador.izquierda
        return respuesta
    
    def validarUsuario(nodoRaiz, username, password):
        iterador = nodoRaiz.raiz
        respuesta = False
        while iterador != None:
            if iterador.user == username and iterador.password == password:
                respuesta = True
                break
            if iterador.user < username:
                iterador = iterador.derecha
            else:
                iterador = iterador.izquierda
        return respuesta

    def concatenar(nodoRaiz, nodo):
        a = "%s" % nodo.user
        nodoRaiz.recorrido = nodoRaiz.recorrido + a + ","

    def preorden1 (nodoRaiz, r):
        if (r != None):
            #return "%s,"%r.idd
            nodoRaiz.concatenar(r)
            nodoRaiz.preorden1(r.izquierda)
            nodoRaiz.preorden1(r.derecha)

    def obtenerNodoReemplazo(nodoRaiz, nodoReemp):
        reemplazarPadre = nodoReemp
        reemplazo = nodoReemp
        auxiliar = nodoReemp.derecha
        while auxiliar != None:
            reemplazarPadre = reemplazo
            reemplazo = auxiliar
            auxiliar = auxiliar.izquierda
        if reemplazo != nodoReemp.derecha:
            reemplazarPadre.izquierda = reemplazo.derecha
            reemplazo.derecha = nodoReemp.derecha
        return reemplazo

        

    def eliminar(nodoRaiz, username):
        auxiliar = nodoRaiz.raiz
        padre = nodoRaiz.raiz
        esHijoIzq = True
        nodo1 = None
        while auxiliar.user != username:
            padre = auxiliar
            if username < auxiliar.user:
                esHijoIzq = True
                auxiliar = auxiliar.izquierda
            else:
                esHijoIzq = False
                auxiliar = auxiliar.derecha
            if auxiliar == None:
                return False
        #fin del while
        if auxiliar.izquierda == None and auxiliar.derecha == None:
            if auxiliar == nodoRaiz.raiz:
                nodoRaiz.raiz = None
            else:
                if esHijoIzq == True:
                    padre.izquierda = None
                else:
                    padre.derecha = None
        else:
            if auxiliar.derecha == None:
                #nodo1 = auxiliar.derecha
                #nodoRaiz.insertarAVL(auxiliar.derecha,nodoRaiz.raiz)
                if auxiliar == nodoRaiz.raiz:
                    nodoRaiz.raiz = auxiliar.izquierda
                else:
                    if esHijoIzq == True:
                        padre.izquierda = auxiliar.izquierda
                    else:
                        padre.derecha = auxiliar.izquierda
            else:
                if auxiliar.izquierda == None:
                    #nodo1 = auxiliar.izquierda
                    #nodoRaiz.insertarAVL(auxiliar.izquierda,nodoRaiz.raiz)
                    if auxiliar == nodoRaiz.raiz:
                        nodoRaiz.raiz = auxiliar.derecha
                    else:
                        if esHijoIzq == True:
                            padre.izquierda = auxiliar.derecha
                        else:
                            padre.derecha = auxiliar.izquierda
                else:
                    reemplazo = nodoRaiz.obtenerNodoReemplazo(auxiliar)
                    if auxiliar == nodoRaiz.raiz:
                        nodoRaiz.raiz = reemplazo
                    else:
                        if esHijoIzq == True:
                            padre.izquierda = reemplazo
                        else:
                            padre.derecha = reemplazo
                    reemplazo.izquierda = auxiliar.izquierda
                    #nodo1 = reemplazo
                    #nodoRaiz.insertarAVL(reemplazo,nodoRaiz.raiz)
        return True


        




#---------------------------------------------------------LISTA USUARIOS ASIGNADOS-------------------------------------------------------
class nodoUsuariosAsignados():
    def __init__(nodoRaiz, nombreUsuario):
        nodoRaiz.nombreUsuario = nombreUsuario
        nodoRaiz.siguiente = None
        nodoRaiz.anterior = None

class ListaUsuariosAsignados():
    def __init__(nodoRaiz):
        nodoRaiz.cabeza = None
        nodoRaiz.fin    = None
        nodoRaiz.cont = 0
        nodoRaiz.tempo = 0 
        nodoRaiz.nodoCabeza = ""

    def insertar(nodoRaiz, nombreUsuario):
        nuevo = nodoUsuariosAsignados(nombreUsuario)
        if nodoRaiz.cabeza == None:
            nodoRaiz.cabeza = nuevo
            nodoRaiz.fin    = nuevo
        else:
            nuevo.siguiente = nodoRaiz.cabeza
            nodoRaiz.cabeza.anterior = nuevo
            nodoRaiz.cabeza = nuevo
    
    def mostrar(nodoRaiz):
        iterador = nodoRaiz.cabeza
        while iterador != None:
            print "Nombre = %s  " % iterador.nombreUsuario
            iterador = iterador.siguiente
        print "------------------------------------------------------------------------------------------"
    
    def eliminar(nodoRaiz, n):
        iterador = nodoRaiz.cabeza
        while iterador != None:
            if iterador.nombreUsuario == n:
                if iterador == nodoRaiz.cabeza:
                    if iterador.siguiente != None:
                        iterador.siguiente.anterior == None
                        nodoRaiz.cabeza = iterador.siguiente
                    else:
                        nodoRaiz.cabeza = nodoRaiz.fin = None
                else:
                    if iterador == nodoRaiz.fin:
                        iterador.anterior.siguiente = None
                        nodoRaiz.fin = iterador.anterior
                    else:
                        aux1 = iterador.anterior
                        aux2 = iterador.siguiente
                        aux1.siguiente = aux2
                        aux2.anterior = aux1
                break
            iterador = iterador.siguiente
    
    def modifcar(nodoRaiz, nombreUsuario, nuevoNombre):
        nodoRaiz.eliminar(nombreUsuario)
        nodoRaiz.insertar(nuevoNombre)

    def get_nodos(nodoRaiz):
        cont = ""
        iterador = nodoRaiz.cabeza
        while iterador != None:
            cont = cont + "\"" + iterador.nombreUsuario + "\"  "
            iterador = iterador.siguiente
        return cont

    def get_nodoCabeza(nodoRaiz, b, c):
        a = ""
        if b == 1:
            nodoRaiz.cont = c
            a = "nodo%s [label=\"%s\"] \n" % (nodoRaiz.cont, nodoRaiz.cabeza.nombreUsuario)
            nodoRaiz.nodoCabeza = "nodo%s" % nodoRaiz.cont
            
        else:
            a = "nodo%s" % nodoRaiz.cont
            nodoRaiz.cont = nodoRaiz.cont + 1 
        
        return a

    def getCont(nodoRaiz):
        return nodoRaiz.cont 

    def dibujar(nodoRaiz):
        iterador = nodoRaiz.cabeza
        aux3 = "%s" % nodoRaiz.get_nodos()
        contenido = " subgraph cluster_0 { node [style=filled] " + aux3  + " color=blue}"
        #"node [shape=record fontsize=8 fontname=\"Verdana\"]; \n" + 
        tmp = ""
        #contenido = ""
        while iterador != None:
            if iterador.siguiente != None:
                #print " ENTRO"
                contenido = "\n" + contenido + "{rank=same " + iterador.nombreUsuario + "  " + iterador.siguiente.nombreUsuario + "}"
                tmp = "%s" % iterador.nombreUsuario         
                contenido = contenido + "\"" + iterador.nombreUsuario + "\"" + "--" + iterador.siguiente.nombreUsuario + "\n"       

            iterador = iterador.siguiente

        return contenido

    def buscar(nodoRaiz, nombre):
        iterador = nodoRaiz.cabeza
        nom = ""
        while iterador != None:
            if iterador.nombreUsuario == nombre:
                nom = nombre
                break
            iterador = iterador.siguiente
        return "%s" % nom


#-------------------------------------------------------------ARBOL VUELOS-----------------------------------------------------------------
class nodoVuelos():
    def __init__(nodoRaiz, lugarLlegada, aeropuerto, horaFechaSalida, horaFechaLlegada, cantidadPrimeraClase, costoPrimeraClase, cantidadClaseTurista, costoClaseTurista, cantidadClaseEjecutiva, costoClaseEjecutiva, idd):
        nodoRaiz.lugarLlegada = lugarLlegada #El lugar de salida se sabe que es del mismo aeropuerto y el aeropuerto debe existir sino este no puede ser asignado
        nodoRaiz.aeropuerto = aeropuerto
        nodoRaiz.horaFechaSalida = horaFechaSalida
        nodoRaiz.horaFechaLlegada = horaFechaLlegada
        nodoRaiz.cantidadPrimeraClase = cantidadPrimeraClase
        nodoRaiz.costoPrimeraClase = costoPrimeraClase
        nodoRaiz.cantidadClaseTurista = cantidadClaseTurista
        nodoRaiz.costoClaseTurista = costoClaseTurista
        nodoRaiz.cantidadClaseEjecutiva = cantidadClaseEjecutiva
        nodoRaiz.costoClaseEjecutiva = costoClaseEjecutiva
        nodoRaiz.EstadoInicial = "En-Aeropuerto"     #el cual por defecto serÃ¡ â€œEn aeropuertoâ€?
        nodoRaiz.idd = idd     # Ãºnico y es generado por el sistema
        nodoRaiz.izquierda = None
        nodoRaiz.derecha = None
        nodoRaiz.usuariosAsignados = None
        nodoRaiz.fe = 0
        nodoRaiz.vuelosEjecutivo = 0
        nodoRaiz.vuelosTurista = 0
        nodoRaiz.vuelosPrimeraClase = 0

    def toString(nodoRaiz):
        tempo = "%s" % nodoRaiz.idd
        cadena = "\"" + tempo + "\""
        return cadena

class arbolVuelos():

    def __init__(nodoRaiz):
        nodoRaiz.raiz = None
        nodoRaiz.contador = 0
        nodoRaiz.recorrido = ""
        nodoRaiz.recorrido2 = ""
        nodoRaiz.listado = ""
        nodoRaiz.listaUser = ""
        nodoRaiz.listaCategoria = ""
        
        nodoRaiz.listaVueloAeropuerto = ""
        nodoRaiz.listaUsuarios_Asignados = ""
        nodoRaiz.contador = 0
        nodoRaiz.cont = 0
        nodoRaiz.cont_temporal = 0;
        
        nodoRaiz.Grafica = ""

    def buscar(nodoRaiz, idd1, r):
        try:
            if nodoRaiz.raiz == None:
                return None
            else:
                if r.idd == idd1:
                    #print "se encontro el nodo"
                    return r
                else:
                    if r.idd < idd1:
                        return nodoRaiz.buscar(idd1, r.derecha)
                    else:
                        return nodoRaiz.buscar(idd1, r.izquierda)
        except Exception, e:
            #print "ERROR"
            return None


    def get_llegda(nodoRaiz, dato):
        nodo = nodoRaiz.buscar(dato, nodoRaiz.raiz)
        if nodo != None:
            return "%s" % nodo.lugarLlegada
        return ""



    def get_fe(nodoRaiz, x):
        if x == None:
            return -1
        else:
            return x.fe


    def preorden (self, r, cont):
        if (r != None):
            a = "%s" % r.idd
            cont = cont + a + ","
            return self.preorden(r.izquierda, cont)
            return self.preorden(r.derecha, cont)
        return cont

    def preorder_ua(self, r, user_name):
        if r != None:
            self.concatenar_user(r, user_name)
            self.preorder_ua(r.izquierda, user_name)
            self.preorder_ua(r.derecha, user_name)
            
    def preorder_uaPDF(self, r, user_name):
        if r != None:
            self.concatenar_userPDF(r, user_name)
            self.preorder_uaPDF(r.izquierda, user_name)
            self.preorder_uaPDF(r.derecha, user_name)
                        
    def concatenar_user(self, r, un):
        if r.usuariosAsignados != None:
            iterador = r.usuariosAsignados.cabeza
            while iterador != None:
                if iterador.nombreUsuario == un:
                    costoClaseEjecutiva = "%s" % r.costoClaseEjecutiva
                    costoClaseTurista = "%s" % r.costoClaseTurista
                    cantidadClaseEjecutiva = "%s" % r.cantidadClaseEjecutiva
                    lugarLlegada = "%s" % r.lugarLlegada
                    aeropuerto = "%s" % r.aeropuerto
                    horaFechaSalida = "%s" % r.horaFechaSalida
                    horaFechaLlegada = "%s" % r.horaFechaLlegada
                    cantidadPrimeraClase = "%s" % r.cantidadPrimeraClase
                    costoPrimeraClase = "%s" % r.costoPrimeraClase
                    cantidadClaseTurista = "%s" % r.cantidadClaseTurista
                    idd = "%s" % r.idd
                    inicio = "<table border=\"1\"><tr><td>Id</td><td>lugarLlegada</td><td>aeropuerto</td><td>horaFechaSalida</td><td>horaFechaLlegada</td><td>cantidadPrimeraClase</td><td>costoPrimeraClase</td><td>cantidadClaseTurista</td><td>costoClaseTurista</td><td>cantidadClaseEjecutiva</td><td>costoClaseEjecutiva</td></tr>"
                    medio = "<td>" + idd + "<td>" + lugarLlegada + "</td>" + "<td>" + aeropuerto + "</td>" + "<td>" + horaFechaSalida + "</td>" + "<td>" + horaFechaLlegada + "</td>" + "<td>" + cantidadPrimeraClase + "</td>" + "<td>" + costoPrimeraClase + "</td>" + "<td>" + cantidadClaseTurista + "</td>" + "<td>" + costoClaseTurista + "</td>" + "<td>" + cantidadClaseEjecutiva + "</td>" + "<td>" + costoClaseEjecutiva + "</td>"
                    contenido = inicio + medio + "</table><br><br>"
                    self.listaUsuarios_Asignados = self.listaUsuarios_Asignados + contenido



                iterador = iterador.siguiente
                
    def concatenar_userPDF(self, r, un):
        if r.usuariosAsignados != None:
            iterador = r.usuariosAsignados.cabeza
            while iterador != None:
                if iterador.nombreUsuario == un:
                    costoClaseEjecutiva = "%s" % r.costoClaseEjecutiva
                    costoClaseTurista = "%s" % r.costoClaseTurista
                    cantidadClaseEjecutiva = "%s" % r.cantidadClaseEjecutiva
                    lugarLlegada = "%s" % r.lugarLlegada
                    aeropuerto = "%s" % r.aeropuerto
                    horaFechaSalida = "%s" % r.horaFechaSalida
                    horaFechaLlegada = "%s" % r.horaFechaLlegada
                    cantidadPrimeraClase = "%s" % r.cantidadPrimeraClase
                    costoPrimeraClase = "%s" % r.costoPrimeraClase
                    cantidadClaseTurista = "%s" % r.cantidadClaseTurista
                    
                    idd = "%s" % r.idd
                    contenido = idd + "," + lugarLlegada + "," + aeropuerto + "," + horaFechaSalida + "," + horaFechaLlegada + "," + cantidadPrimeraClase + "," + costoPrimeraClase + "," + cantidadClaseTurista + "," + costoClaseTurista + "," + cantidadClaseEjecutiva + "," + costoClaseEjecutiva + ","
                    self.listaUsuarios_Asignados = self.listaUsuarios_Asignados + contenido



                iterador = iterador.siguiente

    def concatenar(self, nodo):
        a = "%s" % nodo.idd
        self.recorrido = self.recorrido + a + ","                   
    def rotacionIzquierda(nodoRaiz, c):
        aux = c.izquierda
        c.izquierda = aux.derecha
        aux.derecha = c
        c.fe = (max (nodoRaiz.get_fe(c.izquierda), nodoRaiz.get_fe(c.derecha))) + 1
        aux.fe = (max (nodoRaiz.get_fe(aux.izquierda), nodoRaiz.get_fe(aux.derecha))) + 1
        return aux

    def rotacionDerecha(nodoRaiz, c):
        aux = c.derecha
        c.derecha = aux.izquierda
        aux.izquierda = c
        c.fe = (max(nodoRaiz.get_fe(c.izquierda), nodoRaiz.get_fe(c.derecha))) + 1
        aux.fe = (max (nodoRaiz.get_fe(aux.izquierda), nodoRaiz.get_fe(aux.derecha))) + 1 
        return aux

    def rotacionDobleIzquierda(nodoRaiz, c):
        c.izquierda = nodoRaiz.rotacionDerecha(c.izquierda)
        temporal = nodoRaiz.rotacionIzquierda(c)
        return temporal

    def rotacionDobleDerecha(c):
        c.derecha = nodoRaiz.rotacionIzquierda(c.derecha)
        temporal = nodoRaiz.rotacionDerecha()
        return temporal
    
    def getCont(nodoRaiz):
        a = "%s" % nodoRaiz.contador
        return a

    def insertarAVL(nodoRaiz, nuevo, subAr):
        nuevoPadre = subAr
        if nuevo.idd < subAr.idd:
            if subAr.izquierda == None:
                subAr.izquierda = nuevo
            else:
                subAr.izquierda = nodoRaiz.insertarAVL(nuevo, subAr.izquierda)
                tmp = nodoRaiz.get_fe(subAr.izquierda) - nodoRaiz.get_fe(subAr.derecha)
                if tmp == 2:
                    if nuevo.idd < subAr.izquierda.idd:
                        nuevoPadre = nodoRaiz.rotacionIzquierda(subAr)
                    else:
                        nuevoPadre = rotacionDobleIzquierda(subAr)
        else:
            if nuevo.idd > subAr.idd:
                if subAr.derecha == None:
                    subAr.derecha = nuevo;
                else:
                    subAr.derecha = nodoRaiz.insertarAVL(nuevo, subAr.derecha)
                    tmp1 = nodoRaiz.get_fe(subAr.derecha) - nodoRaiz.get_fe(subAr.izquierda)
                    if tmp1 == 2:
                        if nuevo.idd > subAr.derecha.idd:
                            nuevoPadre = nodoRaiz.rotacionDerecha(subAr)
                        else:
                            nuevoPadre = nodoRaiz.rotacionDobleDerecha(subAr)
        
        if subAr.izquierda == None and subAr.derecha != None:
            subAr.fe = subAr.derecha.fe + 1
        else:
            if subAr.derecha == None and subAr.izquierda != None:
                subAr.fe = subAr.izquierda.fe + 1
            else:
                subAr.fe = (max (nodoRaiz.get_fe(subAr.izquierda), nodoRaiz.get_fe(subAr.derecha))) + 1
        return nuevoPadre

    def insertar(nodoRaiz, lugarLlegada, aeropuerto, horaFechaSalida, horaFechaLlegada, cantidadPrimeraClase, costoPrimeraClase, cantidadClaseTurista, costoClaseTurista, cantidadClaseEjecutiva, costoClaseEjecutiva):
        #a = nodoRaiz.generarId()
        #print "entro a insertar!"
        a = (nodoRaiz.contador + 1)
        n = nodoVuelos(lugarLlegada, aeropuerto, horaFechaSalida, horaFechaLlegada, cantidadPrimeraClase, costoPrimeraClase, cantidadClaseTurista, costoClaseTurista, cantidadClaseEjecutiva, costoClaseEjecutiva, a)
        if nodoRaiz.raiz == None:
            nodoRaiz.raiz = n
        else:
            nodoRaiz.raiz = nodoRaiz.insertarAVL(n, nodoRaiz.raiz)
        nodoRaiz.contador = nodoRaiz.contador + 1

    def modificar(nodoRaiz, lugarLlegada, aeropuerto, horaFechaSalida, horaFechaLlegada, cantidadPrimeraClase, costoPrimeraClase, cantidadClaseTurista, costoClaseTurista, cantidadClaseEjecutiva, costoClaseEjecutiva, id_viejo, estado):
        nodo = nodoRaiz.buscar(id_viejo, nodoRaiz.raiz)
        if nodo != None:
            nodo.lugarLlegada = lugarLlegada
            nodo.aeropuerto = aeropuerto
            nodo.horaFechaSalida = horaFechaSalida
            nodo.horaFechaLlegada = horaFechaLlegada
            nodo.cantidadPrimeraClase = cantidadPrimeraClase
            nodo.costoPrimeraClase = costoPrimeraClase
            nodo.cantidadClaseTurista = cantidadClaseTurista
            nodo.costoClaseTurista = costoClaseTurista
            nodo.cantidadClaseEjecutiva = cantidadClaseEjecutiva
            nodo.costoClaseEjecutiva = costoClaseEjecutiva
            nodo.EstadoInicial = estado
            #nodo.EstadoInicial = EstadoInicial
        else: 
            print "El vuelo no exite"

    def get_cantidadPasajero(nodoRaiz, dato, categoria):
        nodo = nodoRaiz.buscar(dato, nodoRaiz.raiz)
        a = ""
        if nodo != None:
            if categoria == "primera":
                a = "%s" % nodo.cantidadPrimeraClase

            else:
                if categoria == "turista":
                    a = "%s" % nodo.cantidadClaseTurista
                else:
                    if categoria == "ejecutiva":
                        a = "%s" % nodo.cantidadClaseEjecutiva
        return a

    def restar_cantidadPasajero(nodoRaiz, dato, categoria):
        nodo = nodoRaiz.buscar(dato, nodoRaiz.raiz)
        if nodo != None:
            if categoria == "Ejecutiva":
                nodo.vuelosEjecutivo = nodo.vuelosEjecutivo + 1
            else:
                if categoria == "Turista":
                    nodo.vuelosTurista = nodo.vuelosTurista + 1
                else:
                    if categoria == "Primera-Clase":
                        nodo.vuelosPrimeraClase = nodo.vuelosPrimeraClase + 1


    def get_VueloEstado(nodoRaiz, dato):
        nodo = nodoRaiz.buscar(dato, nodoRaiz.raiz)
        a = ""
        if nodo != None:
            a = "%s" % nodo.EstadoInicial
        return a


    def modoficarEstadoInicial(nodoRaiz, idd, estado):
        nodo = nodoRaiz.buscar(idd, nodoRaiz.raiz)
        if nodo != None:
            nodo.EstadoInicial = estado
        else:
            print "El vuelo no exite"

    def llenarListaUsuariosAsignados(nodoRaiz, lista1, i):
        nodo = nodoRaiz.buscar(i, nodoRaiz.raiz)
        if nodo != None:
            nodo.usuariosAsignados = lista1

    def preorden (nodoRaiz, r, cont):
        if (r != None):
            a = "%s" % r.idd
            cont = cont + a + ","
            return nodoRaiz.preorden(r.izquierda, cont)
            return nodoRaiz.preorden(r.derecha, cont)
        return cont

    def concatenar(nodoRaiz, nodo):
        a = "%s" % nodo.idd
        nodoRaiz.recorrido = nodoRaiz.recorrido + a + ","

    def preorden1 (nodoRaiz, r):
        if (r != None):
            #return "%s,"%r.idd
            nodoRaiz.concatenar(r)
            nodoRaiz.preorden1(r.izquierda)
            nodoRaiz.preorden1(r.derecha)

    def concatenar2(nodoRaiz, nodo):
        a = "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (nodo.idd, nodo.lugarLlegada, nodo.aeropuerto, nodo.EstadoInicial)
        nodoRaiz.recorrido2 = nodoRaiz.recorrido2 + a

    def preorden2 (nodoRaiz, r):
        if (r != None):
            #return "%s,"%r.idd
            nodoRaiz.concatenar2(r)
            nodoRaiz.preorden2(r.izquierda)
            nodoRaiz.preorden2(r.derecha)

    def contarCategoria(nodoRaiz, r, categoria):
        if r != None:
            nodoRaiz.buscarCategoria(r, categoria)
            nodoRaiz.contarCategoria(r.izquierda, categoria)
            nodoRaiz.contarCategoria(r.derecha, categoria)
            
    def contarCategoriaPDF(nodoRaiz, r, categoria):
        if r != None:
            nodoRaiz.buscarCategoriaPDF(r, categoria)
            nodoRaiz.contarCategoriaPDF(r.izquierda, categoria)
            nodoRaiz.contarCategoriaPDF(r.derecha, categoria)
            
    def buscarCategoriaPDF(nodoRaiz, r, categoria):
        if r.EstadoInicial == categoria:
            costoClaseEjecutiva = "%s" % r.costoClaseEjecutiva
            costoClaseTurista = "%s" % r.costoClaseTurista
            cantidadClaseEjecutiva = "%s" % r.cantidadClaseEjecutiva
            lugarLlegada = "%s" % r.lugarLlegada
            aeropuerto = "%s" % r.aeropuerto
            horaFechaSalida = "%s" % r.horaFechaSalida
            horaFechaLlegada = "%s" % r.horaFechaLlegada
            cantidadPrimeraClase = "%s" % r.cantidadPrimeraClase
            costoPrimeraClase = "%s" % r.costoPrimeraClase
            cantidadClaseTurista = "%s" % r.cantidadClaseTurista
            idd = "%s" % r.idd
            contenido = idd + "," + lugarLlegada + "," + aeropuerto + "," + horaFechaSalida + "," + horaFechaLlegada + "," + cantidadPrimeraClase + "," + costoPrimeraClase + "," + cantidadClaseTurista + "," + costoClaseTurista + "," + cantidadClaseEjecutiva + "," + costoClaseEjecutiva + ","
            nodoRaiz.listaCategoria = nodoRaiz.listaCategoria + contenido
            
    def buscarCategoria(nodoRaiz, r, categoria):
        if r.EstadoInicial == categoria:
            costoClaseEjecutiva = "%s" % r.costoClaseEjecutiva
            costoClaseTurista = "%s" % r.costoClaseTurista
            cantidadClaseEjecutiva = "%s" % r.cantidadClaseEjecutiva
            lugarLlegada = "%s" % r.lugarLlegada
            aeropuerto = "%s" % r.aeropuerto
            horaFechaSalida = "%s" % r.horaFechaSalida
            horaFechaLlegada = "%s" % r.horaFechaLlegada
            cantidadPrimeraClase = "%s" % r.cantidadPrimeraClase
            costoPrimeraClase = "%s" % r.costoPrimeraClase
            cantidadClaseTurista = "%s" % r.cantidadClaseTurista
            idd = "%s" % r.idd
            inicio = "<table border=\"1\"><tr><td>Id</td><td>Lugar de Llegada</td><td>Lugar de Salida</td><td>Fecha de Salida</td><td>Fecha de Llegada</td><td>Asientos P-Clase</td><td>Costo P-Clase</td><td>Asientos Turista</td><td>Costo Turista</td><td>Asientos Ejecutiva</td><td>Costo Ejecutiva</td></tr>"
            medio = "<td>" + idd + "<td>" + lugarLlegada + "</td>" + "<td>" + aeropuerto + "</td>" + "<td>" + horaFechaSalida + "</td>" + "<td>" + horaFechaLlegada + "</td>" + "<td>" + cantidadPrimeraClase + "</td>" + "<td>" + costoPrimeraClase + "</td>" + "<td>" + cantidadClaseTurista + "</td>" + "<td>" + costoClaseTurista + "</td>" + "<td>" + cantidadClaseEjecutiva + "</td>" + "<td>" + costoClaseEjecutiva + "</td>"
            contenido = inicio + medio + "</table><br><br>"
            nodoRaiz.listaCategoria = nodoRaiz.listaCategoria + contenido

    def TodasCategoria(nodoRaiz, r):
        if r != None:
            nodoRaiz.TodasbuscarCategoria(r)
            nodoRaiz.TodasCategoria(r.izquierda)
            nodoRaiz.TodasCategoria(r.derecha)
 
    def TodasCategoriaPDF(nodoRaiz, r):
        if r != None:
            nodoRaiz.TodasbuscarCategoriaPDF(r)
            nodoRaiz.TodasCategoriaPDF(r.izquierda)
            nodoRaiz.TodasCategoriaPDF(r.derecha)
            
    def TodasbuscarCategoriaPDF(nodoRaiz, r):
        costoClaseEjecutiva = "%s" % r.costoClaseEjecutiva
        costoClaseTurista = "%s" % r.costoClaseTurista
        cantidadClaseEjecutiva = "%s" % r.cantidadClaseEjecutiva
        lugarLlegada = "%s" % r.lugarLlegada
        aeropuerto = "%s" % r.aeropuerto
        horaFechaSalida = "%s" % r.horaFechaSalida
        horaFechaLlegada = "%s" % r.horaFechaLlegada
        cantidadPrimeraClase = "%s" % r.cantidadPrimeraClase
        costoPrimeraClase = "%s" % r.costoPrimeraClase
        cantidadClaseTurista = "%s" % r.cantidadClaseTurista
        idd = "%s" % r.idd
        contenido = idd + "," + lugarLlegada + "," + aeropuerto + "," + horaFechaSalida + "," + horaFechaLlegada + "," + cantidadPrimeraClase + "," + costoPrimeraClase + "," + cantidadClaseTurista + "," + costoClaseTurista + "," + cantidadClaseEjecutiva + "," + costoClaseEjecutiva + ","
        nodoRaiz.listaCategoria = nodoRaiz.listaCategoria + contenido
        


    def TodasbuscarCategoria(nodoRaiz, r):
        costoClaseEjecutiva = "%s" % r.costoClaseEjecutiva
        costoClaseTurista = "%s" % r.costoClaseTurista
        cantidadClaseEjecutiva = "%s" % r.cantidadClaseEjecutiva
        lugarLlegada = "%s" % r.lugarLlegada
        aeropuerto = "%s" % r.aeropuerto
        horaFechaSalida = "%s" % r.horaFechaSalida
        horaFechaLlegada = "%s" % r.horaFechaLlegada
        cantidadPrimeraClase = "%s" % r.cantidadPrimeraClase
        costoPrimeraClase = "%s" % r.costoPrimeraClase
        cantidadClaseTurista = "%s" % r.cantidadClaseTurista
        idd = "%s" % r.idd
        medio = "<tr><td>" + idd + "</td>" + "<td>" + lugarLlegada + "</td>" + "<td>" + aeropuerto + "</td>" + "<td>" + horaFechaSalida + "</td>" + "<td>" + horaFechaLlegada + "</td>" + "<td>" + cantidadPrimeraClase + "</td>" + "<td>" + costoPrimeraClase + "</td>" + "<td>" + cantidadClaseTurista + "</td>" + "<td>" + costoClaseTurista + "</td>" + "<td>" + cantidadClaseEjecutiva + "</td>" + "<td>" + costoClaseEjecutiva + "</td></tr>"
        nodoRaiz.listaCategoria = nodoRaiz.listaCategoria + medio


    def buscarVueloAeropuerto(self, r, nombre):
        print "hola"
        if r.lugarLlegada == nombre:
            costoClaseEjecutiva = "%s" % r.costoClaseEjecutiva
            costoClaseTurista = "%s" % r.costoClaseTurista
            cantidadClaseEjecutiva = "%s" % r.cantidadClaseEjecutiva
            lugarLlegada = "%s" % r.lugarLlegada
            aeropuerto = "%s" % r.aeropuerto
            horaFechaSalida = "%s" % r.horaFechaSalida
            horaFechaLlegada = "%s" % r.horaFechaLlegada
            cantidadPrimeraClase = "%s" % r.cantidadPrimeraClase
            costoPrimeraClase = "%s" % r.costoPrimeraClase
            cantidadClaseTurista = "%s" % r.cantidadClaseTurista
            idd = "%s" % r.idd
            medio = "<tr><td>" + idd + "</td>" + lugarLlegada + "</td>" + "<td>" + aeropuerto + "</td>" + "<td>" + horaFechaSalida + "</td>" + "<td>" + horaFechaLlegada + "</td>" + "<td>" + cantidadPrimeraClase + "</td>" + "<td>" + costoPrimeraClase + "</td>" + "<td>" + cantidadClaseTurista + "</td>" + "<td>" + costoClaseTurista + "</td>" + "<td>" + cantidadClaseEjecutiva + "</td>" + "<td>" + costoClaseEjecutiva + "</td></tr>"
            self.listaVueloAeropuerto = self.listaVueloAeropuerto + medio
    
    def buscarVueloAeropuertoPDF(self, r, nombre):
        print "va bien"
        if r.lugarLlegada == nombre:
            costoClaseEjecutiva = "%s" % r.costoClaseEjecutiva
            costoClaseTurista = "%s" % r.costoClaseTurista
            cantidadClaseEjecutiva = "%s" % r.cantidadClaseEjecutiva
            lugarLlegada = "%s" % r.lugarLlegada
            aeropuerto = "%s" % r.aeropuerto
            horaFechaSalida = "%s" % r.horaFechaSalida
            horaFechaLlegada = "%s" % r.horaFechaLlegada
            cantidadPrimeraClase = "%s" % r.cantidadPrimeraClase
            costoPrimeraClase = "%s" % r.costoPrimeraClase
            cantidadClaseTurista = "%s" % r.cantidadClaseTurista
            idd = "%s" % r.idd
            inicio = idd + "," + lugarLlegada + "," + aeropuerto + "," + horaFechaSalida + "," + horaFechaLlegada + "," + cantidadPrimeraClase + "," + costoPrimeraClase + "," + cantidadClaseTurista + "," + costoClaseTurista + "," + cantidadClaseEjecutiva  + "," + costoClaseEjecutiva
            print inicio
            self.listaVueloAeropuerto = self.listaVueloAeropuerto + inicio
            
    def recorrerArbol(self, r, nombre):
        if r != None:
            self.buscarVueloAeropuerto(r, nombre)
            self.recorrerArbol(r.izquierda, nombre)
            self.recorrerArbol(r.derecha, nombre)
            
    def recorrerArbolPDF(self, r, nombre):
        if r != None:
            self.buscarVueloAeropuertoPDF(r, nombre)
            self.recorrerArbolPDF(r.izquierda, nombre)
            self.recorrerArbolPDF(r.derecha, nombre)
                        
    def recorridoBuscarUser(nodoRaiz, r, datoid):
        if r != None:
            nodoRaiz.buscarUser(r, datoid)
            nodoRaiz.recorridoBuscarUser(r.izquierda, datoid)
            nodoRaiz.recorridoBuscarUser(r.derecha, datoid)

    def buscarUser(nodoRaiz, r, datoid):
        if r.idd == datoid:
            if r.usuariosAsignados != None:
                nodo = r.usuariosAsignados.cabeza
                while nodo != None:
                    nodoRaiz.listaUser = nodoRaiz.listaUser + nodo.nombreUsuario + ","
                    nodo = nodo.siguiente


    def usuarioVuelo(nodoRaiz, nodo, nombre):
        print "entra a buscar en la lista"
        if nodo.usuariosAsignados  != None:
            a = "%s" % nodo.usuariosAsignados.buscar(nombre)
            if a != "":
                b = "%s" % nodo.idd
                nodoRaiz.listado = nodoRaiz.listado + b + "," + a  + "," + nodo.lugarLlegada + "," + nodo.aeropuerto + "," + nodo.horaFechaLlegada + ","
                print "%s" % nodoRaiz.listado

    def listadoUsuarioVuelo(nodoRaiz, nombre, r):
        if r != None:
            nodoRaiz.usuarioVuelo(r, nombre)
            nodoRaiz.listadoUsuarioVuelo(nombre, r.izquierda)
            nodoRaiz.listadoUsuarioVuelo(nombre, r.derecha)


    def ToDot(nodoRaiz, node):
        cont = "\n"
        if node.usuariosAsignados != None:
            cont = cont + node.usuariosAsignados.dibujar()
            a = "%s" % node.usuariosAsignados.cabeza.nombreUsuario
            cont = cont + "{rank=same " + node.toString() + " " + a + "}"
            cont = cont + node.toString() + "-- " + node.usuariosAsignados.cabeza.nombreUsuario + "\n"
        else:
            print "lista null izquierda"
        if node.izquierda != None:
            cont = cont + node.toString() + "--" + node.izquierda.toString() + "\n"
            
            cont = cont + nodoRaiz.ToDot(node.izquierda)
        if node.derecha != None:
            cont = cont + node.toString() + "--" + node.derecha.toString() + "\n"
           
            cont = cont + nodoRaiz.ToDot(node.derecha)
        print "%s" % cont
        return cont

    def ToDotGraph(nodoRaiz):
        contenido = ""
        if nodoRaiz.raiz == None:
            contenido = " Arbol_Vacio"
            nodoRaiz.Grafica = contenido
        else:
            if nodoRaiz.raiz.izquierda == None and nodoRaiz.raiz.derecha == None:
                aux2 = ""
                a = "%s" % nodoRaiz.raiz.usuariosAsignados.cabeza.nombreUsuario
                aux2 = aux2 + "\n" + nodoRaiz.raiz.usuariosAsignados.dibujar() + "\n {rank=same " + nodoRaiz.raiz.toString() + "  " + a  + "}" 
                aux2 = aux2 + "%s -- %s" % (nodoRaiz.raiz.idd, a)
                
                

                contenido = + aux2 
                nodoRaiz.Grafica = contenido
            else:
                contenido = nodoRaiz.ToDot(nodoRaiz.raiz)
                nodoRaiz.Grafica = contenido
#****************************************SIN LISTA******************************

    def ToDotSINLISTA(nodoRaiz, node):
        cont = "\n"
        if node.izquierda != None:
            cont = cont + node.toString() + "--" + node.izquierda.toString() + "\n"
            cont = cont + nodoRaiz.ToDotSINLISTA(node.izquierda)
        if node.derecha != None:
            cont = cont + node.toString() + "--" + node.derecha.toString() + "\n"
            cont = cont + nodoRaiz.ToDotSINLISTA(node.derecha)
        return cont

    def ToDotGraphSINLISTA(nodoRaiz):
        contenido = ""
        if nodoRaiz.raiz == None:
            contenido = "Arbol_Vacio "
            nodoRaiz.Grafica = contenido  
        else:
            if nodoRaiz.raiz.izquierda == None and nodoRaiz.raiz.derecha == None:
                aux2 = "%s" % nodoRaiz.raiz.idd
                #aux2 = aux2 + nodoRaiz.raiz.usuariosAsignados.cabeza.nombreUsuario + " " + nodoRaiz.raiz.usuariosAsignados.dibujar()
                contenido = contenido + aux2 
                nodoRaiz.Grafica = contenido  
            else:
                contenido = nodoRaiz.ToDotSINLISTA(nodoRaiz.raiz) 
                nodoRaiz.Grafica = contenido   



    def AsigUser(nodoRaiz, nombre, idVuelo):
        tempo  = nodoRaiz.buscar(idVuelo, nodoRaiz.raiz)
        if tempo != None:
            #print "tempo no es None"
            if tempo.usuariosAsignados == None:
            #   print "la lista de usuarios es None"
                aux = ListaUsuariosAsignados()
                aux.insertar(nombre)
                tempo.usuariosAsignados = aux
            else:
                #print "la lista ya no es none"
                tempo.usuariosAsignados.insertar(nombre)
    #   print "***************************************************"


    def getDatosVuelo(nodoRaiz, idd1):
        nodo = nodoRaiz.buscar(idd1, nodoRaiz.raiz)
        if nodo != None:
            primera = "%s" % nodo.cantidadPrimeraClase
            turista = "%s" % nodo.cantidadClaseTurista
            ejecutiva = "%s" % nodo.cantidadClaseEjecutiva
            cadena = nodo.lugarLlegada + "," + nodo.aeropuerto + "," + nodo.horaFechaSalida + "," + nodo.horaFechaLlegada + "," + primera + "," + nodo.costoPrimeraClase + "," + turista + "," + nodo.costoClaseTurista + "," + ejecutiva + "," + nodo.costoClaseEjecutiva + "," + nodo.EstadoInicial
            return cadena
        return ""
    
    def getDatosClaseVuelo(nodoRaiz, idd1, clase):
        nodo = nodoRaiz.buscar(idd1, nodoRaiz.raiz)
        print clase
        if nodo != None:
            if clase == ("Ejecutivo"):
                print "Hola"
                ejecutiva = "%s" % nodo.cantidadClaseEjecutiva
                print ejecutiva
                cadena = ejecutiva + "," + "%s" % nodo.vuelosEjecutivo + "," + nodo.lugarLlegada + "," + nodo.aeropuerto + "," + nodo.EstadoInicial
                return cadena
            if clase == ("Primera-Clase"):
                primera = "%s" % nodo.cantidadPrimeraClase
                cadena = primera + "," + "%s" % nodo.vuelosPrimeraClase + "," + nodo.lugarLlegada + "," + nodo.aeropuerto + "," + nodo.EstadoInicial
                return cadena
            if clase == ("Turista"):
                turista = "%s" % nodo.cantidadClaseTurista
                cadena = turista + "," + "%s" % nodo.vuelosTurista + "," + nodo.lugarLlegada + "," + nodo.aeropuerto + "," + nodo.EstadoInicial
                return cadena
        return ""


    def obtenerNodoReemplazo(nodoRaiz, nodoReemp):
        reemplazarPadre = nodoReemp
        reemplazo = nodoReemp
        auxiliar = nodoReemp.derecha
        while auxiliar != None:
            reemplazarPadre = reemplazo
            reemplazo = auxiliar
            auxiliar = auxiliar.izquierda
        if reemplazo != nodoReemp.derecha:
            reemplazarPadre.izquierda = reemplazo.derecha
            reemplazo.derecha = nodoReemp.derecha
        return reemplazo

    def eliminar_2(nodoRaiz, dato):
        temporal = nodoRaiz.raiz
        padre = None
        padrepadre = None
        hijo = None
        while temporal != None:
            #padre = temporal
            if dato > temporal.idd:
                if temporal.derecha != None:
                    padre = temporal
                temporal = temporal.derecha
            else:
                if temporal.izquierda != None:
                    padre = temporal
                temporal = temporal.izquierda
        print " el padre es %s" % padre.idd
        


    def eliminar(nodoRaiz, idd1):
        auxiliar = nodoRaiz.raiz
        padre = nodoRaiz.raiz
        esHijoIzq = True
        nodo1 = None
        while auxiliar.idd != idd1:
            padre = auxiliar
            if idd1 < auxiliar.idd:
                esHijoIzq = True
                auxiliar = auxiliar.izquierda
            else:
                esHijoIzq = False
                auxiliar = auxiliar.derecha
            if auxiliar == None:
                return False
        #fin del while
        if auxiliar.izquierda == None and auxiliar.derecha == None:
            if auxiliar == nodoRaiz.raiz:
                nodoRaiz.raiz = None
            else:
                if esHijoIzq == True:
                    padre.izquierda = None
                else:
                    padre.derecha = None
        else:
            if auxiliar.derecha == None:
                #nodo1 = auxiliar.derecha
                #nodoRaiz.insertarAVL(auxiliar.derecha,nodoRaiz.raiz)
                if auxiliar == nodoRaiz.raiz:
                    nodoRaiz.raiz = auxiliar.izquierda
                else:
                    if esHijoIzq == True:
                        padre.izquierda = auxiliar.izquierda
                    else:
                        padre.derecha = auxiliar.izquierda
            else:
                if auxiliar.izquierda == None:
                    #nodo1 = auxiliar.izquierda
                    #nodoRaiz.insertarAVL(auxiliar.izquierda,nodoRaiz.raiz)
                    if auxiliar == nodoRaiz.raiz:
                        nodoRaiz.raiz = auxiliar.derecha
                    else:
                        if esHijoIzq == True:
                            padre.izquierda = auxiliar.derecha
                        else:
                            padre.derecha = auxiliar.izquierda
                else:
                    reemplazo = nodoRaiz.obtenerNodoReemplazo(auxiliar)
                    if auxiliar == nodoRaiz.raiz:
                        nodoRaiz.raiz = reemplazo
                    else:
                        if esHijoIzq == True:
                            padre.izquierda = reemplazo
                        else:
                            padre.derecha = reemplazo
                    reemplazo.izquierda = auxiliar.izquierda
                    #nodo1 = reemplazo
                    #nodoRaiz.insertarAVL(reemplazo,nodoRaiz.raiz)
        return True
#---------------------------------------------------------FIN DE LAS ESTRUCTURAS----------------------------------------------------------
obj_listaAeropuerto = listaAeropuerto()
obj_arbolUsuarios = arbolUsuarios()
obj_arbolVuelos = arbolVuelos()
#---------------------------------------------------------INICIO METODOS DEL WEB SERVICE--------------------------------------------------

@app.route('/aeropuertoInsertar/<nombre>/<pais>/<password>')
def hello_world(nombre, pais, password):
    obj_listaAeropuerto.insertar(nombre, pais, password)
    return 'Guardado Exitosamente'

@app.route('/get_aeropuertos/')
def getaeropuerotos():
    return obj_listaAeropuerto.mostrar()

@app.route('/vuelosInsertar/<lugarLlegada>/<aeropuerto>/<horaFechaSalida>/<horaFechaLlegada>/<int:cantidadPrimeraClase>/<costoPrimeraClase>/<int:cantidadClaseTurista>/<costoClaseTurista>/<int:cantidadClaseEjecutiva>/<costoClaseEjecutiva>')
def vuelosInsertar(lugarLlegada, aeropuerto, horaFechaSalida, horaFechaLlegada, cantidadPrimeraClase, costoPrimeraClase, cantidadClaseTurista, costoClaseTurista, cantidadClaseEjecutiva, costoClaseEjecutiva):
    obj_arbolVuelos.insertar(lugarLlegada, aeropuerto, horaFechaSalida, horaFechaLlegada, cantidadPrimeraClase, costoPrimeraClase, cantidadClaseTurista, costoClaseTurista, cantidadClaseEjecutiva, costoClaseEjecutiva)
    return "Guardado Exitosamente"

@app.route('/getaeropuerotos2/')
def getaeropuerotos2():
    return obj_arbolVuelos.getCont()


@app.route('/get_vuelos')
def get_vuelos():
    obj_arbolVuelos.recorrido = ""
    obj_arbolVuelos.preorden1(obj_arbolVuelos.raiz)
    return "%s" % obj_arbolVuelos.recorrido

@app.route('/modificarEstado/<int:id1>/<estado>')
def modificarEstado(id1, estado):
    obj_arbolVuelos.modoficarEstadoInicial(id1, estado)
    return "Guardado Exitosamente !"

@app.route('/get_datos_vuelo/<int:id2>')
def get_datos_vuelo(id2):
    return "%s" % obj_arbolVuelos.getDatosVuelo(id2)

@app.route('/get_datos_clase_vuelo/<int:id2>/<clase>')
def get_datos_clase_vuelo(id2, clase):
    return "%s" % obj_arbolVuelos.getDatosClaseVuelo(id2, clase)

@app.route('/modificarDatosVuelo/<lugarLlegada>/<aeropuerto>/<horaFechaSalida>/<horaFechaLlegada>/<cantidadPrimeraClase>/<costoPrimeraClase>/<cantidadClaseTurista>/<costoClaseTurista>/<cantidadClaseEjecutiva>/<costoClaseEjecutiva>/<int:id_viejo>/<estado>')
def modificarDatosVuelo(lugarLlegada, aeropuerto, horaFechaSalida, horaFechaLlegada, cantidadPrimeraClase, costoPrimeraClase, cantidadClaseTurista, costoClaseTurista, cantidadClaseEjecutiva, costoClaseEjecutiva, id_viejo, estado):
    obj_arbolVuelos.modificar(lugarLlegada, aeropuerto, horaFechaSalida, horaFechaLlegada, cantidadPrimeraClase, costoPrimeraClase, cantidadClaseTurista, costoClaseTurista, cantidadClaseEjecutiva, costoClaseEjecutiva, id_viejo, estado)
    return "Guardado Exitosamente !"

@app.route('/eliminarVuelo/<int:idd>')
def eliminarVuelo(idd):
    obj_arbolVuelos.eliminar(idd)
    return "Eliminado Exitosamente !"

@app.route('/userExiste/<username>')
def userExiste(username):
    respuesta = "%s" % obj_arbolUsuarios.usuarioExiste(username)
    return respuesta

@app.route('/validarUsuario/<username>/<passwoard>')
def validarUsuario(username, passwoard):
    respuesta = "%s" % obj_arbolUsuarios.validarUsuario(username, passwoard)
    return respuesta


@app.route('/crearUsuario/<nombre>/<password>/<user>/<direccion>/<telefono>/<tarjeta>/<direcionActual>')
def crearUsuario(nombre, password, user, direccion, telefono, tarjeta, direcionActual):
    obj_arbolUsuarios.insertar(nombre, password, user, direccion, telefono, tarjeta, direcionActual)
    return "Guardado Exitosamente !"

@app.route('/get_usuarios')
def get_usuarios():
    obj_arbolUsuarios.recorrido = ""
    obj_arbolUsuarios.preorden1(obj_arbolUsuarios.raiz)
    return "%s" % obj_arbolUsuarios.recorrido

@app.route('/getCantidad/<int:id1>/<categoria>')
def getCantidad(id1, categoria):
    res = "%s" % obj_arbolVuelos.get_cantidadPasajero(id1, categoria)
    return res

@app.route('/getEstado/<int:dato>')
def getEstado(dato):
    return obj_arbolVuelos.get_VueloEstado(dato)

@app.route('/asignar_vuelo/<nombre>/<int:idvuelo>')
def asignar_vuelo(nombre, idvuelo):
    obj_arbolVuelos.AsigUser(nombre, idvuelo)
    return "Guardado Exitosamente !"

@app.route('/restar_cantidad/<int:dato>/<categoria>')
def restar_cantidad(dato, categoria):
    obj_arbolVuelos.restar_cantidadPasajero(dato, categoria)
    return "Guardado Exitosamente !"

@app.route('/get_datos_2/')
def get_datos_2():
    obj_arbolVuelos.recorrido2 = ""
    obj_arbolVuelos.preorden2(obj_arbolVuelos.raiz)
    return "%s" % obj_arbolVuelos.recorrido2

@app.route('/mostrar_aeropuertos')
def mostrar_aeropuertos():
    return "%s" % obj_listaAeropuerto.mostrar1()

@app.route('/user_vuelo/<nombre>')
def usuarios_vuelo(nombre):
    obj_arbolVuelos.listado = ""
    obj_arbolVuelos.listadoUsuarioVuelo(nombre, obj_arbolVuelos.raiz)
    return "%s" % obj_arbolVuelos.listado

@app.route('/eliminar_usuario/<user>')
def eliminar_usuario(user):
    obj_arbolUsuarios.eliminar(user)
    return "Eliminado Exitosamente !"

@app.route('/set_direccion_actual/<id_viejo>/<estado>')
def set_direccion_actual(id_viejo, estado):
    print id_viejo
    print estado
    obj_arbolUsuarios.set_direcionActual(id_viejo, estado)
    return "Guardado Exitosamente !"

@app.route('/get_usuariosVuelo/<int:dato>')
def get_usuariosVuelo(dato):
    obj_arbolVuelos.listaUser = ""
    obj_arbolVuelos.recorridoBuscarUser(obj_arbolVuelos.raiz, dato)
    return obj_arbolVuelos.listaUser

@app.route('/get_userDatos/<nombre>/<int:codigo>')
def get_userDatos(nombre, codigo):
    return "%s" % obj_arbolUsuarios.getDatos(nombre, codigo)

@app.route('/get_userDatosPDF/<nombre>/<int:codigo>')
def get_userDatosPDF(nombre, codigo):
    return "%s" % obj_arbolUsuarios.getDatosPDF(nombre, codigo)

@app.route('/get_direccionAeropuerto/<nombre>')
def get_direccionAeropuerto(nombre):
    respuesta = "%s" % obj_listaAeropuerto.getDireccionAeropuerto(nombre)
    return respuesta
   

@app.route('/get_vuelosDatos/<categoria>')
def get_vuelosDatos(categoria):
    obj_arbolVuelos.listaCategoria = ""
    obj_arbolVuelos.contarCategoria(obj_arbolVuelos.raiz, categoria)
    return obj_arbolVuelos.listaCategoria

@app.route('/get_todosVuelos')
def get_todosVuelos():
    obj_arbolVuelos.listaCategoria = ""
    obj_arbolVuelos.TodasCategoria(obj_arbolVuelos.raiz)
    inicio = "<table border=\"1\"><tr><td>Lugar de Llegada</td><td>Lugar de Salida</td><td>Fecha de Salida</td><td>Fecha de Llegada</td><td>Asientos P-Clase</td><td>Costo P-Clase</td><td>Asientos Turista</td><td>Costo Turista</td><td>Asientos Ejecutiva</td><td>Costo Ejecutiva</td></tr>"
    respuesta = inicio + obj_arbolVuelos.listaCategoria + "</table>"
    return "%s" % respuesta

@app.route('/get_todosVuelosPDF')
def get_todosVuelosPDF():
    obj_arbolVuelos.listaCategoria = ""
    obj_arbolVuelos.TodasCategoriaPDF(obj_arbolVuelos.raiz)
 
    return obj_arbolVuelos.listaCategoria

@app.route('/get_vuelosDatosPDF/<categoria>')
def get_vuelosDatosPDF(categoria):
    obj_arbolVuelos.listaCategoria = ""
    obj_arbolVuelos.contarCategoriaPDF(obj_arbolVuelos.raiz, categoria)
    return obj_arbolVuelos.listaCategoria

@app.route('/dibujar_listaAeropuerto')
def dibujar_listaAeropuerto():
    obj_listaAeropuerto.dibujar2()
    return obj_listaAeropuerto.Grafica

@app.route('/dibujar_arbolUsuarios')
def dibujar_arbolUsuarios():
    obj_arbolUsuarios.ToDotGraph()
    return obj_arbolUsuarios.Grafica

@app.route('/dibujar_arbolVuelos')
def dibujar_arbolVuelos():
    obj_arbolVuelos.ToDotGraph()
    return obj_arbolVuelos.Grafica

@app.route('/dibujar_arbolVuelos1')
def dibujar_arbolVuelos1():
    obj_arbolVuelos.ToDotGraphSINLISTA()
    return obj_arbolVuelos.Grafica

@app.route('/get_vuelos_aeropuerto/<nombre>')
def get_vuelos_aeropuerto(nombre):
    obj_arbolVuelos.listaVueloAeropuerto = ""
    obj_arbolVuelos.recorrerArbol(obj_arbolVuelos.raiz, nombre)
    inicio = "<table border=\"1\"><tr><td>lugarLlegada</td><td>aeropuerto</td><td>horaFechaSalida</td><td>horaFechaLlegada</td><td>cantidadPrimeraClase</td><td>costoPrimeraClase</td><td>cantidadClaseTurista</td><td>costoClaseTurista</td><td>cantidadClaseEjecutiva</td><td>costoClaseEjecutiva</td></tr>"
    respuesta = inicio + obj_arbolVuelos.listaVueloAeropuerto + "</table>"
    return "%s" % respuesta

@app.route('/get_vuelos_aeropuertoPDF/<nombre>')
def get_vuelos_aeropuertoPDF(nombre):
    obj_arbolVuelos.listaVueloAeropuerto = ""
    obj_arbolVuelos.recorrerArbolPDF(obj_arbolVuelos.raiz, nombre)
    inicio = ""
    respuesta = inicio + obj_arbolVuelos.listaVueloAeropuerto
    return obj_arbolVuelos.listaVueloAeropuerto

@app.route('/get_Vuelo_usuario/<username>')
def get_Vuelo_usuario(username):
    obj_arbolVuelos.listaUsuarios_Asignados = ""
    obj_arbolVuelos.preorder_ua(obj_arbolVuelos.raiz, username)
    inicio = "<h1>Vuelos</h1><table border=\"1\"><tr><td>lugarLlegada</td><td>aeropuerto</td><td>horaFechaSalida</td><td>horaFechaLlegada</td><td>cantidadPrimeraClase</td><td>costoPrimeraClase</td><td>cantidadClaseTurista</td><td>costoClaseTurista</td><td>cantidadClaseEjecutiva</td><td>costoClaseEjecutiva</td></tr>"
    respuesta = inicio + obj_arbolVuelos.listaUsuarios_Asignados + "</table>"
    return  obj_arbolVuelos.listaUsuarios_Asignados
    
@app.route('/get_Vuelo_usuarioPDF/<username>')
def get_Vuelo_usuarioPDF(username):
    obj_arbolVuelos.listaUsuarios_Asignados = ""
    obj_arbolVuelos.preorder_uaPDF(obj_arbolVuelos.raiz, username)
    return  obj_arbolVuelos.listaUsuarios_Asignados


    
if __name__ == '__main__':
    app.run()


