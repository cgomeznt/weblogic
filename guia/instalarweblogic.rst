Instalar Oracle Weblogic 12.2.1.3.0
====================================

Oracle WebLogic es un servidor de aplicaciones Java EE (J2EE) y también un servidor web HTTP, desarrollado por BEA Systems, posteriormente adquirida por Oracle Corporation. Se ejecuta en Unix, Linux, Microsoft Windows, y otras plataformas.

WebLogic puede utilizar Oracle, DB2, Microsoft SQL Server, y otras bases de datos que se ajusten al estándar JDBC. El servidor WebLogic es compatible con WS-Security y cumple con los estándares de J2EE 1.3 desde su versión 7 y con la J2EE 1.4 desde su versión 9 y Java EE para las versiones 9.2 y 10.x.

Descargamos Weblogic 12.2.1.3.0 desde: http://www.oracle.com/technetwork/middleware/weblogic/downloads/wls-main-097127.html
Supplemental Quick Installer (231 MB) http://download.oracle.com/otn/nt/middleware/12c/12213/fmw_12.2.1.3.0_wls_supplemental_quick_Disk1_1of1.zip

Creamos un usuario para ejecutar la instalacion.::

	# groupadd install
	# useradd oracle -g install
	# passwd oracle
	Cambiando la contraseña del usuario oracle.
	Nueva contraseña: 
	Vuelva a escribir la nueva contraseña: 
	passwd: todos los tokens de autenticación se actualizaron exitosamente.

Debemos configurar el sshd para que se pueda hacer X11 forward, motivado que vamos a requerir las X para esta instalacion.::

	# vi /etc/ssh/sshd_config
	     X11Forwarding yes

Instalamos el paquete xauth.::

	# yum install xauth xorg-x11-apps

Ingresamos nuevamente al servidor con la opcion -X.::

	$ ssh -X oracle@192.168.56.10
	oracle@192.168.56.10's password: 
	[oracle@srvoracle ~]$ 

Probamos que las X11 esten haciendo el forward, ejecutamos el xclock y debemos visuailizar esta utilidad grafica.::

	$ echo $DISPLAY
	localhost:10.0

	$ xclock

Creamos la estructura de directorios para almacenar los paquetes e instalarlos.::

	# mkdir -p /u02/app/oracle
	# mkdir -p /u02/product
	# mkdir -p /u02/EAR
	# chown -R oracle.install /opt/IBM/

Instalamos el JDK de java.::

	# rpm -ivh /u02/product/jdk-8u101-linux-x64.rpm 
	Preparando...               ########################################### [100%]
		el paquete jdk1.8.0_101-2000:1.8.0_101-fcs.x86_64 ya está instalado

	# java -version
	java version "1.8.0_101"
	Java(TM) SE Runtime Environment (build 1.8.0_101-b13)
	Java HotSpot(TM) 64-Bit Server VM (build 25.101-b13, mixed mode)


Copiamos el paquete en el directorio de product y lo descomprimimos.::

	$ ls
	fmw_12.2.1.3.0_wls_quick_Disk1_1of1.zip

	$ unzip fmw_12.2.1.3.0_wls_quick_Disk1_1of1.zip 
	Archive:  fmw_12.2.1.3.0_wls_quick_Disk1_1of1.zip
	  inflating: fmw_12.2.1.3.0_wls_quick.jar  
	  inflating: README.txt              
	  inflating: fmw_12213_readme.htm  

Instalamos el Oracle Weblogic 12.2.1.3.0.::

	$ java -jar fmw_12.2.1.3.0_wls_quick.jar
		El archivo log del iniciador es /tmp/OraInstall2017-12-29_07-51-33PM/launcher2017-12-29_07-51-33PM.log.
		Extrayendo instalador... . Listo
		Comprobando si la velocidad de CPU es superior a 300 MHz.   3191.998 MHz reales    Correcto
		Comprobando el espacio de intercambio: debe ser mayor que 512 MB.   1227 MB reales    Correcto
		Comprobando si esta plataforma necesita una JVM de 64 bits.   64 reales    Correcto (no son necesarios 64 bits)
		Comprobando el espacio temporal: debe ser mayor que 300 MB.   5267 MB reales    Correcto
		Preparando para iniciar Oracle Universal Installer desde /tmp/OraInstall2017-12-29_07-51-33PM
		Log: /tmp/OraInstall2017-12-29_07-51-33PM/install2017-12-29_07-51-33PM.log

		*****************************************************


		Nombre de Distribución: Oracle Fusion Middleware 12c WebLogic y Desarrollador de Coherence
		Versión de Distribución: 12.2.1.3.0

		Inventario de Oracle: /home/oracle/oraInventory

		Directorio Raíz de Oracle:  /u02/product/wls12213
		Directorio Raíz de Java: /usr/java/jdk1.8.0_101

		Nota: No se ha proporcionado el directorio raíz de Oracle (el valor por defecto será el <directorio de trabajo actual>/wls12213)

		*****************************************************

		Copyright (c) 1996, 2017, Oracle y/o sus filiales. Todos los derechos reservados.
		Omitiendo Actualizaciones de Software
		Iniciando Comprobación: CertifiedVersions
		Resultado esperado: Uno de oracle-6, oracle-7, redhat-7, redhat-6, SuSE-11, SuSE-12
		Resultado real: oracle-6.7
		Comprobación terminada. El resultado general de esta comprobación es: Correcto
		Comprobación de CertifiedVersions: Correcta.


		Iniciando Comprobación: CheckJDKVersion
		Problema: Esta versión de JDK no se certificó en el momento en que se hizo disponible de forma general. Puede que se haya certificado teniendo en cuenta la disponibilidad general.

		Recomendación: Consulte Supported System Configurations Guide (http://www.oracle.com/technetwork/middleware/ias/downloads/fusion-certification-100350.html) para obtener más información. Pulse "Siguiente" si desea continuar.

		Resultado esperado: 1.8.0_131
		Resultado real: 1.8.0_101
		Advertencia: Comprobación:CheckJDKVersion terminada con advertencias.


		Las validaciones están activadas para esta sesión.
		Verificando datos
		Copiando Archivos
		Porcentaje Terminado: 10
		Porcentaje Terminado: 20
		Porcentaje Terminado: 30
		Porcentaje Terminado: 40
		Porcentaje Terminado: 50
		Porcentaje Terminado: 60
		Porcentaje Terminado: 70
		Porcentaje Terminado: 80
		Porcentaje Terminado: 90
		Porcentaje Terminado: 100

		instalación de Oracle Fusion Middleware 12c WebLogic y Desarrollador de Coherence 12.2.1.3.0 ha terminado correctamente.
		Los logs se han copiado correctamente en /u02/product/wls12213/cfgtoollogs/oui.

Esto no es necesario, pero al que le guste colocar otro nombre al directorio principal.::

	$ mv wls12213 Wl_12213
	$ mv wls12213 Wl_12213
	$ for i in `grep -r wls12213 Wl_12213 > files.txt` ; do sed -i -e 's/wls12213/Wl_12213/g'$i ; done

Ya con esto culminamos la configuracion de Weblogic.

	


