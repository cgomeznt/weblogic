Activación de Puerto Debug Weblogic
=====================================

Ubicarse el “bin” del Dominio al cual se desea activar el puerto::

	cd /u02/app/oracle/domain/D7035/bin

Editar el setDomainEnv::

	vi setDomainEnv.sh

Ubicar “if [ "${DEBUG_PORT}" = ""….” Para asignar el puerto deseado ::


	if [ "${DEBUG_PORT}" = "" ] ; then

		DEBUG_PORT="9035"

		export DEBUG_PORT

	fi

Luego  ubicar el “debugFlag” y colocarlo en true para activar o false para desactivar.::

	debugFlag="true"

	export debugFlag



