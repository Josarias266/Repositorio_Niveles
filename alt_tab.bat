echo set WshShell = CreateObject("WScript.Shell") >alttab.vbs
echo WshShell.Sendkeys "%%{TAB}" >>alttab.vbs
cscript alttab.vbs
del alttab.vbs