# WFM - Wow File Manager 📁🔍

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/GUI-PySide6-green.svg)](https://doc.qt.io/qtforpython/)
[![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Gestor de Archivos Académicos Automatizado** - Sistema inteligente con interfaz gráfica para organización automática de archivos y clustering de documentos PDF académicos mediante algoritmos TF-IDF y K-means.

## Características Principales

- **Clasificación Automática por Tipo**: Organiza archivos en carpetas por extensión (PDFs, documentos, imágenes, código, etc.)
- **Clustering Inteligente**: Agrupa documentos PDF por contenido usando TF-IDF + K-means
- **Índice Invertido**: Búsqueda eficiente por palabras clave en documentos PDF
- **Interfaz Gráfica**: GUI intuitiva desarrollada con PySide6/Qt
- **Extracción de Texto**: Procesamiento robusto de PDFs con PyMuPDF
- **Filtrado Avanzado**: Eliminación de stopwords en español e inglés
- **Persistencia**: Guarda índices en formato JSON para sesiones futuras

## Inicio Rápido

### Prerrequisitos
```bash
# Python 3.8 o superior
python --version

# Instalar dependencias
pip install PySide6 PyMuPDF scikit-learn
```

### Instalación
```bash
git clone https://github.com/RodrigoAlexander7/Automated_File_Manager.git
cd Automated_File_Manager
pip install -r requirements.txt
```

### Uso Básico
```bash
# Ejecutar la aplicación con interfaz gráfica
python main.py

# O ejecutar módulos específicos
python -m app.clustering  # Para clustering de documentos
python -m app.file_manager  # Para organización de archivos
```

## Ejemplo de Uso

```bash
# Entrada: Carpeta con archivos desorganizados
/Documents/
├── calculo1.pdf
├── algoritmos.docx
├── imagen.jpg
├── codigo.py
└── presentacion.pptx

# Salida: Estructura organizada automáticamente
/Documents/WFM_Organized/
├── pdf_files/
│   ├── calculo1.pdf
│   └── index.json  # Índice invertido generado
├── other_files/
│   ├── docs_files/
│   │   └── algoritmos.docx
│   ├── media/
│   │   └── imagen.jpg
│   ├── code_files/
│   │   └── codigo.py
│   └── slides_files/
│       └── presentacion.pptx
```

## Arquitectura

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│    main.py      │───▶│    gui.py       │───▶│ file_manager.py │
│  (Entry Point)  │    │  (PySide6 GUI)  │    │ (Organization)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  pdf_reader.py  │───▶│   indexer.py    │───▶│  clustering.py  │
│  (PyMuPDF)      │    │ (Inverted Index)│    │ (TF-IDF+KMeans) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   constant.py   │    │    utils.py     │    │   selector.ui   │
│ (Configuration) │    │  (Utilities)    │    │  (Qt Designer)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Tecnologías

- **Lenguaje**: Python 3.8+
- **GUI Framework**: PySide6 (Qt for Python)
- **PDF Processing**: PyMuPDF (pymupdf)
- **Machine Learning**: scikit-learn (TF-IDF, K-means)
- **Data Structures**: defaultdict, frozenset, pathlib
- **Serialization**: JSON para persistencia de índices
- **Text Processing**: Regex, stopwords filtering

## Características

- **Organización**: Clasificación automática por 8 tipos de archivos diferentes
- **Procesamiento PDF**: Extracción de texto con filtrado de stopwords bilingüe
- **Clustering**: Agrupación inteligente de documentos por contenido
- **Interfaz**: GUI moderna e intuitiva con PySide6
- **Precisión**: Clustering efectivo con algoritmos TF-IDF optimizados
- **Formatos**: Soporte para PDF, DOC, DOCX, TXT, imágenes, código, y más

## Contribución

Este proyecto fue desarrollado como trabajo final del curso de Estructuras de Datos, enfocado en **Responsabilidad Social Universitaria (RSU)** para beneficiar a la comunidad estudiantil.

### Equipo de Desarrollo
- Desarrolladores del curso de Estructuras de Datos
- Institución académica participante

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Reconocimientos

Proyecto desarrollado aplicando estructuras de datos avanzadas para resolver problemáticas reales de gestión documental en el ámbito universitario.

---

**¿Te fue útil?**  ¡Dale una estrella al repositorio :)!