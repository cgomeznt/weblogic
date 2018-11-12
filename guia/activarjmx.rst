Activar el JMX remote
======================


Agregar estas lineas en el archivo  **setDomainEnv.sh ** en la ruta "$WLS_HOME/bin" ::

	# Monitoring JMX
	JAVA_OPTIONS="$JAVA_OPTIONS -Djava.rmi.server.hostname=192.168.1.11"
	JAVA_OPTIONS="$JAVA_OPTIONS -Dcom.sun.management.jmxremote"
	JAVA_OPTIONS="$JAVA_OPTIONS -Dcom.sun.management.jmxremote.port=6065"
	JAVA_OPTIONS="$JAVA_OPTIONS -Dcom.sun.management.jmxremote.ssl=false"
	JAVA_OPTIONS="$JAVA_OPTIONS -Dcom.sun.management.jmxremote.authenticate=false"
	export JAVA_OPTIONS


Ahora para hacer las pruebas utilizamos el cliente **cmdline-jmxclient-0.10.3.jar** de la siguiente forma::

	$ java -jar /home/cgomez/Documentos/app/jmxclient/cmdline-jmxclient-0.10.3.jar - localhost:6065 java.lang:type=Memory HeapMemoryUsage

	11/12/2018 11:38:44 -0400 org.archive.jmx.Client HeapMemoryUsage: 
	committed: 490209280
	init: 268435456
	max: 490209280
	used: 420348728

