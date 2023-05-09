#include<iostream>
#include<math.h>
#include<fstream>

using namespace std;

int main (void)
{
  ofstream archivo("tx.txt") , archivos ("tv.txt"), archivoss("xp.txt");
 float alfa, beta, gama, delta, omega ,p, m, h ;
 cout<<"alfa= ";
 cin>>alfa;
 cout<<"beta= ";
 cin>>beta;
 cout<<"gamma= ";
 cin>>gama;
 cout<<"delta= ";
 cin>>delta;
 cout<<"omega= ";
 cin>>omega;
  cout<<"h= ";
 cin>>h;
cout<<"m= ";
 cin>>m;

 float u0=0,u,v0=0,v, t,x;
    cout<<"t= ";
 cin>>t;
 float K1, K2, K3, K4,u1,u2,u3;
 float k1, k2, k3, k4,v1,v2,v3;

 u=u0;
 v=v0;
  if (h == 0){ cout<<"h= ";
 cin>>h;}
  else{
    

for (float i = 0 ; i<= t ; i = i+h){
 k1=gama*cos(omega*i)-(delta*v)-(alfa*u)-(beta*pow(u,3));
 //v1=u+K1*(h/2);
 k2=gama*cos(omega*(i+(1/2)*h))-(delta*(v+(1/2)*k1*h))-(alfa*u)-(beta*pow(u,3));
 //u2=v+(k2*(h/2));
 k3=gama*cos(omega*(i+(1/2)*h))-(delta*(v+(1/2)*k2*h))-(alfa*u)-(beta*pow(u,3));
 //u3=v+(k3*h);
 k4=gama*cos(omega*(i+h))-(delta*(v+(1/2)*k3*h))-(alfa*u)-(beta*pow(u,3));
 v=v+((k1+2*k2+2*k3+k4)/6)*h;

 //
 K1=v;
 u1=v+(h/2);
 K2=u1;
 u2=v+(h/2);
 K3=u2;
 u3=v+(h/2);
 K4=u3;
 u=u+((K1+2*K2+2*K3+K4)/6)*h;

 x=u;
p = m*v; 
 archivo <<i<<"\t"<<x<<"\n";
  archivos<<i<<"\t"<<v<<"\n";
  archivoss<<x<<"\t"<<p<<"\n"; 
  

}}
  archivo.close();
  archivos.close();
  archivoss.close(); 
  ofstream gnuarchivo("grafica.gp");
     gnuarchivo << "set title 'Posición vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo'\n";
     gnuarchivo << "set ylabel 'Posicion'\n";
     gnuarchivo << "plot 'tx.txt' using 1:2 with lines title 'Posicion'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'posicion.png'\n";
     gnuarchivo << "replot\n";     
     gnuarchivo << "set title 'Velocidad vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo'\n";
     gnuarchivo << "set ylabel 'Velocidad'\n";
     gnuarchivo << "plot 'tv.txt' using 1:2 with lines title 'Velocidad'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'velocidad.png'\n";
     gnuarchivo << "replot\n"; 
    gnuarchivo << "set title 'Espacio de Fase '\n";
     gnuarchivo << "set xlabel 'Posición'\n";
     gnuarchivo << "set ylabel 'Velocidad'\n";
     gnuarchivo << "plot 'xv.txt' using 1:2 with lines title 'Fase'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'Fase.png'\n";
     gnuarchivo << "replot\n";
     gnuarchivo.close();

     // ejecuta gnuplot para generar las graficas
     system("gnuplot grafica.gp");

 return 0;
}
