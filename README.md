Bootcamp TripleTen-QA Project Urban Routes Aldo Tablas Ramírez 

-Descripción del proyecto
Este proyecto automatiza la prueba funcional de la aplicación web Urban Routes, que permite solicitar taxis en una ciudad.  
El objetivo es verificar que el flujo completo de solicitud de un taxi funcione correctamente, incluyendo la selección de ruta, tarifa, confirmación telefónica, método de pago y solicitud de servicios adicionales.

-Tecnologías y técnicas utilizadas
1. Python 3: Lenguaje de programación para escribir los tests.
2. Selenium WebDriver**: Biblioteca para automatizar el navegador Chrome.
3. WebDriverWait y Expected Conditions: Para manejar elementos dinámicos en la página y evitar errores por sincronización.
4. Chrome DevTools Protocol (CDP): Para obtener logs de red.
5. PO (Page Object) pattern: Para estructurar los selectores y acciones sobre la interfaz en la clase `UrbanRoutesPage`.
6. pytest: Framework para organizar y ejecutar los tests.

-Qué hice en el proyecto
1.Analicé el flujo funcional completo de la aplicación Urban Routes.
2.Diseñé y desarrollé **pruebas automatizadas end-to-end** para el proceso de solicitud de un taxi.
3.Implementé el **patrón Page Object** para organizar selectores y acciones en la clase `UrbanRoutesPage`.
4.Automatizé la validación de:
  - Selección de origen y destino
  - Elección de tarifa
  - Confirmación de número telefónico
  - Selección de método de pago
  - Solicitud de servicios adicionales
5.Utilicé **WebDriverWait y Expected Conditions** para manejar elementos dinámicos y evitar problemas de sincronización.
6.Capturé **logs de red** mediante **Chrome DevTools Protocol** para validar el comportamiento de las solicitudes.
7.Ejecuté los tests utilizando **pytest** y validé los resultados obtenidos.

---

- Resultados obtenidos
1.Validación exitosa del flujo completo de solicitud de taxi.
2.Detección de posibles fallas en la carga y respuesta de algunos componentes dinámicos.
3.Confirmación del correcto manejo de datos ingresados por el usuario.
4.Mejora en la cobertura de pruebas funcionales de la aplicación web.
5.Aumento de la estabilidad de los tests mediante el uso de esperas explícitas.

-Cómo ejecutar las pruebas
1. Asegúrate de tener instalado Python 3 y pip.
2. Instala las dependencias necesarias con: pip install selenium pytest
3. Descarga el [ChromeDriver](https://chromedriver.chromium.org/downloads) compatible con la versión de tu navegador Chrome y colócalo en tu PATH.
4. Clona el repositorio o copia el código fuente del proyecto.
5. Define los datos de prueba en el archivo `data.py` con las variables necesarias
6. Ejecuta los tests con: pytest main.py
7. Observa los resultados en la consola.
