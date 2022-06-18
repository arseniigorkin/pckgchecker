#!/usr/bin/env perl
#######################
# App name: Paskage Checker "pckgchecker"
# Description: This application lists all the installed in the local host Perl modules
# and sends them as JSON to the frontend webpage to be further parsed with JS
# Author: Arsenii Gorkin <gorkin@protonmail.com>
#######################

use strict;
#use warnings;

use File::Find::Rule;
use CGI::Carp q(fatalsToBrowser);
use Cpanel::JSON::XS qw(encode_json);


	# find all the .pm files in @INC
	my $rule =  File::Find::Rule->new;
	$rule->file;
	$rule->name( '*.pm' );
	my @files = $rule->in( @INC );
	
	my $mod_prep = []; #this will be a temporary array_ref with all the results
	my %duplicates;
	
	#foreaching through a list of found modules
	foreach my $this (@files) {
		
		open(my $pf, "<", $this) or die "Could not open a file: $this";
		
		my $package;
		my $version;
		
		while(<$pf>) {
			
			if ($package eq '')  {
				
				#checking package name:
				($package) = $_ =~ /package[ ]*([\w::]*);/i;
			}
			elsif ($version eq '') {
				
				#checking package version:
				($version) = $_ =~ /\$VERSION[ ]*=[ ]*['"]?([\w*\.]*)['"]?;/i;
			}
			if ($package ne '' and $version ne '') {
				last;
			}
		} 
		
		close $pf;
		
		#preventing duplicates
		if ($duplicates{$package}) {
			next;
		}
		else {
			$duplicates{$package} = 1;
		}
		
		#storing results into the temp array_ref as a future JS object
		push @$mod_prep, {
			module		=> $package,
			version		=> $version,
			path		=> $this
		}
		
	}
	
	my $json = encode_json $mod_prep; #encoding all the data into JSON format

	print "Content-type:application/json\n\n";
	print $json;

=head1 NAME
pckgchecker - JSON modules checker using @INC records

=head1 DESCRIPTION
This is a simple web application, based on AJAX technology,
for showing online a list of all the installed Perl modules
on the local host.
This program has two parts:

=over 5

=item B<Frontend>
which is an .html file (with JS scripts),
that receives and parses lists of modules,
supplied in JSON format by the backend this Perl script,

=item B<Backend>
Perl script (actual), that fetches a list
of all the installed modules,
using @INC, and converts it into JSON format.
Then the result is sent to the frontend 

=back

=head2 Methods

The Perl script uses two modules for implementing the task:

=over 5

=item B<File::Find::Rule>
This is a very handy module for searching files on the machine.
It provides a very easy API for creating search queries "on fly"
and it can work with @INC,

=item B<Cpanel::JSON::XS>
This one gives me a really easy method for converting my data into JSON format.

=back

=head1 AUTHOR
Arsenii Gorkin I<< gorkin@protonmail.com >>

