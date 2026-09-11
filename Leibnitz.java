public class CalculoPi {
    public static double calcularPi(int n) {
        double pi = 0.0;
        double signo = 1.0;       
        double denominador = 1.0; 

        // El for se repite n veces
        for (int i = 0; i < n; i++) {
            //Calculamos la fracción y le sumamos pi 
            double numero = signo * (1.0 / denominador);
            pi = pi + numero;
            
            //Siguiente ciclo sumamos 2 al numerador
            denominador = denominador + 2.0;         
            // Cambiamos el signo
            signo = signo * -1.0;
        }

        // y multiplicamos por 4
        return pi * 4.0;
    }
}
