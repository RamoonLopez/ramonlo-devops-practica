# Ramonlo DevOps Práctica - Aplicación de Tienda

Aplicación Python de gestión de tienda online con sistema de usuarios, productos y pedidos.

## Descripción

Esta aplicación implementa una tienda online básica con las siguientes funcionalidades:
- Gestión de usuarios (Clientes y Administradores)
- Catálogo de productos (Productos de Ropa y Electrónicos)
- Sistema de pedidos con control de stock
- Cálculo de importes y gestión de inventario

## Docker

### Cómo construir la imagen

Para construir la imagen Docker, ejecuta el siguiente comando desde la raíz del repositorio:

```bash
docker build -t ramonlo-tienda:1.0 .
```

También puedes usar otras etiquetas según tus necesidades:

```bash
# Con etiqueta latest
docker build -t ramonlo-tienda:latest .

# Con tu usuario de Docker Hub
docker build -t tu-usuario/ramonlo-tienda:1.0 .
```

### Cómo ejecutar el contenedor

#### Ejecución básica

Para ejecutar el contenedor y ver la salida de la aplicación:

```bash
docker run --rm ramonlo-tienda:1.0
```

El flag `--rm` elimina automáticamente el contenedor después de que termina su ejecución.

#### Ejecución con nombre

Para ejecutar el contenedor con un nombre específico:

```bash
docker run --name tienda-app ramonlo-tienda:1.0
```

#### Ejecución en modo interactivo

Si necesitas ejecutar en modo interactivo:

```bash
docker run -it --rm ramonlo-tienda:1.0
```

### Variables de entorno soportadas

Actualmente, la aplicación no requiere variables de entorno para su funcionamiento básico. La configuración es estática y está definida en el código.

### Salida esperada

Al ejecutar el contenedor, deberías ver la siguiente salida:

#### 1. Stock inicial
```
Stock
Identificador: 101, Name: Camiseta, Price: 20, Stock: 10, Size: L, Colour: Verde
Identificador: 102, Name: Pantalón, Price: 35, Stock: 5, Size: M, Colour: Azul
Identificador: 103, Name: Aurculares, Price: 50, Stock: 15, Garantia: 2 años
Identificador: 104, Name: Altsvoz, Price: 300, Stock: 8, Garantia: 1 año
Identificador: 105, Name: Ordenador, Price: 15, Stock: 20, Garantia: 5 años
```

#### 2. Resumen de pedidos
```
Resumen de pedidos
Pedido ID: 1, Cliente: Ramon, Total: 90€
Pedido ID: 2, Cliente: Laura, Total: 80€
Pedido ID: 3, Cliente: Mario, Total: 330€
```

#### 3. Stock actualizado
```
Stock actualizado
Identificador: 101, Name: Camiseta, Price: 20, Stock: 8, Size: L, Colour: Verde
Identificador: 102, Name: Pantalón, Price: 35, Stock: 4, Size: M, Colour: Azul
Identificador: 103, Name: Aurculares, Price: 50, Stock: 14, Garantia: 2 años
Identificador: 104, Name: Altsvoz, Price: 300, Stock: 7, Garantia: 1 año
Identificador: 105, Name: Ordenador, Price: 15, Stock: 15, Garantia: 5 años
```

#### 4. Historial de compras
```
Tus pedidos
Pedido ID: 1, Total: 90€
```

### Pasos de prueba

1. **Construir la imagen**: Verifica que la construcción se complete sin errores
2. **Ejecutar el contenedor**: Debe mostrar toda la salida esperada descrita arriba
3. **Verificar la lógica**: 
   - El stock debe disminuir correctamente después de cada pedido
   - Los totales de los pedidos deben ser correctos
   - El historial debe mostrar solo los pedidos del cliente específico

### Estructura del proyecto

```
.
├── dockerfile
├── .dockerignore
├── requirements.txt
├── Main/
│   └── main.py
├── Models/
│   ├── Usuario.py
│   ├── Producto.py
│   └── Pedido.py
└── Tienda Service/
    └── Tienda_service.py
```

## Desarrollo

### Requisitos
- Python 3.12
- Docker (para contenerización)

### Tecnologías utilizadas
- Python 3.12-slim (imagen base)
- Módulos estándar de Python (datetime)
