pipinstaller-qgis-experimental - only windows 7 tested
=======================================================
PLEASE README before install!!!

A simple pipinstaller plugin for Qgis 2. Experimental. Use at your own risk.

Tested only on Windows 7 with Administrator permission. It can create problems on your own python packages modules installations. Please use it "cum grano salis".

To try to install put the pipinstaller folder into your own C:/users/your_user/.qgis2/python/plugins/

Require to restart two times Qgis.

If setuptools it's just present on your QGis distribution, probably doesn't run properly.

You can test if setuptools is present opening QGis 2 and calling on python console:
import easy_install

If you don't have ImportError: No module named easy_install you can try at your own risk to use it.
