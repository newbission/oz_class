from db.save_data import save_data
from scraping.naver_scraper import scrap

if __name__ == "__main__":
    save_data(scrap())