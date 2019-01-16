Reset the AdminServer Password in WebLogic 11g and 12c
=======================================================

If you forget the AdminServer password for your WebLogic 11g domain, you can reset it from the command line using the following process.

Set up the following environment variables. They are not necessary for the process itself, but will help you navigate. In this case my domain is called "ClassicDomain". Remember to change the value to match your domain.::

	export MW_HOME=/u01/app/oracle/middleware
	export DOMAIN_HOME=$MW_HOME/user_projects/domains/ClassicDomain

Shut down the WebLogic domain.::

	$ $DOMAIN_HOME/bin/stopWebLogic.sh

Rename the data folder.::

	$ mv $DOMAIN_HOME/servers/AdminServer/data $DOMAIN_HOME/servers/AdminServer/data-old

Set the environment variables.::

	$ . $DOMAIN_HOME/bin/setDomainEnv.sh

Reset the password using the following command. Remember to substitute the appropriate username and password.::

	$ cd $DOMAIN_HOME/security
	$ java weblogic.security.utils.AdminAccount <username> <password> .

Update the "$DOMAIN_HOME/servers/AdminServer/security/boot.properties" file with the new username and password. The file format is shown below.::

	username=<username>
	password=<password>

Start the WebLogic domain.::

	$ $DOMAIN_HOME/bin/startWebLogic.sh
