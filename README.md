# geocoding

* **Overview**
  - Basic Python script that parses a csv file of addresses, geocodes them, and writes the address, latitude, and longitude to a new csv file.

* **Example Usage**
  - Have addresses saved in csv file called `addresses.csv` in the same directory as `geocoding.py`.
  - Save addresses in the format:
 
    ```
    directions1, city1, state1, zip1
    directions2, city2, state2, zip2
    directions3, city3, state3, zip3
    etc...
    ```
    
  - Run the script and geocoded info will be written to a new csv file called `geocoded_addresses.csv`.
  - Any existing data in `geocoded_addresses.csv` will be overwritten.
