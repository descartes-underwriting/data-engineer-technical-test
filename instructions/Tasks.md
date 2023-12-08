# Task

Please look at the [Conventions.md](Conventions.md) file to understand how the task should be implemented in the project.

## Task 1 - Python & SQL

In a first part, using Python as programming language and SQLite3 as an SQL database, perform the tasks listed below.

### 1.1 Database initialization

In [../src/data-engineer-technical-test/database.py](../src/data-engineer-technical-test/database.py), initialize the SQL database with the necessary empty tables.

+ `earthquakes` with `id, latitude, longitude, magnitude, date`
+ `locations` with `id, name, latitude, longitude, value`
+ `losses` with `earthquake_id, location_id, net_loss` where `earthquake_id` and `location_id` are foreign keys

### 1.2 Client location parsing

In [../src/data-engineer-technical-test/locations.py](../src/data-engineer-technical-test/locations.py), read the provided `locations.csv` and insert its values in the database.

### 1.3 USGS API call

The API URL is stored in the `BASE_URL` variable. The API documentation can be found [here](https://earthquake.usgs.gov/fdsnws/event/1/)

In [../src/data-engineer-technical-test/api.py](../src/data-engineer-technical-test/api.py),

1. select the area of interest for the API request: "the *bounding box* of the client sites, expanded by 200km in each directions". (we assume that 200 km corresponds to 200 / 110.567 = 1.8089 degrees of latitude/longitude)
2. call the USGS API and store the retrieved data in the `earthquakes` table

*Notes:*

+ a bounding box is square centered on the client site, the sides of the square follow North-South and East-West directions
+ the time range of the data of interest is from 1900, January 1st to 2022, January 1st
+ the magnitude range of interest is 5 and above*

### 1.4 Payouts and loss computation

In [../src/data-engineer-technical-test/payouts.py](../src/data-engineer-technical-test/payouts.py).

1. populate the `losses` table with the relevant data using the provided payout structure (`payout_structure.csv`)
2. select the variables (year, earthquake, location, loss) from to payout table and export them to csv format
3. select the losses per event and export them to csv format
4. select the losses per year and export them to csv format

*Notes:*

+ As a simplification, we will use the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) to compute distance (instead of using a more complicated distance, as the Earth is not flat).

*Hint:*

+ A temporary table can be used before computing the final payout.

---

## Tasks 2 - Airflow

As a second part, use a Airflow DAG to write and run a data pipeline that will perform the steps implemented in the previous task.

The DAG must be written in [../src/data-engineer-technical-test/dag.py](../src/data-engineer-technical-test/dag.py).
