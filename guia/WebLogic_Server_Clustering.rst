WebLogic Server Clustering
==============================

https://docs.oracle.com/cd/E11035_01/wls100/cluster/overview.html


¿Qué es un clúster de servidores WebLogic?
+++++++++++++++++++++++++++++++++++++++++++++++

Un clúster de WebLogic Server consta de varias instancias de servidor de WebLogic Server que se ejecutan simultáneamente y trabajan juntas para proporcionar una mayor escalabilidad y confiabilidad. Un clúster parece ser una única instancia de WebLogic Server para los clientes. Las instancias de servidor que constituyen un clúster pueden ejecutarse en la misma máquina o ubicarse en máquinas diferentes. Puede aumentar la capacidad de un clúster agregando instancias de servidor adicionales al clúster en una máquina existente, o puede agregar máquinas al clúster para hospedar las instancias de servidor incrementales. Cada instancia de servidor en un clúster debe ejecutar la misma versión de WebLogic Server.


¿Cómo se relaciona un clúster con un dominio?
+++++++++++++++++++++++++++++++++++++++++++++++

Un clúster es parte de un dominio particular de WebLogic Server.

Un dominio es un conjunto interrelacionado de recursos de WebLogic Server que se administran como una unidad. Un dominio incluye una o más instancias de WebLogic Server, que pueden ser agrupadas, no agrupadas o una combinación de instancias agrupadas y no agrupadas. Un dominio puede incluir múltiples clusters. Un dominio también contiene los componentes de la aplicación implementados en el dominio, y los recursos y servicios requeridos por esos componentes de la aplicación y las instancias del servidor en el dominio. Los ejemplos de los recursos y servicios utilizados por las aplicaciones y las instancias de servidor incluyen definiciones de máquinas, canales de red opcionales, conectores y clases de inicio.

Puede usar una variedad de criterios para organizar las instancias de WebLogic Server en dominios. Por ejemplo, puede elegir asignar recursos a múltiples dominios según las divisiones lógicas de la aplicación alojada, las consideraciones geográficas o el número o la complejidad de los recursos bajo administración. Para obtener información adicional acerca de los dominios, consulte Descripción de la configuración del dominio.

En cada dominio, una instancia de WebLogic Server actúa como el Servidor de administración, la instancia del servidor que configura, administra y supervisa todas las demás instancias y recursos del servidor en el dominio. Cada Servidor de Administración administra un solo dominio. Si un dominio contiene varios clústeres, cada clúster del dominio tiene el mismo Servidor de administración.

Todas las instancias de servidor en un clúster deben residir en el mismo dominio; no se puede "dividir" un clúster en varios dominios. Del mismo modo, no puede compartir un recurso o subsistema configurado entre dominios. Por ejemplo, si crea un grupo de conexión JDBC en un dominio, no puede usarlo con una instancia de servidor o un clúster en otro dominio. (En su lugar, debe crear un grupo de conexión similar en el segundo dominio).

Las instancias de WebLogic Server agrupadas se comportan de forma similar a las instancias no agrupadas, excepto que proporcionan conmutación por error y equilibrio de carga. El proceso y las herramientas utilizadas para configurar las instancias de WebLogic Server agrupadas son los mismos que los utilizados para configurar las instancias no agrupadas. Sin embargo, para lograr los beneficios de equilibrio de carga y conmutación por error que permite la agrupación en clústeres, debe cumplir con ciertas pautas para la configuración del clúster.

Para comprender cómo se relacionan los mecanismos de conmutación por error y equilibrio de carga utilizados en WebLogic Server con las opciones de configuración particulares, consulte Equilibrio de carga en un clúster, y Migración por error y replicación en un clúster.

Se incluyen recomendaciones de configuración detalladas a lo largo de las instrucciones en Configuración de clusters de WebLogic.
