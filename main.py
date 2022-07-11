import cloudscraper
import fastapi

app = fastapi.FastAPI()
scraper = cloudscraper.create_scraper()


@app.get("/")
def read_root():
    r = scraper.get("https://www.moneysavingexpert.com/news/feeds/news.rss")
    return fastapi.Response(content=r.text, media_type=r.headers["content-type"])
