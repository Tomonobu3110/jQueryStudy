#!/usr/bin/perl

# use strict;
use warnings;
use CGI;

# Test script for Ajax trial
# ajax_01.cgi
#   01-Dec, 2015
# by Saito Tomonobu (Tomonobu.Saito@gmail.com)

# get parameter (name is 'C')
$http = new CGI;
$c = $http->param('C');

# output response (HTML)
print "Content-type: text/html; charset=utf-8\n";
print "\n";
print "<html><head></head><body> Hello World. </body></head></html>\n";
