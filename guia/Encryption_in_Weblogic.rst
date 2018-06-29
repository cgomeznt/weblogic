Encryption in Weblogic:

1. Set the environment
cd [domain_home]/bin
./setDomainEnv.sh
2.Encrypt the password using the below command.

java weblogic.security.Encrypt <password>

e.g., java weblogic.security.Encrypt weblogic123

{AES}xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

The above encrypted value can used in place of the password weblogic123 in all the necessary configuration files.

Decryption:

To recover the encrypted username and password:

1. Create a script decrypt.py under [domain_home]/security with the below:

from weblogic.security.internal import *
from weblogic.security.internal.encryption import *
encryptionService = SerializedSystemIni.getEncryptionService(“.”)
clearOrEncryptService = ClearOrEncryptedService(encryptionService)
# Take encrypt password from user
pwd = raw_input(“Paste encrypted password ({AES}fk9EK…): “)
# Delete unnecessary escape characters
preppwd = pwd.replace(“\\”, “”)
# Display password
print “Decrypted string is: ” + clearOrEncryptService.decrypt(preppwd)

2.Get the encrypted username/password which needs to be recovered.

grep username $DOMAIN_HOME/servers/AdminServer/security/boot.properties | sed -e “s/^username=\(.*\)/\1/”

grep password $DOMAIN_HOME/servers/AdminServer/security/boot.properties | sed -e “s/^password=\(.*\)/\1/”
3.Set the environment variables.

cd [domain_home]/bin
./setDomainEnv.sh
4.Execute the decrypt.py script to recover the encrypted text.
cd [domain_home]/security
java weblogic.WLST decrypt.py
[KENANFX1]/apps/bss/retail1.1/wls_10/security> java weblogic.WLST decrypt_password.py
Initializing WebLogic Scripting Tool (WLST) …

Welcome to WebLogic Server Administration Scripting Shell

Type help() for help on available commands

Paste encrypted password ({AES}fk9EK…): {AES}86n6O6xZvG3ucxGCxf4CMLQJBJqNVIPwKaMbtsWf8TM=
Decrypted string is: admin1
