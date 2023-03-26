%Solución EDO Metodo de Euler. 
% Inicializar en variable la ecuación diferencial 
dydx = @(x, y) 2*y;
% Definir las condiciones iniciales 
x0 = 0;
y0 = 1;
% Definir el paso y cantidad de interaciones 
h = 0.1;
n = 10; 
% Construir un vector paa almacenar todos los valores de x y y 
x = zeros(n+1, 1);
y = zeros(n+1, 1);
% Conjutos de valores inciales 
x(1) = x0;
y(1) = y0;

% Implement the Euler method
for i = 1:n
    x(i+1) = x(i) + h;
    y(i+1) = y(i) + h * dydx(x(i), y(i));
end
% Muestra los resultados 
disp("x ");
disp(x);
disp("y ");
disp(y);
