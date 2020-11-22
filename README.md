# firewall
A Python application to learn how to analyse network data to make a firewall

The first version consists of

* app.py - Flask application that makes a summary from an SQLite database

* pcap.db - SQLite database containing some data

To install the required python packages

```pip3 install -r requirements.txt```

To run the application do the following from a terminal

```python3 -m flask run --host=0.0.0.0 --port=5000```
