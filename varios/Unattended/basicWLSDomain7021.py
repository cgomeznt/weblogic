

readTemplate("/u01/app/oracle/middleware/wlserver/common/templates/wls/wls.jar")


cd('Servers/AdminServer')
set('ListenAddress','')
set('ListenPort', 7021)


cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword('weblogic01')


cd('/')
create('myDataSource', 'JDBCSystemResource')
cd('JDBCSystemResource/myDataSource/JdbcResource/myDataSource')
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName','org.apache.derby.jdbc.ClientDriver')
set('URL','jdbc:derby://localhost:1527/db;create=true')
set('PasswordEncrypted', 'PBPUBLIC')
set('UseXADataSourceInterface', 'false')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
create('user', 'Property')
cd('Property/user')
cmo.setValue('PBPUBLIC')

cd('/JDBCSystemResource/myDataSource/JdbcResource/myDataSource')
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String("myDataSource_jndi"))

cd('/JDBCSystemResource/myDataSource/JdbcResource/myDataSource')
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName','SYSTABLES')


cd('/')
assign('JDBCSystemResource', 'myDataSource', 'Target', 'AdminServer')


setOption('OverwriteDomain', 'true')
writeDomain('/u01/app/oracle/middleware/user_projects/domains/D7021')
closeTemplate()


exit()
