#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# определяете шрифт
font = ImageFont.truetype("Verdana.ttf", 10)

# определяете положение текста на картинке
text_position = (0, 0)

# цвет текста, RGB
text_color = (0,0,0)

# собственно, сам текст
text = 'hellow world'

# загружаете фоновое изображение
img = Image.open('blank.jpg')

# определяете объект для рисования
draw = ImageDraw.Draw(img)

# добавляем текст
draw.text(text_position, text, text_color, font)

# сохраняем новое изображение
img.save('blank_with_text.jpg')
