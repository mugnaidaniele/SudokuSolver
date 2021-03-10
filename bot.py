import telepot
import cv2
from image_processing import *
from sudoku import Sudoku


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        bot.sendMessage(chat_id, 'Dio cane manda un sudoku!')
    elif content_type == "photo":
        bot.sendMessage(chat_id, "Ricevuta immagine")
        bot.download_file(msg["photo"][-1]["file_id"], "image.jpg")
        original = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
        processed = pre_process_image(original)
        corners = find_corners_of_largest_polygon(processed)
        cropped = crop_and_warp(original, corners)
        squares = infer_grid(cropped)
        digits = get_digits(cropped, squares, 28)
        grid = cell_to_img(digits)
        # show_image(cropped)
        s = Sudoku(grid)
        print("Sudoku Input")
        s.show_grid()
        print()
        print("Sudoku Solution")
        solution = s.solver()
        print(solution)
        bot.sendMessage(chat_id, str(solution))


TOKEN = '1647483281:AAFc2u6tP-fcZBqze135jgbtvW-i3YAqzxo'

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print('Listening ...')

import time

while 1:
    time.sleep(10)
