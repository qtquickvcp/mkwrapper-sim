# Simulator configuration for Machinekit mkwrapper

This example configuration need [Machinekit](http://machinekit,io)
installed on your computer.

## Start and run

To start this configuration either use run `run.py` or start
`mklauncher` with this directory as search path.

```bash
./run.py
```

The default search path for announced user interfaces are
`~/repos/Cetus` and `~/repos/Machineface`. To add an alternative search path use `./run.py -p <search_path>`.

Configserver scans the directory recursively.

## Install Cetus UI

Git clone the Cetus UI into your home directory:

```bash
cd
git clone https://github.com/qtquickvcp/Cetus.git
```

## Running the UI

To run the remote UI you need to download and install [MachinekitClient](https://github.com/qtquickvcp/QtQuickVcp#download) on your computer or mobile device.

When starting the UI select the Machinekit instance and UI.
