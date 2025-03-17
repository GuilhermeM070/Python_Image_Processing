from PIL import Image

def load_image(image_path):
    """Carrega e retorna uma imagem."""
    return Image.open(image_path)

def get_image_size(image_path):
    """Retorna o tamanho (largura, altura) da imagem."""
    with Image.open(image_path) as img:
        return img.size
