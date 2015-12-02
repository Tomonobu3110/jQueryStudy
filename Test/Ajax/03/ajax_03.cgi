#!/usr/bin/perl

use lib lib; # library path

# use strict;
use warnings;
use CGI;
use JSON;

# Test script for Ajax trial
# ajax_03.cgi
#   02-Dec, 2015
# by Saito Tomonobu (Tomonobu.Saito@gmail.com)

# get parameter (name is 'C')
$http = new CGI;
$c = $http->param('C');

# sleep 3 sec (emulation of heavy task.)
sleep 3;

# construct response
my $res = {
	name => 'Tomonobu Saito',
	count => $c + 1,
};

# output response (json wrapped HTML)
print "Content-type: text/html; charset=utf-8\n";
print "\n";
print "<html><body><div id='res'>";
print encode_json $res;
print "</div></body></html>\n";

# eof
