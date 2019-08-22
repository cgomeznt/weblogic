wlst script example to start, stop and run as service
==========================================================

Below are the wlst script example which you can use in combination to make weblogic a service and automate the start/stop of Admin servers , managed servers and Node manager.

Create a folder at your server for ex: /opt/WLS/scripts/ where you will store all your scripts.

There are 5 scripts

MainWLS.sh : Script to manually start/stop all servers(including nodemanager). Can be used in /etc/init.d so that after system/machine reboot also the weblogic servers will comeup automatically.

Commands: MainWLS.sh start|stop::

	#! /bin/bash
	#
	# description: Oracle Weblogic auto start-stop script.

	# Source function library.
	. /etc/init.d/functions

	MW_HOME="/u01/app/oracle/middleware"
	DM_HOME="/u02/weblogic/user_projects/domains/base_domain"

	JAVA_OPTIONS="-Dweblogic.security.SSL.ignoreHostnameVerification=true"

	fileDate=`date '+%F_%H%M'`
	RETVAL=0
	start() {
	export MW_HOME DM_HOME JAVA_OPTIONS
	logFileName=nodemanager.log.$fileDate
	nohup $MW_HOME/wlserver_10.3/server/bin/startNodeManager.sh > $MW_HOME/logs/$logFileName &

	chown oracle:oinstall $MW_HOME/logs/$logFileName
	su oracle -c '/opt/WLS/scripts/startServers.sh'
	return $RETVAL
	}

	stop() {
	export MW_HOME DM_HOME JAVA_OPTIONS
	su oracle -c '/opt/WLS/scripts/stopServers.sh'
	return $RETVAL
	}
	case "$1" in
	start)
	start
	;;
	stop)
	stop
	;;
	*)
	echo $"Usage: $0 {start|stop}"
	exit 1
	esac

	exit $?

Above wlst script example can be used as a linux/*NIX service to start servers using “chkconfig –add servicename”
The above MainWLS.sh script refers 3 script files for starting servers.

startNodeManager.sh -> Provided by Oracle. ($MW_HOME/wlserver_10.3/server/bin/) -> Starts Nodemanager
startServers.sh -> We will create it in below section to start all servers including Admin and Managed.
stopServers.sh -> We will create it in below section to stop all servers including Admin and Managed.

Now we will create startServers.sh script to start all servers.(Admin and Managed)

startServers.sh::

	#Shell to start Admin Server First.
	export JAVA_OPTIONS="-Dweblogic.security.SSL.nojce=true\
	-Dweblogic.security.SSL.ignoreHostnameVerification=true"
	export PRE_CLASSPATH="${MW_HOME}/wlserver_10.3/server/lib/jsafeFIPS.jar"
	export USER_MEM_ARGS="-Xms1280m -Xmx1280m -XX:MaxPermSize=256M"
	export LOG_DIR="${MW_HOME}/logs"
	export WLS_REDIRECT_LOG=${LOG_DIR}/AdminServer.log
	#echo "Starting admin server"
	mv ${WLS_REDIRECT_LOG} ${WLS_REDIRECT_LOG}.`date +%F_%H%M`
	#
	# start the WLS admin server.
	#
	nohup $DM_HOME/startWebLogic.sh &
	#
	# once Admin Server is started, now we can start all the managed servers
	#
	echo `env` >> $MW_HOME/logs/startup.log
	source $DM_HOME/bin/setDomainEnv.sh
	#
	#Below startMS.py python script is used to start all the managed servers present in your domain(Ex: base_domain).
	#
	java weblogic.WLST /opt/WLS/scripts/startMS.py

Above script startServers.sh refers startMS.py python script to start all the managed servers.
Please find the python code for startMS.py

startMS.py::

	import time
	sleep=time.sleep
	configFile = "/home/cgomez/cgomez-WebLogicConfig.properties"
	pwFile = "/home/cgomez/cgomez-WebLogicKey.properties"
	while True:
	try:
	connect(userConfigFile=configFile,
	userKeyFile=pwFile,
	url='t3://192.168.1.105:7001')
	break
	except:
	sleep(60)
	nmConnect(userConfigFile=configFile,
	userKeyFile=pwFile,
	domainName='base_domain')
	nmStart('ManagedServer1')
	nmStart('ManagedServer2')
	exit()

you can see I have given configFile and Password file instead of username and password for better security.
You can also create you own secured/encrypted secure file using wlst.
Tips:

When you use this command with no arguments the user configuration file for the current user will be generated within the current OS user’s home folder.::

	wls:/testdomain/serverConfig>storeUserConfig()

All above scripts were for starting Adminserver, Nodemanager and Managed servers.

Now we will see the stop part scripts for AdminServer, managed servers.
stopServers.sh -> Referenced in MainWLS.sh::

	cd /opt/WLS
	source $DM_HOME/bin/setDomainEnv.sh
	java weblogic.WLST /opt/WLS/scripts/stopMS.py
	exit

stopMS.py -> Python script to stop Managed servers, Admin server and Nodemanager::

	configFile = "/home/cgomez/cgomez-WebLogicConfig.properties"
	pwFile = "/home/cgomez/cgomez-WebLogicKey.properties"
	connect(userConfigFile=configFile,
	userKeyFile=pwFile,
	url='t3://my.AdminServer.com:7001')
	nmConnect(userConfigFile=configFile,
	userKeyFile=pwFile,
	domainName='base_domain')
	print " shutting down managed servers"
	shutdown('ManageServer1',force='true')
	print " ManageServer1 shutdown"
	shutdown('ManageServer2',force='true')
	print " ManageServer2 shutdown"
	print "Shutting down Admin Server"
	shutdown('AdminServer',force='true')
	print "Stopping node manager"
	stopNodeManager()
	exit()

