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
public class arbolAVL {

    private NodoArbolAVL raiz;

    public arbolAVL() {
        raiz = null;

    }

    //metodo para buscar un nodo
    public NodoArbolAVL buscar(nodoUsuario dato, NodoArbolAVL raiz) {
        if (raiz == null) {
            return null;
        } else if (raiz.dato == dato) {
            return raiz;
        } else if (raiz.dato.nick.charAt(0) < dato.nick.charAt(0)) {
            return buscar(dato, raiz.hijoDerecho);

        } else {
            return buscar(dato, raiz.hijoIzquierdo);
        }

    }

    public nodoUsuario obtenerFE(NodoArbolAVL x) {
        if (x == null) {
            return null;

        } else {
            return x.factorEquilibrio;

        }
    }

    //Rotación simple izquierda
    public NodoArbolAVL rotacionIzquierda(NodoArbolAVL c) {
        NodoArbolAVL aux = c.hijoDerecho;
        aux.padre = c.padre;
        c.hijoDerecho = aux.hijoIzquierdo;

        if (c.hijoDerecho != null) {
            c.hijoDerecho.padre = c;
        }

        aux.hijoIzquierdo = c;
        c.padre = aux;

        if (aux.padre != null) {
            if (aux.padre.hijoDerecho == c) {
                aux.padre.hijoDerecho = aux;
            } else if (aux.padre.hijoIzquierdo == c) {
                aux.padre.hijoIzquierdo = c;
            }
        }
        setBalance(c);
        setBalance(aux);

        return aux;
    }

    private void setBalance(NodoArbolAVL cur) {
//        cur.factorEquilibrio = height(cur.hijoDerecho) - height(cur.hijoIzquierdo);
    }

    private int height(NodoArbolAVL cur) {
        if (cur == null) {
            return -1;
        }
        if (cur.hijoIzquierdo == null && cur.hijoDerecho == null) {
            return 0;
        } else if (cur.hijoIzquierdo == null) {
            return 1 + height(cur.hijoDerecho);
        } else if (cur.hijoDerecho == null) {
            return 1 + height(cur.hijoIzquierdo);
        } else {
            return 1 + maximum(height(cur.hijoIzquierdo), height(cur.hijoDerecho));
        }
    }

    private int maximum(int a, int b) {
        if (a >= b) {
            return a;
        } else {
            return b;
        }
    }

}
