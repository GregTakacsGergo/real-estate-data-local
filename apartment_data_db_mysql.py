from db_config import func_real_db

class ApartmentDataDatabase:
    def __init__(self):
        self.real_db = func_real_db()
        self.my_cursor = self.real_db.cursor()

    def create_table(self):
        self.my_cursor.execute("""CREATE TABLE IF NOT EXISTS real_estate_market_data (
                                  date DATETIME PRIMARY KEY, 
                                  avg_sqm_price_huf MEDIUMINT UNSIGNED , 
                                  avg_sqm_price_eur SMALLINT UNSIGNED,
                                  one_million_huf_to_eur MEDIUMINT UNSIGNED)""")

    def check_existing_data(self, date):
        query = "SELECT * FROM real_estate_market_data WHERE date = %s"
        self.my_cursor.execute(query, (date, ))
        result = self.my_cursor.fetchall()
        return len(result) > 0

    def insert_data_db(self, date, universal_sqm_price_huf, universal_sqm_price_eur, one_million_huf_to_eur):
        if not self.check_existing_data(date):
            SQL_statement = """INSERT INTO real_estate_market_data (date, avg_sqm_price_huf, avg_sqm_price_eur,
                               one_million_huf_to_eur) VALUES (%s, %s, %s, %s)"""
            self.my_cursor.execute(SQL_statement, (date, universal_sqm_price_huf, universal_sqm_price_eur, one_million_huf_to_eur))
            self.real_db.commit()
        else:
            print("Az adat már megtalálható az adatbázisban.")
    
    def fetch_data_from_db(self):
        query = "SELECT date, avg_sqm_price_huf, avg_sqm_price_eur, one_million_huf_to_eur FROM real_estate_market_data"
        self.my_cursor.execute(query)
        result = self.my_cursor.fetchall()
        return result

def main():
    handler = ApartmentDataDatabase()
    handler.create_table()
   
if __name__ == "__main__":
    main()
