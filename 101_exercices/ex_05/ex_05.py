import threading
from urllib.request import urlopen
from PIL import Image

class Challenge5:

    def aspect_ratio(self, url):
        threading.Thread(target=self._aspect_ratio_thread, args=(url,)).start()

    def _aspect_ratio_thread(self, url):
        aspect_ratio_str = None

        with urlopen(url) as response:
            f = Image.open(response)
            width, height = f.size
            aspect_ratio = self.rational_aspect_ratio(height / width)
            aspect_ratio_str = f"{aspect_ratio[1]}:{aspect_ratio[0]}"

        if aspect_ratio_str:
            print(f"El aspect ratio es {aspect_ratio_str}")
        else:
            print("No se ha podido calcular el aspect ratio")

    class Quadruple:
        def __init__(self, h1, k1, h, k):
            self.h1 = h1
            self.k1 = k1
            self.h = h
            self.k = k

    def rational_aspect_ratio(self, aspect_ratio):
        precision = 1.0E-6
        x = aspect_ratio
        a = round(x)
        q = self.Quadruple(1, 0, a, 1)

        while abs(x - a) > precision * q.k * q.k:
            x = 1.0 / (x - a)
            a = round(x)
            q = self.Quadruple(q.h, q.k, q.h1 + a * q.h, q.k1 + a * q.k)

        return (q.h, q.k)

# Ejemplo de uso
challenge = Challenge5()
challenge.aspect_ratio("https://assets.pokemon.com/assets/cms2/img/pokedex/full/134.png")

