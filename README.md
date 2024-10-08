
# Real Estate Data Project LOCAL version

## Overview
- The Real Estate Data Project is a Python application designed to scrape, store, and visualize real estate market data. It connects to an API or data source to fetch apartment data, stores the information in a MySQL database, and provides visualization capabilities through various charting libraries. This first version of the project is designed to work with data from the hungarian real estate market, but it can be easily adapted to work with other sources. I called this LOCAL, because this version is designed to do ETL (Extract, Transform, Load) operations on a local machine, without the need for a cloud-based database.
The next version of the project will be designed to work with a cloud-based database (AWS cloud service), allowing for non-stop data collection and analysis.
- For now, this version after the etl operations, compares the highly volatile Hungarian Forint (1 million HUF to EUR daily exchange rate) with the real estate prices in Debrecen, Hungary. Note that I created a universal square meter price index for the purpose of this comparison. This index calculates the average sqm price of fifty 50 to 60 sqm apartments. Further development of this project will include more sophisticated analysis.

## Features
- Fetch real estate data from a specified source.
- Store data in a MySQL database, automatically creating the database and tables if they don’t exist.
- Visualize the fetched data using charts for better understanding of market trends.
- Designed with modularity in mind, allowing for easy expansion and modification.

## Installation and prerequisites
See SETUP.md for installation, prerequisites, and configuration instructions.

## Run the project
To run the project, follow these steps:
1. Open VsCode or any other IDE.
2. Open the project folder.
3. Run the following script to create a new table in your MySQL database: apartment_data_db_mysql.py
4. Run twice (bug no.2) the following script to fetch, store, and visualize data: main.py

KNOWN BUGS:
1. after configuring this project on your local machine, you need to first run apartment_data_sd_mysql.py 
    to create the table. For some reason the table is not being created automatically in the main.py.
2. run main.py twice to properly update the table with new data.

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create your feature branch (git checkout -b feature/MyFeature).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/MyFeature).
5. Open a pull request.

## License
This project is licensed under *Personal Use Only License* - see the LICENSE file for details.
