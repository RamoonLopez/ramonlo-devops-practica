#Practica 2.1 - ramon lopez orjales
#Esta es un aaplicacion que permite gestionar una tienda


#Docker 
#Cómo construir la imagen

```bash
docker build -t ramonlo-tienda:1.0 .
```

#Como ejecutarla

```bash
docker run --rm ramonlo-tienda:1.0
```

#Variables de entorno soportadas

La aplicación no requiere variables de entorno.

#Salida esperada


Stock
Identificador: 101, Name: Camiseta, Price: 20, Stock: 10, Size: L, Colour: Verde
Identificador: 102, Name: Pantalón, Price: 35, Stock: 5, Size: M, Colour: Azul
Identificador: 103, Name: Aurculares, Price: 50, Stock: 15, Garantia: 2 años
Identificador: 104, Name: Altsvoz, Price: 300, Stock: 8, Garantia: 1 año
Identificador: 105, Name: Ordenador, Price: 15, Stock: 20, Garantia: 5 años

Resumen de pedidos
Pedido ID: 1, Cliente: Ramon, Total: 90€
Pedido ID: 2, Cliente: Laura, Total: 80€
Pedido ID: 3, Cliente: Mario, Total: 330€

Stock actualizado
Identificador: 101, Name: Camiseta, Price: 20, Stock: 8, Size: L, Colour: Verde
Identificador: 102, Name: Pantalón, Price: 35, Stock: 4, Size: M, Colour: Azul
Identificador: 103, Name: Aurculares, Price: 50, Stock: 14, Garantia: 2 años
Identificador: 104, Name: Altsvoz, Price: 300, Stock: 7, Garantia: 1 año
Identificador: 105, Name: Ordenador, Price: 15, Stock: 15, Garantia: 5 años

Tus pedidos
Pedido ID: 1, Total: 90€




