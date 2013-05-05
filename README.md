Simple Dynamic DNS updater for Linode's DNS
========

## Quick Guide

Use `virtualenvwrapper` and `pip` to get things running.

    mkvirtualenv dyndns
    git clone git://github.com/denibertovic/dyndns.git
    cd dyndns
    pip install -r requirements.txt
    
    mv config.py.example config.py
    Edit config.py and fill in your settings.
    NOTE: You can use the default IP_SERVICE or change it to some other service.
    Just be sure it only returns the ip address as a string.

    Run it: python dyndns.py

## Requirements
  *  `python >= 2.7` 
  *  `see requirements.txt file for rest`

## License

Copyright (C) 2013. by Deni Bertović.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
