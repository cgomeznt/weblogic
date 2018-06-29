FROM centos:7

MAINTAINER Carlos Gomez G cgomeznt@gmail.com

# Instalamos la base de la Imagen
ENV     container docker

RUN     yum -y update
RUN     yum -y install sudo \
        tar \
        gzip \
        openssh-clients \
        vi \
        find \
	net-tools
RUN	yum clean all

# Creamos el usuario valido para inicializar el Weblogic
RUN     groupadd oinstall
RUN     useradd -g oinstall oracle

# Creamos los directorios requeridos para copiar los archivos base y para dejar las configuraciones
RUN	mkdir -p /u01/software
RUN	mkdir -p /u01/app/oracle/middleware
RUN	mkdir -p /u01/app/oracle/config/domains
RUN	mkdir -p /u01/app/oracle/config/applications
RUN	chown -R oracle:oinstall /u01
RUN	chmod -R 775 /u01/

# Creamos las variables para el Weblogic
ENV	export MW_HOME=/u01/app/oracle/middleware
ENV	export WLS_HOME=$MW_HOME/wlserver
ENV	export WL_HOME=$WLS_HOME

# Creamos la variable del JAVA_HOME y lo colocamos en el PATH
ENV	export JAVA_HOME=/u01/app/oracle/jdk1.8.0_77
ENV	export PATH=$JAVA_HOME/bin:$PATH

# Copiamos la version del JAVA y lo instalamos
COPY	jdk-8u101-linux-x64.rpm	/u01/software
RUN	rpm -ivh /u01/software/jdk-8u101-linux-x64.rpm

# Copiamos los archivos base para dentro de la imagen.
COPY	wls.rsp /u01/software
COPY	oraInst.loc /u01/software
COPY	UpdatePortal.sh /u01/software
COPY	deploy.py /u01/software
COPY	basicWLSDomain7021DataSource.py /u01/software
COPY 	fmw_12.2.1.3.0_wls.jar /u01/software

# WLS
#RUN 	su oracle -c "$JAVA_HOME/bin/java -Xmx512m -jar /u01/software/fmw_12.2.1.3.0_wls_quick.jar -silent -responseFile /u01/software/wls.rsp -invPtrLoc /u01/software/orainst.loc" 

USER	oracle
RUN 	$JAVA_HOME/bin/java -Xmx1024m -jar /u01/software/fmw_12.2.1.3.0_wls.jar -silent -responseFile /u01/software/wls.rsp -invPtrLoc /u01/software/oraInst.loc 

RUN	source /u01/app/oracle/middleware/wlserver/server/bin/setWLSEnv.sh  && \
	$JAVA_HOME/bin/java weblogic.WLST /u01/software/basicWLSDomain7021DataSource.py     


EXPOSE	7021

#Lanzar WebLogic
#RUN	/u01/app/oracle/middleware/user_projects/domains/D7021/bin/startWebLogic.sh
CMD ["/u01/app/oracle/middleware/user_projects/domains/D7021/bin/startWebLogic.sh"]

