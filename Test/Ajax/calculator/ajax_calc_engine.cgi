#!/usr/bin/perl

use lib lib; # library path

# use strict;
use warnings;
use CGI;
use JSON;

# Test script for Ajax trial
# ajax_calc_engine.cgi
#   04-Dec, 2015
# by Saito Tomonobu (Tomonobu.Saito@gmail.com)

# get parameter (a and b)
$http    = new CGI;
$json    = $http->param('POSTDATA');
$data    = decode_json $json;
$fomula  = $data->{"fomula"};
$lastkey = $data->{"lastkey"};

$result  = "";
if ($lastkey eq "=") {
	$result = eval { $fomula + 0; };
	if ($@) {
		$result = "ERROR: $@";
	}
	$fomula = "";
} else {
	$fomula = $fomula . " " . $lastkey;
}

# construct response
my $res = {
	lastkey => $lastkey,
	fomula  => $fomula,
	result  => $result,
};

# output response (json wrapped HTML)
print "Content-type: text/html; charset=utf-8\n";
print "\n";
print "<html><body><div id='res'>";
print encode_json $res;
print "</div></body></html>\n";

# eof
