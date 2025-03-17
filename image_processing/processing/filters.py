from PIL import Image

def convert_to_grayscale(image_path, output_path):
    """Converte uma imagem colorida para tons de cinza."""
    image = Image.open(image_path).convert("L")
    image.save(output_path)
    print(f"Imagem convertida para {output_path}")

def invert_colors(image_path, output_path):
    """Inverte as cores de uma imagem."""
    image = Image.open(image_path)
    inverted_image = Image.eval(image, lambda x: 255 - x)
    inverted_image.save(output_path)
    print(f"Imagem com cores invertidas salva em {output_path}")

