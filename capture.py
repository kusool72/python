import pyautogui as auto
import time
import pyperclip
import random

# 총 페이지 수
total_page = 273
# 파일명
book_name = 'ebook'
# 캡쳐버튼 좌표
capture_pos = (440, 108)
# 캡쳐화면 중앙 좌표
# ebook_screen_center_pos = (3600, 716)
# ebook right  버튼
ebook_screen_right_pos = (1706, 580)
sleep_time = 1.0

time.sleep(5.)

for i in range(123, int(total_page/2)+1):
    file_name = book_name + '_' + str(i + 1).zfill(3) + '.png'
    pyperclip.copy(file_name)

    auto.click(capture_pos)
    time.sleep(sleep_time)

    auto.hotkey('ctrl', 'v')
    time.sleep(sleep_time)

    auto.press('enter')
    time.sleep(sleep_time)

#    auto.click(ebook_screen_center_pos)
    auto.click(ebook_screen_right_pos)
    time.sleep(sleep_time*(round(random.random()*7)+10))

#    auto.press('right')
#    time.sleep(sleep_time)

    print(str(i+1), '/', int(total_page/2)+1)
