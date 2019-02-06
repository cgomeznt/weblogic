
Como trabaja un weblogic clustering?
++++++++++++++++++++++++++++++++++++++
• un clúster contiene uno o más servidores lógicos que pueden residir en uno o varios servidores físicos?
• al implementar una aplicación j2ee en un clúster, está vinculada a un servidor en ese clúster?
• los usuarios externos de la aplicación implementada no son conscientes de la agrupación en clústeres?
• el archivo de registro de esa aplicación se encuentra en el servidor que está implementado?
• ¿Si el servidor que aloja la aplicación falla, está bien porque la aplicación está en un clúster y otro servidor retomará el trabajo?
• Si el servidor que aloja la aplicación falla, ¿qué sucede con el registro?


Creo que deberías entender el concepto de dominio primero.

El dominio es el padre de un clúster. Normalmente contiene un administrador y uno o más servidores administrados. Ahora el Cluster es una agrupación de algunos o todos estos servidores administrados dentro del dominio.

Espero que el diagrama aquí ayude a la comprensión.

https://docs.oracle.com/cd/E13222_01/wls/docs90/domain_config/understand_domains.html#1101988


Una vez que configure usted mismo un dominio y un clúster en un entorno de desarrollo, podrá conocer más sobre él.

Ahora aquí están las respuestas a sus preguntas específicas

• un clúster contiene uno o más servidores lógicos que pueden residir en uno o varios servidores físicos

Cierto. Pero aclaremos lo que quiere decir con servidores "lógicos". En el Clúster normalmente tiene dos o más servidores administrados. Estos servidores se ejecutan en sus propias JVM y se pueden iniciar de forma independiente y atender las solicitudes de forma independiente. Cada servidor tendrá una dirección IP: puerto única, y se puede acceder directamente desde el navegador. Pero estas instancias de servidor pueden residir sobre múltiples servidores físicos.

• al implementar una aplicación j2ee en un clúster, está vinculada a un servidor en ese clúster

No, no está vinculado a un servidor. Cuando implementa una aplicación J2EE en el clúster, se implementará en cada servidor de ese clúster. El JNDI es para todo el clúster y cada servidor mantiene una copia local del JNDI.

Puede buscar el objeto (por ejemplo, un EJB) a través de JNDI en el Clúster o en el servidor individual. También vea qué tipos de objetos se pueden agrupar.

• los usuarios externos de la aplicación implementada no son conscientes de la agrupación en clústeres

Cierto.

Pero en este caso, debe tener un servidor web Apache o un equilibrador de carga o un servidor DNS que tome la solicitud del navegador y la asigne internamente a uno de los servidores del clúster. Si no tiene ninguno de estos, tendría que definir la dirección del clúster como un nombre DNS o una dirección IP para el cliente. Consulte la sección "Evitar problemas de escucha de direcciones" en http://download.oracle.com/docs/cd/E13222_01/wls/docs103/cluster/setup.html#wp682940

• el archivo de registro de esa aplicación se encuentra en el servidor que está implementado

Es cierto, un registro weblogic por servidor.

• ¿Si el servidor que aloja la aplicación falla, está bien porque la aplicación está en un clúster y otro servidor retomará el trabajo?

No de forma predeterminada, tiene que configurarlo para la conmutación por error y la replicación. Este es un gran tema que necesita lectura separada

• Si el servidor que aloja la aplicación falla, ¿qué sucede con el registro?

Se detiene el registro. Verá algunos errores de apagado o de latido en el registro, o fuera de la memoria o por cualquier motivo de error. Tendrá que reiniciar el servidor, y el registro continuará en un nuevo archivo (según la configuración de registro)
