Crear un Datasource
===================

Lo primero que debemos hacer es descargar el driver **mssql-jdbc-7.0.0.jre8.jar**

Ese driver lo copiamos en el "/u06/app/product/wls12213/wlserver/server/lib/"

Luego debemos editar el **setDomainEnv.sh** y agregarlo en el **CLASSPATH** ::


	CLASSPATH="${CLASSPATH}:/u06/app/product/wls12213/wlserver/server/lib/mssql-jdbc-7.0.0.jre8.jar"

.. figure:: ../images/53.png


Ingresamos a la consola del Weblogic.:

.. figure:: ../images/13.png


Nos vamos a Orígenes de Datos

.. figure:: ../images/14.png

Le damos a Nuevo y seleccionamos Origen de Datos Generico

.. figure:: ../images/15.png


Colocamos nombre desea asignar al nuevo origen de datos JDBC y el nombre JNDI

.. figure:: ../images/16.png

.. figure:: ../images/45.png


Hacemos seleccion del Driver.

.. figure:: ../images/46.png


Dejamos esto igual.

.. figure:: ../images/47.png


Debemos tener a la mano todos los datos de la BD.

.. figure:: ../images/48.png


Confirma que todos los datos esten bien.

.. figure:: ../images/49.png



Seleccionamos los Destinos en que se desplegara los Datasource.

.. figure:: ../images/51.png


Y finiquitamos con exito.

.. figure:: ../images/52.png


