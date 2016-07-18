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

__What I have done__
* Built a dockerfile that builds Ubuntu (last ver.) with fully configured __Apache2__ and __cpanminus__ on board. To start a new container you just need to call an image (without any parameters and arguments, like: perl myapp.pl etc..). This is a very comfort build that gives me all the power of Apache2 server. Using this biuld you feel like if you work on the full machine with a full server.
* developed a software itself.

----
###Principles###
__On the server-side__

The application uses the Perl module "bla:bla" that gives us an easy way to list all the Perl modules currently availbale on the local machine.

__On the client-side__

The webpage uses AJAX method to fetch updated list of the Perl modules from the server-side and, adding some markup, shows it to a user. The webpage re-checks the data every second, but it can be modified at any time, using special settings-box in the page.

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

__Interface__
Once you open a page `http://localhost:9191` you may see loading image (until the list will come to the browser in full).
When the page is loaded you see a list of installed modules. and a settings (in the right bottom corner right under the list) for update interval (3 optwions: 5, 10 and 15 secs).
Installed modules are shown with color icon (in the left of the row) and a green "play" icon on the right.
Just added modules will have a label "NEW" next to their names and it will last for 30 seconds from the time of installation.
Just deleted modules will be shown in greyscale colours (b/w icon on the left) and with red cross on the right.
Deleted modules will appear in the list for the next minute.
If you click on "Information" you will see a DEMO of how the information. It has a link to the module's page in the CPAN website and a version number.
Also: if the module is active its icon in this dialogue will be colour, if delete - greyscale.

###NB###
As I have never worked with any containers like Docker, this is my first try (dockerfile). I spent 2 days for understanding the idea and preparing the dockerfile that I supply in this repository.

__Author__: _Arsenii Gorkin_
![picture alt](https://github.com/arseniigorkin/pckgchecker/blob/master/perl.png?raw=true "Perl demo program")
