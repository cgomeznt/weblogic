Monitoring with jconsole Weblogic
==================================

::

	service:jmx:iiop://192.168.0.4:7044/jndi/weblogic.management.mbeanservers.runtime

::

	/u02/app/product/jdk1.7.0_79/bin/jconsole -J-Djava.class.path=/u02/app/product/jdk1.7.0_79/lib/jconsole.jar:/u02/app/product/jdk1.7.0_79/lib/tools.jar:/u02/app/product/W_12c/wlserver/server/lib/wljmxclient.jar -J-Djmx.remote.protocol.provider.pkgs=weblogic.management.remote -debug

	connect('weblogic','weblogic01','t3://srvscm02:8010')

	find('DebugEjbCaching') 

	HeapSizeMax 		- 	MaxHeapSize
	HeapSizeCurrent 	- 	Commited
	HeapFreeCurrent		-	FreeMemory: Commited menos Used

	HeapSizeCurrent menos HeapFreeCurrent = Used

	HeapFreeCurrent: Freememory
	HeapSizeCurrent: Committed
	HeapSizeMax: MaxHeapSize



