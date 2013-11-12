#!/usr/bin/env python
#Author: Le Kien Truc <afterlastangel@gmail.com>
#https://github.com/afterlastangel/outlook-new-email-indicator
#GPL V3
"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import sys
import gtk
import appindicator
import pynotify

import imaplib
import re
import os
import SocketServer
import thread
import gobject


import sys
import BaseHTTPServer
import SimpleHTTPServer
import urlparse
from SimpleHTTPServer import SimpleHTTPRequestHandler
gobject.threads_init() 

SERV_PORT = 8001
START_WEBSERV = u'Start server'
STOP_WEBSERV = u'Stop server'


PING_FREQUENCY = 10 # seconds
class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def do_GET(self):
       # Parse query data & params to find out what was passed
       parsedParams = urlparse.urlparse(self.path)       
       queryParsed = urlparse.parse_qs(parsedParams.query)

       # request is either for a file to be served up or our test
       if parsedParams.path == "/email":
          self.processIncomeRequest(queryParsed)
       elif parsedParams.path == "/clear":         
         self.processClearRequest(queryParsed)
          # Default to serve up a local file 
          #SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self);

  def processIncomeRequest(self, query):    
    indicator.ind.set_status(appindicator.STATUS_ATTENTION)
    n = pynotify.Notification ("New email received");
    n.set_urgency(pynotify.URGENCY_NORMAL)
    n.set_timeout(3)
    n.show();
    self.send_response(200)
    self.send_header('Content-Type', 'application/xml')
    self.end_headers()
    self.wfile.write("<?xml version='1.0'?>");
    self.wfile.write("<sample>New email</sample>");
    self.wfile.close();
  def processClearRequest(self, query):
    indicator.ind.set_status(appindicator.STATUS_ACTIVE)
    self.send_response(200)
    self.send_header('Content-Type', 'application/xml')
    self.end_headers()
    self.wfile.write("<?xml version='1.0'?>");
    self.wfile.write("<sample>Clear email</sample>");
    self.wfile.close();
class WebServer():
    def __init__(self):
        pass

    def start(self):
        Handler = MyHandler

        self.httpd = SocketServer.TCPServer(("", SERV_PORT), Handler)

        print "serving at port", SERV_PORT
        gtk.gdk.threads_enter()
        thread.start_new(self.httpd.serve_forever, tuple())
        gtk.gdk.threads_leave()

    def stop(self):
        #~ self.httpd.socket.close()
        return


class EmailChecker:
    def __init__(self):
        self.ind = appindicator.Indicator("outlook-new-email-indicator",
                                           "indicator-messages",
                                           appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon("indicator-messages-new")

        self.menu_setup()
        pynotify.init ("outlook-new-email-indicator")
        WebServer().start()
        self.ind.set_menu(self.menu)        
    def menu_setup(self):
        self.menu = gtk.Menu()        
        self.clear_item = gtk.MenuItem("Clear")
        self.clear_item.connect("activate", self.clear)
        self.clear_item.show()
        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.clear_item)

        self.menu.append(self.quit_item)        
        self.menu.show()
        self.ind.set_menu(self.menu)            
    def clear(self, data=None):
      self.ind.set_status(appindicator.STATUS_ACTIVE)
      
    def main(self):    
      gtk.gdk.threads_enter()
      gtk.main()
      gtk.gdk.threads_leave()

    def quit(self, widget):
        sys.exit(0)

if __name__ == "__main__":
    indicator = EmailChecker()
    indicator.main()
    indicator.start()

