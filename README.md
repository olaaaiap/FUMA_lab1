# Aproximación de pi utilizando Monte Carlo

En este problema tenemos un círculo de radio "a" y un cuadrado de "a**2". Según la hipótesis, la division entre la cantidad de pelotas que caen dentro del círculo, dividido por las que han caído dentro del cuadrado debería de resultar en una aproximación de pi.

Para llevar a cabo el problema hemos definido unas areas y distancias, como se pueden ver en la siguiente imagen.



![Definición de tabla](https://github.com/user-attachments/assets/2d58bcdb-e0f5-4c6a-b40b-9cd6543996a4)

El enunciado nos dice que el area total medirá 40x80cm, por tanto podemos deducir que "a" tendrá 20cm.

Esta definición de puntos relevantes nos ha servido como punto de partida a la hora de implementar la aproximación.

 ## Estudiar el efecto del parámetro fijo a.
Para este apartado hemos analizado con qué tamaño el círuculo o el cuadrado cambiando su a se saldrían del rectángulo, su contenedor. Es importante esto, porque a partir de ese momento la aproximación de pi ya no sé calcula porque se pierde la relación ya que 

Valor de pi:  3.117557374418231
Valor de pi:  3.145446632018229
Valor de pi:  3.139981435247423
Valor de pi:  2.755565449688335
Valor de pi:  0.9175658571935005