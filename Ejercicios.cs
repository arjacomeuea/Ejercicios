using System;

class Program
{
    // Función para calcular la longitud de una lista
    static int CalcularLongitud(int[] lista)
    {
        int longitud = 0;

        // Recorrer la lista y contar los elementos
        foreach (var elemento in lista)
        {
            longitud++;
        }

        return longitud;
    }

    static void Main(string[] args)
    {
        // Ejemplo de lista
        int[] lista = { 1, 2, 3, 4, 5 };

        // Calcular la longitud de la lista
        int longitud = CalcularLongitud(lista);

        // Mostrar el resultado
        Console.WriteLine($"La longitud de la lista es: {longitud}");
    }
}
