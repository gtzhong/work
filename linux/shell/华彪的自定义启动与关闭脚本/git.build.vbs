Set ws = WScript.CreateObject("WScript.Shell")
WScript.sleep(1200)
ws.AppActivate "Cmder"
ws.SendKeys "w"
ws.AppActivate "Cmder"
ws.SendKeys "{ENTER}"
ws.AppActivate "Cmder"
ws.SendKeys "git co base_v2"
ws.SendKeys "{ENTER}"
ws.AppActivate "Cmder"
ws.SendKeys "git pull origin base_v2"
WScript.sleep(2000)
ws.AppActivate "Cmder"
ws.SendKeys "{ENTER}"
ws.SendKeys "wv"
ws.AppActivate "Cmder"
ws.SendKeys "{ENTER}"
ws.AppActivate "Cmder"
ws.SendKeys "b"
ws.AppActivate "Cmder"
ws.SendKeys "{ENTER}"
WScript.sleep(6000)
ws.AppActivate "Cmder"
ws.SendKeys "w"
ws.AppActivate "Cmder"
ws.SendKeys "{ENTER}"
ws.SendKeys "cls"
ws.SendKeys "{ENTER}"