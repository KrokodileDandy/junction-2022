
# Delivering Attractive Maps Now! ... DAMN!

## Setup

Download the [imposm](https://imposm.org/docs/imposm3/latest/install.html) tool and some Open Streat Map file (.pbf), e.g., of [Helsinki](https://www.hsl.fi/en/hsl/open-data#open-street-map).

```bash
sudo wget -c https://github.com/omniscale/imposm3/releases/download/v0.11.1/imposm-0.11.1-linux-x86-64.tar.gz
```

Unpack the imposm tool by executing `sudo tar -xf imposm-0.11.1-linux-x86-64.tar.gz`. Then execute the following to populate the database:

```bash
# Read the PBF data and write to cache /tmp/imposm/
./imposm-0.11.1-linux-x86-64/imposm import -mapping mapping.yml -read Helsinki.osm.pbf -overwritecache
# Read the cache and write into the database
sudo ./imposm-0.11.1-linux-x86-64/imposm import -mapping mapping.yml -write -connection postgis://postgres:password@localhost:5555/damn-postgresql

./imposm-0.11.1-linux-x86-64/imposm import -mapping mapping.yml -read Helsinki.osm.pbf -overwritecache -write -connection postgis://alex:password@localhost:5432/gis
```

```bash
# Install docker
# Create container "alex"
sudo docker -it <name> bash
su postgres
psql # Login
$ \l # List databases
use gis # Switch to db
show tables
```

---

```bash
osm2pgsql -c -d damn-junction-2022 -U postgres -H junction-hack22esp-7060:europe-north1:damn-junction-2022 -S default.style Helsinki.osm.pbf
```