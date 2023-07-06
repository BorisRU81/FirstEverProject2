import os  # еще одна библиотека PyQt5 - графический
from io import BytesIO  #Читает битовый массив
from datetime import datetime
from tkinter import *  # подключаем элементы tkinter
from tkinter import filedialog  # для выбора картинки
from PIL import Image, ImageTk, ImageFilter  # для обработки изображения
import requests


class App:
    def __init__(self):
        self.w = None
        self.h = None
        self.window = Tk()  # Создали окно
        self.window.title('Поиск по карте')
        self.window.geometry('900x625')
        self.window.resizable(False, False)
        self.window.iconphoto(False, PhotoImage(file='Rat.png'))
        self.apikey = '40d1649f-0493-4b70-98ba-98533de7710b'
        self.name = 'СПБ, Миллионная,11'
        self.geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey={self.apikey}&geocode={self.name}&kind=metro&format=json'
        self.label = Label(text='Обработка твоего кривого изображения', background='purple', foreground='white',
                           font=('Verdana', 16))
        self.label.pack(fill=X, pady=5)
        self.canvas = Canvas(bg='white', width=600, height=450)
        self.canvas.pack(anchor=CENTER, pady=15)
        self.load = Button(text='Найти', background='yellow', command=self.open)
        self.load.pack(anchor=N, side=LEFT, padx=50, fill=X, expand=True)
        self.place = Entry(width=40, font=('Verdana', 16))
        self.place.pack(anchor=N, side=LEFT, padx=50, fill=X, expand=True)
        # self.blur = Button(text='Нет, сюда', background='orange', command=self.blur)
        # self.blur.pack(anchor=N, side=LEFT, padx=50, fill=X, expand=True)
        self.dtime = Label(background='grey', foreground='white', font=('Verdana', 26))
        self.dtime.place(x=310, y=570)
        self.cwd = os.getcwd()
        self.image = NONE  # Заглушка
        self.orig = Image.new('RGB', (600, 400), (255, 255, 255))
        self.show_time()
        self.window.mainloop()

    def open(self):
        self.name = self.place.get()
        self.geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey={self.apikey}&geocode={self.name}&kind=metro&format=json'
        response = requests.get(self.geocoder_request)
        info = response.json()
        coords = info['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        coords = ','.join(coords.split())
        delta = '0.0095,0.0095'
        map_param = {
            'll': coords,
            'spn': delta,
            'l': 'map',
            'pt': f'{coords},pm2dgl'
        }
        api_server = 'https://static-maps.yandex.ru/1.x/'
        image_map = requests.get(api_server, params=map_param)
        pic_to_show = Image.open(BytesIO(image_map.content))
        self.image = ImageTk.PhotoImage(pic_to_show)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        #print(response)


    #     try:
    #         fullpath = filedialog.askopenfilename(title='Выбор картинки', initialdir=self.cwd, filetypes=(
    #             ('GIF', '*,gif'), ('PNG', '*.png'), ('JPG', '*.jpg'), ('JPEG', '*.jpeg')
    #         ))
    #         self.orig = Image.open(fullpath)
    #         self.w, self.h = self.orig.size
    #         if self.w > 600:
    #             ratio = self.w / 600
    #             self.orig = self.orig.resize((600, int(self.h / ratio)))
    #         self.image = ImageTk.PhotoImage(self.orig)
    #         self.canvas.create_image(0, 0, anchor=NW, image=self.image)
    #     except AttributeError:
    #         self.image = ImageTk.PhotoImage(self.orig)
    #         self.canvas.create_image(0, 0, anchor=NW, image=self.image)
    #
    # def blur(self):
    #     blur_image = self.orig.filter(ImageFilter.BLUR)
    #     self.image = ImageTk.PhotoImage(blur_image)
    #     self.canvas.create_image(0, 0, anchor=NW, image=self.image)
    #
    def show_time(self):  # Интеграция часов
        self.time_to_show = datetime.time(datetime.now()).strftime("%H:%M:%S")
        self.dtime['text'] = self.time_to_show
        self.dtime.after(1000, self.time_to_show)


if __name__ == '__main__':
    app = App()  # Пустое окно
