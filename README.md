
# Delivering Attractive Maps Now! ... DAMN!

## Usage

Navigate into the `damn/` folder and execute `python main.py`. This will start an example workflow of reading data from the database, comparing trips with shortest paths, and executing similar analyses with the data. Changes are written into the database and can be visualized with a tool like pgadmin 4. An example visualization of the data analysis in the database is depicted below:

![Lines depicting analyzed street segments in the database tool pgadmin 4.](https://github.com/KrokodileDandy/junction-2022/blob/main/doc/images/data_extract_improved-color-min.png)

A dynamic visualization is planned for a later stage of the project, but below is an image of what we envsion it might could look like. The figure visualizes the usage frequency of streets (with mockup data).

![The road network of Helsinki with different colors depending on the usage frequency, based on mockup data.](https://github.com/KrokodileDandy/junction-2022/blob/main/doc/images/Figure_1.png)

## Setup

### Database

Go to [Google Cloud](https://console.cloud.google.com/) and create a new PostgreSQL 13 instance. In this example the database has the IP address `34.88.101.46` and the database name is `damn-junction-2022`. Go to SQL > Users and reset the password of the user `postgresql` to a password you know. Then go to SQL > Connections and add the IP address of your machine to the list of authorized networks in order to allow for the database connections to work.

### Populate the Database

Install the tool `osm2pgsql` by running `sudo apt intall osm2pgsql`. Then run the following command to import the map data into the cloud postgresql database. Adapt the command to your needs. The example below uses map data from [Helsinki](https://www.hsl.fi/en/hsl/open-data#open-street-map) in the `Helsinki.osm.pbf` file, and the default style file of the `osm2pgsql` tool `default.style` is used. The database credentials are the same as above.

```bash
osm2pgsql -c -d damn-junction-2022 -U postgres -W -H 34.88.101.46 -S default.style Helsinki.osm.pbf
```
