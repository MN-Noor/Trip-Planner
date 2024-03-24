
from wiki import WebScrapper

def main(city):
    num_results = 5
    query = f'picnic spots  in {city}'
    scraper = WebScrapper(query, num_results)
    scraper.webscrapper()
    
if __name__ == "__main__":
    city = input("Enter the city name: ")
    main(city)

