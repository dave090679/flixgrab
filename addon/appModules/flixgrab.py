# flixgrab app module
import appModuleHandler
from NVDAObjects.UIA import UIA
class flixgrabobj(UIA):
	def _get_name(self):
		return self.UIAElement.cachedAutomationId.split(".")[-1]

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.name == ""  and isinstance(obj, UIA):
				clslist.insert(0, flixgrabobj)
