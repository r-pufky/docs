# Removes pre-install crapware from Windows 10
# Adjust list as needed, automatically wraps with globs. Case Insensitive.
# Exection policy needs to be unrestricted, and run as admin
#
# From:
#  https://thomas.vanhoutte.be/miniblog/delete-windows-10-apps/
#  http://www.makeuseof.com/tag/3-clever-powershell-functions-upgrading-windows-10/
#  http://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system
#
#
$apps_to_remove =
	'zune',
	'bing',
	'SkypeApp',
	'WindowsMaps',
	'SolitaireCollection',
	'OneNote',
	'facebook',
	'twitter',
	'netflix',
	'xbox',
	'3dbuilder',
	'messaging',
	'oneconnect',
	'office',
	'stickynotes',
	'windowsphone',
	'windowssoundrecorder',
	'windowscamera',
	'windows.photos',
	'getstarted'

foreach ($app in $apps_to_remove) {
	Get-AppxPackage -AllUsers ('*%s*' -replace '%s', $app) | Remove-AppxPackage 
}