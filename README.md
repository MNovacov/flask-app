# **Aplicación Flask: Gestión de Promedios y Comparación de Nombres**

Este proyecto es una aplicación web desarrollada con **Flask**, diseñada para mostrar habilidades tanto en desarrollo backend como en diseño frontend. La aplicación incluye dos funcionalidades principales que destacan la interacción con formularios y el procesamiento de datos en tiempo real, acompañadas de un diseño limpio y moderno.

---

## **Aspectos técnicos**
- **Framework:** Flask (Python).
- **Frontend:** 
  - HTML5 y CSS3.
  - Diseño responsivo y moderno con bordes circulares, degradados y fuente Roboto.
- **Gestión de formularios:**
  - Métodos HTTP `GET` y `POST` para procesar los datos enviados por el usuario.
- **Estilos visuales:** Implementa un diseño atractivo con un fondo degradado, colores vibrantes y contenedores estilizados con sombras y bordes redondeados.

---

## **Funcionalidades**
1. **Promedio de Notas:**
   - Permite ingresar tres notas y el porcentaje de asistencia.
   - Calcula el promedio de las notas y determina si el estudiante está aprobado o reprobado.
   - **Consideraciones para el estado de aprobado o reprobado:**
   - El promedio de las tres notas debe ser **mayor o igual a 40**.
   - La asistencia debe ser **mayor o igual al 75%**.

2. **Comparación de Nombres:**
   - Permite ingresar tres nombres.
   - Determina cuál es el nombre más largo y cuántos caracteres tiene.

---

## **Capturas de pantalla**

### Menú principal:
![Menú Principal](https://github.com/MNovacov/flask-app/blob/main/menu%20principal.png)

### Formulario de Promedio de Notas:
![Promedio de Notas](https://github.com/MNovacov/flask-app/blob/main/promedio%20de%20notas.png)

### Formulario de Comparación de Nombres:
![Comparación de Nombres](https://github.com/MNovacov/flask-app/blob/main/comparar%20nombres.png)


## **Cómo usar el proyecto**

```bash
# Clonar el repositorio
git clone https://github.com/MNovacov/flask-app.git
cd flask-app

# Crear un entorno virtual
python -m venv .venv

# Activar el entorno virtual
# En Windows:
.venv\Scripts\activate
# En Mac/Linux:
source .venv/bin/activate

# Instalar dependencias
pip install flask

# Ejecutar la aplicación
python main.py

# Acceder a la aplicación en el navegador
http://127.0.0.1:5000
