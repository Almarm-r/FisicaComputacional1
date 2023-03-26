import java.util.Scanner; 


class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in); 
    //Solicitar el numero a hallar el factorial. 
    System.out.print("Ingrese un numero para hallar el factorial: ");

    int n = sc.nextInt(); 

    //Para mostrar el resultado llamando la función factorial 

    System.out.println( n + "Facotrial  es " + factorial(n) );
    
  }

  //Definir la función del facotrial para llamar en el main. 
public static double  factorial(int n) {
  double no = 1;
  for (int i = 2 ;i<=n ;i++){
    no*=i;
  
  } 
       return no; 
}
  
}
