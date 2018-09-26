Como instalar parches, consultar y hacer rollback en Weblogic
============================================================
.::

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


Napply Command for OUI-based Oracle Homes
+++++++++++++++++++++++++++++++++++++++++++++


Examples

The following example applies all patches under the <patch_location> directory::

	opatch napply <patch_location>

The following example applies patches 1, 2, and 3 that are under the <patch_location> directory::

	opatch napply <patch_location> -id 1,2,3

The following example applies all patches under the <patch_location> directory. OPatch skips duplicate patches and subset patches (patches under <patch_location> that are subsets of patches installed in the Oracle home).::

	opatch napply <patch_location> -skip_subset -skip_duplicate


The following example applies patches 1, 2, and 3 that are under the <patch_location> directory. OPatch skips duplicate patches and subset patches (patches under <patch_location> that are subsets of patches installed in the Oracle home).::

	opatch napply <patch_location> -id 1,2,3 -skip_subset -skip_duplicate


This command applies interim patches to several Oracle homes at the same time.

