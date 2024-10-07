import apartment_data_fetcher
from apartment_data_db_mysql import ApartmentDataDatabase
import visualization
from config import SCRAPING_TARGET

data = []

def main():
    url = SCRAPING_TARGET
    data_fetcher = apartment_data_fetcher.ApartmentDataFetcher(url)
    apartment_data = data_fetcher.get_apartment_data()
    if apartment_data:
        date, universal_sqm_price_huf, universal_sqm_price_eur, one_million_huf_to_eur = apartment_data
        data = [date, universal_sqm_price_huf, universal_sqm_price_eur, one_million_huf_to_eur]
        db_handler = ApartmentDataDatabase()
        db_handler.create_table()
        db_handler.insert_data_db(*data)
        visualization.visualize()
    else: print("No data found.")   

if __name__ == "__main__":
    main()    

    