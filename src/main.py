from scraping import scrape_quotes
from data_processing import process_data

def main():
    # Realizar el web scraping y obtener el DataFrame
    quotes_df = scrape_quotes()

    # Procesar y guardar los datos en la base de datos
    process_data(quotes_df)

if __name__ == '__main__':
    main()
