### Guía para Iniciar QASTACK en Trading Algorítmico con Zipline en Docker (2024)

#### Pasos para Principiantes:

1. **Clonar el Repositorio:**
   - Descarga la versión más reciente del código desde el repositorio.
-     ```
    git clone https://github.com/quantarmyz/quantstack.git
     ```


2. **Crear Archivo .env en DockerSource:**
   - Crea un archivo `.env` dentro de la carpeta `DockerSource`.
   - Formato del archivo:
     ```
     ENDPOINT=TuEndPoint.COM
     DB=TuBucket
     ACCESS_KEY=TuAccessKey
     SECRET_KEY=TuSecretKey
     ```
   - Guardar como:
     - `/quantstack/DockerSource/.env`

3. **Compilar la Imagen:**
   - Desde la terminal, en la ruta `/quantstack`, ejecuta:
     ```
     docker compose build --no-cache
     ```

4. **Configuración Opcional de Docker Compose:**
   - Edita `/quantstack/docker-compose.yml` según sea necesario (se recomienda configurar el token).

5. **Iniciar el Stack:**
   - Ejecuta el siguiente comando para el modo debug:
     ```
     docker compose up
     ```
   - Para ejecutar en segundo plano:
     ```
     docker compose up -d
     ```

6. **Acceder a JupyterLab:**
   - Si no se han realizado modificaciones, la dirección es:
     ```
     localhost:8888
     ```
   - Contraseña:
     ```
     testing
     ```

7. **Añadir Feed de Datos al JupyterLab:**
   - Desde el JupyterLab, abre un terminal y ejecuta:
     ```
     conda activate base
     zipline ingest -b qa_datalake
     ```
   - Esto conectará al datalake, descargará los datos y los añadirá a la base de datos de Zipline.

8. **Realizar Backtest:**
   - Después de completar el proceso de ingest, dirígete a la carpeta de backtests y realiza una prueba para asegurarte de que todo funcione correctamente.

-------
