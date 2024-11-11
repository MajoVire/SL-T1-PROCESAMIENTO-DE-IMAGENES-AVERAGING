from PIL import Image
import matplotlib.pyplot as plt

def load_image(filepath):
    # Carga la imagen desde el archivo dado y la convierte a RGB.
    return Image.open(filepath).convert("RGB")

def apply_averaging_blur(image, kernel_size):
    # Aplica el método de suavizado de promediado en la imagen a color con un kernel de tamaño definido.
    width, height = image.size
    pixels = image.load()

    # Crear una nueva imagen para almacenar el resultado
    blurred_image = Image.new("RGB", (width, height))
    blurred_pixels = blurred_image.load()

    # Calcular el rango del kernel
    offset = kernel_size // 2

    # Recorrer cada píxel de la imagen, evitando los bordes según el tamaño del kernel
    for x in range(offset, width - offset):
        for y in range(offset, height - offset):
            # Inicializar sumas para cada canal de color
            total_r, total_g, total_b = 0, 0, 0
            count = 0
            for i in range(-offset, offset + 1):
                for j in range(-offset, offset + 1):
                    r, g, b = pixels[x + i, y + j]
                    total_r += r
                    total_g += g
                    total_b += b
                    count += 1
            # Calcular el promedio para cada canal
            blurred_pixels[x, y] = (total_r // count, total_g // count, total_b // count)

    return blurred_image

filepath ="image90.png"
kernel_size = 9
image = load_image(filepath)
# Aplicar el filtro de suavizado con el tamaño de kernel especificado
blurred_image = apply_averaging_blur(image, kernel_size)

# Mostrar la imagen original con ruido y la procesada
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image)
axes[0].set_title("Imagen Original con Ruido")
axes[0].axis("off")
axes[1].imshow(blurred_image)
axes[1].set_title("Imagen Suavizada")
axes[1].axis("off")
plt.show()