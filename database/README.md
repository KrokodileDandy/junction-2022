
# Delivering Attractive Maps Now! ... DAMN!

## Setup

Download the [imposm](https://imposm.org/docs/imposm3/latest/install.html) tool and some Open Streat Map file (.pbf), e.g., of [Helsinki](https://www.hsl.fi/en/hsl/open-data#open-street-map).

```bash
sudo wget -c https://github.com/omniscale/imposm3/releases/download/v0.11.1/imposm-0.11.1-linux-x86-64.tar.gz
```

Unpack the imposm tool by executing `sudo tar -xf imposm-0.11.1-linux-x86-64.tar.gz`.

```bash
sudo ./imposm-0.10.0-linux-x86-64/imposm import -mapping mapping.yml -read "Helsinki.osm.pbf" -overwritecache -write -connection postgis://simra:simra12345simra@localhost/simra
```
