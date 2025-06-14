QA Project Urban Routes Aldo Tablas Ramírez Sprint No. 8 Grupo 29

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

-Cómo ejecutar las pruebas
1. Asegúrate de tener instalado Python 3 y pip.
2. Instala las dependencias necesarias con: pip install selenium pytest
3. Descarga el [ChromeDriver](https://chromedriver.chromium.org/downloads) compatible con la versión de tu navegador Chrome y colócalo en tu PATH.
4. Clona el repositorio o copia el código fuente del proyecto.
5. Define los datos de prueba en el archivo `data.py` con las variables necesarias
6. Ejecuta los tests con: pytest main.py
7. Observa los resultados en la consola.