Bien

Configurar las X para el ssh
https://community.oracle.com/thread/571326
https://www.cyberciti.biz/faq/how-to-fix-x11-forwarding-request-failed-on-channel-0/
https://unix.stackexchange.com/questions/131531/how-to-fix-xclock-command-not-found-error-on-oracle-linxu-6-4

vi /etc/ssh/sshd_config
   Set the following two options:
   X11Forwarding yes
   # si agrego la siguiente linea debo colocar en el /etc/hosts el nombre del servidor ejemplo como este
   # 127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4 srvoracle
   # si no la agrego automatcamente el DISPLAY apunta la localhost ejemplo
   # localhost:10.0
   X11UseLocalhost no 

/etc/init.d/sshd reload

La variable DISPLAY sera controlada y administrada por el ssh, no es necesario configurarla

yum install xauth # Este debe estar instalado porque si

Esto es opcional

yum install xorg-x11-server-utils

yum install xorg-x11-apps.x86_64 # esto es solo para optener el xclock

xhost +

# esta linea recuerda que hay un parametro en sshd_config #X11DisplayOffset 10, por eso que el ssh controla esta variale

export DISPLAY=localhost.localdomain:10.0

============================================================================================================
1.- https://geekflare.com/oracle-weblogic-installation-guide/

2.- https://docs.oracle.com/cd/E20593_01/doc.560/e23613/config_weblogic.htm

3.- https://help.adobe.com/en_US/enterpriseplatform/10.0/AdminHelp/WS92d06802c76abadb-5145d5d12905ce07e7-7c8f.html

4.- http://saltnlight5.blogspot.com/2014/08/deploying-applications-or-libraries-to.html

5.- http://narayanasetti.blogspot.com/2014/03/path-classpath.html

6.- https://docs.oracle.com/cd/E24329_01/web.1211/e24443/deploy.htm#DEPGD216

7.- https://docs.oracle.com/cd/E13222_01/wls/docs92/deployment/redeploy.html

Instalar weblogic

crear el dominio

desde el dominio iniciar weblogic

Levantar las variables

Ejecurtar despliegue




