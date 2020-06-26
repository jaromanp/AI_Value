# Repositorio proyecto AI Value
![enter image description here](https://raw.githubusercontent.com/jaromanp/AI_Value/master/Logo.png)
## Integrantes
**Product Owner**
Juan Camilo Vanegas Pinto
jvaneg22@eafit.edu.co

**Desarrolladores** <br>
Alejandra Cárdenas Montoya
acarden6@eafit.edu.co,
acarden100@gmail.com

Mateo Flórez Restrepo
mflorezr@eafit.edu.co,
mflorez1@gmail.com

José Alejandro Román Patiño
jaromanp@eafit.edu.co,
alejandrojrp10@gmail.com

Laura Sánchez Córdoba
lsanchezc@eafit.edu.co,
laurasanchez1306@gmail.com

## Estructuración del proyecto
### [Carpeta Algorithm Server](https://github.com/jaromanp/AI_Value/tree/master/AlgorithmServer)
En esta carpeta se encuentra el servidor Django usado para desplegar el algoritmo genetico como servicio API - REST
### [Carpeta Combination](https://github.com/jaromanp/AI_Value/tree/master/Combination)
En esta carpeta se encuentran los esqueletos de los metodos de interpolación, algoritmo genético y red neuronal, la mayoria se encuentran en formato ipyn para mejor visualización durante la ejecución.
### [Carpeta LR Prediction](https://github.com/jaromanp/AI_Value/tree/master/LR_Prediction)
Archivos csv para la interpolación y versiones previas de esta
### [Varios intentos](https://github.com/jaromanp/AI_Value/tree/master/Varios%20Intentos)
Otros metodos usados al principio del proyecto

## Repositorio del servidor Backend
En el siguiente link se encuentra el repositorio del servidor Back end, usado para la autenticación y el guardado de datos.
Para esta parte del proyecto se uso [django](https://www.djangoproject.com/) y como base de datos se uso MySQL
<br>
[Link](https://github.com/lsanchezc613/AI-Value-Server)

## Repositorio del servidor Frontend
En el siguiente link se encuentra una parte del front end, contiene vista principales, de login y de register, estas no pudieron ser probadas con el servidor back desplegado en AWS, y su ejecucion solo ha sido posible en entorno nativo en windows se recomienda reestructuración o desarrollo desde 0 con otra tecnologia.
Se uso el framework [React](https://es.reactjs.org/)
<br>
[Link](https://github.com/mflorezr/Aifront)
### Aclaraciones y advertencias
La parte del dashboard que se estaba desarrollando se perdio, no obstante para la graficación se uso la libreria [chart.js](https://www.chartjs.org/), se recomienda seguir con esta en un futuro desarrollo de esta parte del front, se recomienda cambiar React por un framework más conocido por lo desarrollores o más facil de usar como por ejemplo [Vue](https://vuejs.org/).
La idea para integración de Front y Back es comunicacion meramente por API - REST,  tomando provecho de la parte del back ya realizada en la que se comprobo su funcionamiento mediante postman al igual que la parte del algoritmo que ya tambien esta implementada como servicio API

### Partes pendientes
- Comunicación entre los servicios
- Automatización de la entrada de datos
- Re-entrenamiento de la red neuronal con los datos de cada usuario 
- Gran parte del front end
- Tranformaciones de los datos automatica
- Modificación del algoritmo genetico para trabajar con los datos especificos del cliente
- Posible optimizacion del algoritmo genetico con paralelizacion 

