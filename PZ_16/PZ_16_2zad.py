class Image:
    def __init__(self, resolution: [int, int], title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, height, width):
        self.resolution = [height, width]

    def title_upper(self):
        self.title = self.title.upper()

Image1 = Image([350*700], 'tututu', 'haip')
Image2 = Image([430*500], 'margin', 'help')
Image3 = Image([305*100], 'sabmit', 'houp')

Image1.resize(100, 100)
print(f'Новое расширение Image1: {Image1.resolution}')
Image2.resize(200, 200)
print(f'Новое расширение Image2: {Image2.resolution}')
Image3.resize(300, 300)
print(f'Новое расширение Image3: {Image3.resolution}')

Image2.title_upper()
print(Image2.title)

