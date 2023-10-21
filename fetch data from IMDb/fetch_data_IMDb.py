from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv

options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-extensions")
# options.add_argument("--headless")
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
# )


# 創建一個Chrome瀏覽器實例，請確保已安裝Chrome並下載相應的Chrome WebDriver
driver = webdriver.Chrome(options=options)

# 指定IMDb網頁的URL
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

# 打開網頁
driver.get(url)

# 使用execute_script方法來滾動網頁，等待網頁完全載入
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 等待一些時間，以確保網頁載入完成（可以根據需要調整等待時間）
driver.implicitly_wait(10)

# 找到包含熱門影片資訊的元素，通常是在<div>標籤中
movie_elements = driver.find_elements(
    By.CLASS_NAME,
    "ipc-metadata-list-summary-item sc-59b6048d-0 jemTre cli-parent",
)

print(movie_elements)

# # 創建CSV檔案，以寫入模式打開
# with open("movie_data_selenium.csv", "w", newline="") as csv_file:
#     # 創建CSV寫入器
#     csv_writer = csv.writer(csv_file)

#     # 寫入CSV標題行
#     csv_writer.writerow(
#         [
#             "Title",
#             "Rating"
#             #  , "Cast", "Release Year"
#         ]
#     )

#     # 遍歷每個影片元素，並提取相關資訊
#     for movie in movie_elements:
#         title = movie.find_element(
#             By.CLASS_NAME,
#             "ipc-poster-card__title ipc-poster-card__title--clamp-2 ipc-poster-card__title--clickable",
#         ).text
#         rating = movie.find_element(
#             By.CLASS_NAME,
#             "ipc-rating-star ipc-rating-star--baseAlt ipc-rating-star--imdb ipc-rating-star-group--imdb",
#         ).text

#         # # 找到演員列表，通常在<div>標籤中
#         # actors_element = movie.find_element(By.CLASS_NAME, "list-description")
#         # actors = actors_element.text.strip()

#         # # 找到上映年份，通常在<span>標籤中
#         # year_element = movie.find_element(By.CLASS_NAME, "list-description-year")
#         # year = year_element.text

#         # 寫入該部影片的資訊到CSV檔案
#         csv_writer.writerow(
#             [
#                 title,
#                 rating
#                 #  , actors, year
#             ]
#         )

print("資料已成功匯出到movie_data_selenium.csv檔案")

# 關閉瀏覽器
driver.quit()
