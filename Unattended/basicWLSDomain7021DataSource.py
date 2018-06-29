

readTemplate("/u01/app/oracle/middleware/wlserver/common/templates/wls/wls.jar")


cd('Servers/AdminServer')
set('ListenAddress','')
set('ListenPort', 7021)


cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword('weblogic01')


print 'Create datasource Datasource-GS'
cd('/')
create('Datasource-GS', 'JDBCSystemResource')
cd('JDBCSystemResource/Datasource-GS/JdbcResource/Datasource-GS')
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName','oracle.jdbc.OracleDriver')
set('URL','jdbc:oracle:thin:@192.168.1.53:1521:orcl12c')
set('PasswordEncrypted', 'SCM_CRECERGU_V138')
set('UseXADataSourceInterface', 'false')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
create('user', 'Property')
cd('Property/user')
cmo.setValue('SCM_CRECERGU_V138')

cd('/JDBCSystemResource/Datasource-GS/JdbcResource/Datasource-GS')
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String("jdbc/Datasource-GS"))

cd('/JDBCSystemResource/Datasource-GS/JdbcResource/Datasource-GS')
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName','SYSTABLES')

cd('/')
assign('JDBCSystemResource', 'Datasource-GS', 'Target', 'AdminServer')

print 'Create datasource Datasource-PE'
cd('/')
create('Datasource-PE', 'JDBCSystemResource')
cd('JDBCSystemResource/Datasource-PE/JdbcResource/Datasource-PE')
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName','oracle.jdbc.OracleDriver')
set('URL','jdbc:oracle:thin:@192.168.1.53:1521:orcl12c')
set('PasswordEncrypted', 'SCM_CRECER_V138')
set('UseXADataSourceInterface', 'false')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
create('user', 'Property')
cd('Property/user')
cmo.setValue('SCM_CRECER_V138')

cd('/JDBCSystemResource/Datasource-PE/JdbcResource/Datasource-PE')
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String("jdbc/Datasource-PE"))

cd('/JDBCSystemResource/Datasource-PE/JdbcResource/Datasource-PE')
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName','SYSTABLES')


cd('/')
assign('JDBCSystemResource', 'Datasource-PE', 'Target', 'AdminServer')
setOption('OverwriteDomain', 'true')

print 'Creating Domain...!!!'
writeDomain('/u01/app/oracle/middleware/user_projects/domains/D7021')


closeTemplate()


exit()
