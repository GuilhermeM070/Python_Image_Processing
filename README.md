# Image Processor

Overview:
This is a simple Python package for image processing. It allows you to convert images to grayscale and invert their colors.

Features:
Convert images to grayscale.
Invert the colors of images.

## 📌 Instalação

```bash
pip install .
```

## 🚀 Uso

```python
from image_processor import convert_to_grayscale, invert_colors

convert_to_grayscale("imagem.jpg", "imagem_cinza.jpg")
invert_colors("imagem.jpg", "imagem_invertida.jpg")
```

## 📂 Estrutura do Projeto
```
image_processor/
│── image_processor/
│   ├── __init__.py
│   ├── filters.py
│   ├── utils.py
│── tests/
│   ├── test_filters.py
│── setup.py
│── README.md
```

## 🛠 Dependências
- Pillow (para manipulação de imagens)

## 📄 Licença
Este projeto está sob a licença MIT.
"""
