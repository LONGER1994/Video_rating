import requests
from bs4 import BeautifulSoup
import csv

# 指定IMDb網頁的URL
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Referer": "https://www.example.com",
}

# 發送HTTP請求並取得網頁內容
response = requests.get(url, headers=headers)

# 使用Beautiful Soup解析網頁內容
soup = BeautifulSoup(response.text, "html.parser")

# 創建CSV檔案，以寫入模式打開
with open("movie_data.csv", "w", newline="") as csv_file:
    # 創建CSV寫入器
    csv_writer = csv.writer(csv_file)

    # 寫入CSV標題行
    csv_writer.writerow(
        [
            "Title",
            "Rating",
            # "Cast",
            # "Release Year"
        ]
    )

    # 找到包含熱門影片資訊的元素，通常是在<div>標籤中
    movie_elements = soup.find_all(
        "li", class_="ipc-metadata-list-summary-item sc-59b6048d-0 jemTre cli-parent"
    )

    # 遍歷每個影片元素，並提取相關資訊
    for movie in movie_elements:
        title = movie.find(
            "h3",
            class_="ipc-title__text",
        ).get_text()
        rating = movie.find(
            "span",
            class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating",
        ).get_text()

        # # 找到演員列表，通常在<div>標籤中
        # actors_element = movie.find("div", class_="list-description")
        # if actors_element:
        #     actors = actors_element.get_text(strip=True)
        # else:
        #     actors = "演員資訊不可用"

        # # 找到上映年份，通常在<span>標籤中
        # year_element = movie.find("span", class_="list-description-year")
        # if year_element:
        #     year = year_element.get_text()
        # else:
        #     year = "上映年份不可用"

        # 寫入該部影片的資訊到CSV檔案
        csv_writer.writerow(
            [
                title,
                rating,
                # actors,
                # year
            ]
        )

print("資料已成功匯出到movie_data.csv檔案")
