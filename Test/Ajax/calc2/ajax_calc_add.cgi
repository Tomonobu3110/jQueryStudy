#!/usr/bin/perl

use lib lib; # library path

# use strict;
use warnings;
use CGI;
use JSON;

# Test script for Ajax trial
# ajax_calc_add.cgi
#   02-Dec, 2015
# by Saito Tomonobu (Tomonobu.Saito@gmail.com)

# get parameter (a and b)
$http = new CGI;
$json = $http->param('POSTDATA');
$data = decode_json $json;
$a    = $data->{"a"};
$b    = $data->{"b"};

# sleep 3 sec (emulation of heavy task.)
sleep 3;

# construct response
my $res = {
	func => "add",
	a    => $a,
	b    => $b,
	res  => $a + $b,
};

# output response (json wrapped HTML)
print "Content-type: text/html; charset=utf-8\n";
print "\n";
print "<html><body><div id='res'>";
print encode_json $res;
print "</div></body></html>\n";

# eof
