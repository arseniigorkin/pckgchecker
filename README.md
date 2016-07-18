# PckgChecker #
## Listing Perl modules added/removed to/from the system ##
----
###Description###
This is a web-software that lists all the present in the local host Perl modules, using AJAX. This is an easy-to-use webpage that has only one mission: to show in a real time Perl modules installed in the system.

But this webpage can trace modules even after their deletion. You can see just deleted modules as "deleted" one more minute after they have been wiped.

The application provides the user with a list of all the modules in the alphabetical order. Each module is presented with its name and its version.

__Languages used:__
* Perl // _as a server-side_
* JavaScript // _as a client-side_
* HTML
* CSS
* JSON // _for transmitting data_

__Frameworks used:__
* Bootstrap 3
* jQuery
* File::Find::Rule
* Cpanel::JSON::XS

__What I have done__
* Developed the two-side web-software: server-side is based on Perl script and the client-side is based on JavaScript. 
* Built a dockerfile that builds Ubuntu (last ver.) with fully configured __Apache2__ and __cpanminus__ on board. To start a new container you just need to call an image (without any parameters and arguments, like: perl myapp.pl etc..). This is a very comfort build that gives me all the power of Apache2 server. Using this biuld you feel like if you work on the full machine with a full server.

----
###Principles###
This program has two parts:

* __"Frontend"__
which is an .html file (with JS scripts),that receives and parses lists of modules,supplied in JSON format by the backend this Perl script,

* __"Backend"__
Perl script (actual), that fetches a list of all the installed modules every 5, 10 or 15 seconds (depending on the user's settings), using `@INC`, and converts it into JSON format. Then the result is sent to the frontend 

__Methods__

The Perl script uses two modules for implementing the task:

* __"File::Find::Rule"__
This is a very handy module for searching files on the machine. It provides a very easy API for creating search queries "on fly" and it can work with `@INC`,

* __Cpanel::JSON::XS"__
This one gives me a really easy method for converting my data into JSON format.

----

![picture alt](https://github.com/arseniigorkin/pckgchecker/blob/master/docker.png?raw=true "Dockerfile")

###The Docker###
The software is deitributed with the dockerfile. This meand that you can run the software in the container (aka VM but with lower system requirements and size than a usual VMs).

__There are below instructions of how to run:__

1. First we need to build (and download on fly) the image: `$ sudo docker build -t ag/pckgchecker https://github.com/arseniigorkin/pckgchecker.git`. You can replace `ag/pckgchecker` with any name you like for this image.
2. Run new container: `$ sudo docker run -it --rm -p 9191:80 ag/pckgchecker`. You can change the port `9191` to any you like for outuping the program to your localhost. 
3. Open a browser and type: `http://localhost:9191` (please, note: the server is NOT configured for SSL now).
4. Once you finished working with the app you need to terminate the container. Just type in the terminal (with running container) `CTRL+C`.

----

###Interface###
Once you open a page `http://localhost:9191` you may see loading image (until the list will come to the browser in full).
When the page is loaded you see a list of installed modules. and a settings (in the right bottom corner right under the list) for update interval (3 optwions: 5, 10 and 15 secs).

__Installed__ modules are shown with color icon (in the left of the row) and a green "play" icon on the right.

__Just added modules__ will have a label "NEW" next to their names and it will last for 30 seconds from the time of installation.

__Just deleted modules__ will be shown in greyscale colours (b/w icon on the left) and with red cross on the right.

Deleted modules will appear in the list for the next minute.

If you click on _"Information"_ button next to each module, you will see a DEMO information. It has a link to the module's page in the CPAN website and a version number.

Also: if the module is active its icon in this dialogue will be colour, if delete - greyscale.

As I said the build of the Docker includes cpanminus. It means, that you can easily install and uninstall any modules from the host.

__To install the module__ use your open Terminal (which works with the container with the software now) and type: `$ sudo cpanm Module::Name`. That's it! 

__To uninstall the module__ just type in the Terminal (also where the container with this software is active now) and type: `$ sudo cpanm --uninstall Module::Name`. You will need to confirm the deletion.

__To find just installed/uninstalled__ modules on the screen (in the webpage) just use oldschool `ctrl+f` and type there the name of the module you are looking for.

###NB###
As I have never worked with any containers like Docker (or any else) and never saw them in the action, so this is my first try (dockerfile). I spent 2 days for understanding the idea and preparing the dockerfile that I supply in this repository.

Also I could create the program using a regular "refresh" method for auto reloading the same page, which could be then fully written on Perl. But it would be too easy and not in the modern way)). Thus I created this mutiful Bootstrap page with AJAX for your comfort. I hope you will enjoy it!

Thank you.

__Author__: _Arsenii Gorkin_
![picture alt](https://github.com/arseniigorkin/pckgchecker/blob/master/perl.png?raw=true "Perl demo program")
