Description: add setup.py
 Integration of setuptools to allow easier building with dh_python
 .
 acmebot (2.6.0-1) unstable; urgency=medium
 .
   * Initial release. (Closes: #930094)
Author: Hinrikus Wolf <mail@hinrikus-wolf.de>
Bug-Debian: https://bugs.debian.org/930094

---
The information above should follow the Patch Tagging Guidelines, please
checkout http://dep.debian.net/deps/dep3/ to learn about the format. Here
are templates for supplementary fields that you might want to add:

Origin: <vendor|upstream|other>, <url of original patch>
Bug: <url in upstream bugtracker>
Bug-Debian: https://bugs.debian.org/<bugnumber>
Bug-Ubuntu: https://launchpad.net/bugs/<bugnumber>
Forwarded: <no|not-needed|url proving that it has been forwarded>
Reviewed-By: <name and email of someone who approved the patch>
Last-Update: 2019-07-24

--- /dev/null
+++ acmebot-2.6.0/setup.py
@@ -0,0 +1,7 @@
+from setuptools import setup, find_packages
+setup(
+    name="acmebot",
+    version="2.6.0",
+    scripts=['acmebot']
+    )
+
