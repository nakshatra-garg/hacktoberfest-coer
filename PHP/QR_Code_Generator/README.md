## QR Code Generator 
Create Dynamic QR Code Generator app using php. You can Create QR code with text or Website URL. I use Library for generate QR Code.
QR Code save into images directory.

## Run Project on localhost
`"http://localhost/hacktoberfest-coer/PHP/QR_Code_Generator/"`

# Overview

PHP QR Code is open source (LGPL) library for generating QR Code, 2-dimensional barcode. Based on libqrencode C library, provides API for creating QR Code barcode images (PNG, JPEG thanks to GD2). Implemented purely in PHP, with no external dependencies (except GD2 if needed).

Some of library features includes:

* Supports QR Code versions (size) 1-40
* Numeric, Alphanumeric, 8-bit and Kanji encoding. (Kanji encoding was not fully tested, if you are japan-encoding enabled you can contribute by verifing it :) )
* Implemented purely in PHP, no external dependencies except GD2
* Exports to PNG, JPEG images, also exports as bit-table
* TCPDF 2-D barcode API integration
* Easy to configure
* Data cache for calculation speed-up
* Provided merge tool helps deploy library as a one big dependency-less file, simple to "include and do not wory"
* Debug data dump, error logging, time benchmarking

# Usage
To install simply include:

* `qrlib.php` for full version (also you have to provide all library files form package plus cache dir)
* OR `phpqrcode.php` for merged version (only one file, but slower and less accurate code because disabled cache and quicker masking configured)

` QRcode::png('code data text', 'filename.png'); // creates file `

` QRcode::png('some othertext 1234'); // creates code image and outputs it directly into browser ` 


Above examples show the most basic usage. For more features and customization see [Detailed examples](http://phpqrcode.sourceforge.net/examples/index.php) and  [PHP QR Code wiki](http://sourceforge.net/p/phpqrcode/wiki/) or read INSTALL file in distribution package. For Further information see this API Documention [http://phpqrcode.sourceforge.net/docs/html/index.html](http://phpqrcode.sourceforge.net/docs/html/index.html)

## Screenshot of QR code app

![screencapture-localhost-hacktoberfest2021-hacktoberfest-coer-PHP-QR-Code-Generator-2021-10-05-07_59_50](https://user-images.githubusercontent.com/63604585/135992266-a01924eb-5474-4285-a682-1d28ad03aaa3.png)




## Author

- [Vijay Chauhan](https://github.com/mr-vijaychauhan/)
