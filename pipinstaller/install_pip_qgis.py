from PyQt4.QtCore import QProcess
import os, sys
class Pip_installation_process:
	
	
	IS_WIN32 = ""
	def __init__(self):
		self.IS_WIN32='win32' in str(sys.platform).lower()

	def run_installer(self, package_name):

		self.package_name = package_name

		if os.name == 'posix':
			home = os.environ['HOME']
		elif os.name == 'nt':
			home = os.environ['HOMEPATH']

##		pip_rel_path = os.path.join(os.sep,'.qgis2', 'python', 'plugins','pipinstaller','pip-1.5.4')
##		pip_path = ('%s%s') % (home,pip_rel_path)
##		try:
##			import pip
##		except:
##			try:
##				subprocess.call('C:\\PROGRA~2\\QGISDU~1\\Osgeo4W.bat python ez_setup.py install')
##			except Exception, e:
##				print str(e)
##			try:
##				subprocess.call('C:\\PROGRA~2\\QGISDU~1\\Osgeo4W.bat python setup.py install')
##			except Exception, e:
##				print str(e)

		package_to_install = "reportlab"
		cmd = 'C:\\PROGRA~2\\QGISDU~1\\Osgeo4W.bat pip install sqlalchemy'
		qprocess = QProcess()
		p = qprocess.start(cmd)

		return p


	def subprocess_call(self,*args, **kwargs):
		#also works for Popen. It creates a new *hidden* window, so it will work in frozen apps (.exe).
		if self.IS_WIN32:
			startupinfo = subprocess.STARTUPINFO()
			startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
			startupinfo.wShowWindow = subprocess.SW_HIDE
			kwargs['startupinfo'] = startupinfo
		retcode = subprocess.call(*args, **kwargs)
		return retcode


##		try:
	#subprocess.call('C:\\PROGRA~2\\QGISDU~1\\Osgeo4W.bat pip install sqlalchemy') # % (package_name)
##		except:
##			pass