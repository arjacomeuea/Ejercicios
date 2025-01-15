using System;

class Nodo
{
    public int Valor;
    public Nodo Siguiente;

    public Nodo(int valor)
    {
        Valor = valor;
        Siguiente = null;
    }
}

class ListaEnlazada
{
    public Nodo Cabecera;

    public ListaEnlazada()
    {
        Cabecera = null;
    }

    // Método para añadir un nuevo nodo al final de la lista
    public void Añadir(int valor)
    {
        Nodo nuevoNodo = new Nodo(valor);
        if (Cabecera == null)
        {
            Cabecera = nuevoNodo;
        }
        else
        {
            Nodo temp = Cabecera;
            while (temp.Siguiente != null)
            {
                temp = temp.Siguiente;
            }
            temp.Siguiente = nuevoNodo;
        }
    }

    // Método para invertir la lista enlazada
    public void Invertir()
    {
        Nodo anterior = null;
        Nodo actual = Cabecera;
        Nodo siguiente = null;

        while (actual != null)
        {
            siguiente = actual.Siguiente; // Guardar el siguiente nodo
            actual.Siguiente = anterior; // Invertir el enlace
            anterior = actual; // Mover el nodo anterior
            actual = siguiente; // Mover al siguiente nodo
        }
        Cabecera = anterior; // Ahora el anterior es el nuevo primer nodo
    }

    // Método para mostrar la lista
    public void Mostrar()
    {
        Nodo temp = Cabecera;
        while (temp != null)
        {
            Console.Write(temp.Valor + " ");
            temp = temp.Siguiente;
        }
        Console.WriteLine();
    }
}

class Program
{
    static void Main(string[] args)
    {
        ListaEnlazada lista = new ListaEnlazada();

        // Añadir algunos elementos a la lista
        lista.Añadir(1);
        lista.Añadir(2);
        lista.Añadir(3);
        lista.Añadir(4);
        lista.Añadir(5);

        // Mostrar la lista original
        Console.WriteLine("Lista original:");
        lista.Mostrar();

        // Invertir la lista
        lista.Invertir();

        // Mostrar la lista invertida
        Console.WriteLine("Lista invertida:");
        lista.Mostrar();
    }
}
