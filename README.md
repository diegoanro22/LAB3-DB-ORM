
# LAB3-DB-ORM 🏨

Este proyecto es parte del **Laboratorio 3 de la clase de Bases de Datos 1**, y consiste en el desarrollo de una aplicación CRUD usando Django y su ORM, para la gestión de reservas en un hotel. La aplicación incluye relaciones entre huéspedes, habitaciones, tipos de habitaciones, servicios, reservas y pagos.

El sistema también integra una vista SQL (`VIEW`) para facilitar la visualización consolidada de datos de varias tablas, cumpliendo con los requerimientos del laboratorio.

---

## 🧠 Funcionalidades principales

- CRUD completo para **reservas**
- Formulario interactivo con validaciones (fechas válidas, selección de huéspedes, etc.)
- Vista consolidada (`vista_reservas_completas`) para mostrar información relacionada
- Frontend sencillo basado en templates de Django + Bootstrap
- API REST disponible para todas las entidades (opcional)

---

## ⚙️ Requisitos

- Python 3.10+
- pip
- Git
- SQLite3 (por defecto) o cualquier otro gestor de base de datos compatible con Django

---

## 🚀 Instrucciones de instalación

1. **Clonar el repositorio**

\`\`\`bash
git clone https://github.com/usuario/LAB3-DB-ORM.git
cd LAB3-DB-ORM
\`\`\`

2. **Crear y activar un entorno virtual**

\`\`\`bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
\`\`\`

3. **Instalar dependencias**

\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. **Crear archivo de entorno**

\`\`\`bash
cp .env.example .env
\`\`\`

5. **Crear y configurar la base de datos**

\`\`\`bash
python manage.py migrate
\`\`\`

6. **Insertar datos de prueba**

\`\`\`bash
# Abre tu gestor de base de datos o usa este comando si tienes SQLite instalado
sqlite3 db.sqlite3 < data.sql
sqlite3 db.sqlite3 < view.sql
\`\`\`

> 🔹 Asegúrate de que los archivos `data.sql` (para poblar datos) y `view.sql` (para crear `vista_reservas_completas`) estén en la raíz del proyecto.

7. **Levantar el servidor**

\`\`\`bash
python manage.py runserver
\`\`\`

---

## 🌐 Interfaz

- CRUD Web: http://localhost:8000/
- Documentación API: http://localhost:8000/docs/
- Panel de administración (si activas el superusuario): http://localhost:8000/admin/

---

## 📁 Estructura del Proyecto

\`\`\`
hotel/
├── migrations/
├── templates/
│   └── reservations/
│       ├── index.html
│       ├── form.html
│       └── confirm_delete.html
│   └── base.html
├── models.py
├── views.py
├── forms.py
├── serializers.py
\`\`\`

---

## 📌 Notas adicionales

- Se utilizaron **tipos de datos personalizados** como `DecimalField` para valores monetarios y `CharField` con `choices` para campos con valores restringidos.
- El CRUD se implementa tanto con **Django clásico (HTML + ORM)** como con **API REST (DRF)**.

---

## 🧑‍💻 Autor

- Nombre:
- Universidad del Valle de Guatemala
- Curso: cc3088 - Bases de Datos 1

