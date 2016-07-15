# PckgChecker #
## Listing Perl modules added/removed to/from the system ##
----
__Languages used:__
* Perl // _as a server-side_
* JavaScript // _as a client-side_
* HTML
* CSS
* XML // _for transmitting data_

__Frameworks used:__
* Bootstrap 3
* jQuery

----
###Principles###
__On the server-side__

The application uses the Perl module "bla:bla" that gives us an easy way to list all the Perl modules currently availbale on the local machine.

__On the client-side__

The webpage uses AJAX method to fetch updated list of the Perl modules from the server-side and, adding some markup, shows it to a user. The webpage re-checks the data every second, but it can be modified at any time, using special settings-box in the page.

----

###The Docker###
The software is deitributed with the dockerfile. This meand that you can run the software in the container (aka VM but with lower system requirements and size than a usual VMs).

__There are below instructions of how to run:__

First we need to download (on fly) and build the image
`$ `
