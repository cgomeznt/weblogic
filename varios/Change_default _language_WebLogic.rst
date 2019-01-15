
Change the default language of WebLogic Server
=====================================================

To change the language of the messages in the log files, perform the following steps:

Go to your domain root directory (MIDDLEWARE_HOME/user_projects/domains/MY_DOMAIN).
Open the file::

	bin/setDomainEnv 

Search for EXTRA_JAVA_PROPERTIES and add the following lines::

	# Linux
	EXTRA_JAVA_PROPERTIES="-Duser.language=en -Duser.country=US ${EXTRA_JAVA_PROPERTIES}"
	export EXTRA_JAVA_PROPERTIES


Ver este link que ya le dio el error ORA-01843: not a valid month por cambiar de java 5 a java 7

http://apuntesadeteran.blogspot.com/2016/04/sqlexception-ora-01843-al-migrar-java-7.html


