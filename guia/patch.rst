Como instalar parches, consultar y hacer rollback en Weblogic
============================================================

	ORACLE_HOME

	java -version

	/u01/Middleware/12.1.2/OPatch

	./opatch lsinventory

	cd ..

	cd downloaded_patches/

	/u01/Middleware/12.1.2/downloaded_patches/

	ls
	p17662264_121200_Generic.zip

	unzip -d PATCHTOP p17662264_121200_Generic.zip

	cd PATCHTOP

	cd 17662264


	/u01/Middleware/12.1.2/OPatch/opatch apply

	appied

	/u01/Middleware/12.1.2/OPatch/opatch lsinventory

	ver log

	/u01/Middleware/12.1.2/OPatch/opatch rollback -id 17662264

	/u01/Middleware/12.1.2/OPatch/opatch lsinventory


