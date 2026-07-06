# Acceptance Testing - Grupo 5

Proyecto de pruebas de aceptación con [Behave](https://behave.readthedocs.io/) (BDD para Python).

## Requisitos

- Python 3.10+
- pip

## Setup del entorno

```bash
# Clonar el repositorio
git clone <url-del-repo>
cd acceptance-testing-grupo5

# Crear y activar el virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Instalar dependencias
pip install behave

# Verificar instalación
behave --version
```

## Estructura del proyecto

```
acceptance-testing-grupo5/
├── features/          # Archivos .feature (escenarios en Gherkin)
│   └── steps/         # Step definitions (implementación de los pasos)
├── .gitignore
└── README.md
```

## Ejecutar los tests

```bash
behave
```

## Equipo

- Grupo 5
