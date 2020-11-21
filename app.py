#!/usr/bin/env python3
from flask import Flask, render_template, url_for
import socket
import pandas as pd
from sqlalchemy import create_engine

HostName = socket.gethostbyname(socket.gethostname())
app = Flask(__name__)

@app.route('/')
def summary():
  sqlite_engine = create_engine('sqlite:///pcap.db')
  query = 'select ip_src as Sender, ip_dst as Receiver, sum(length) as TotalBytes from summary '\
    'group by Sender, Receiver '\
    'order by TotalBytes desc '\
    'limit 3'
  totalBytes = pd.read_sql(sql = query, con = sqlite_engine)
  return totalBytes.to_html()

if __name__ == '__main__':
  app.run()
