print 'connecting to admin server....'
connect( 'weblogic', 'weblogic01', 't3://localhost:7021', adminServerName='AdminServer' )

print 'deploying....'
deploy('CONSIS', '/var/lib/docker/scm/EAR_Weblogic/7022/CONSIS.ear', targets='AdminServer')

startApplication('CONSIS')

print 'disconnecting from admin server....'
disconnect()

exit()
