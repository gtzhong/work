@echo off
echo       
echo   1.����PHP��������� PhpStudy.exe
start "��������" "C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\phpStudy.lnk"
echo   
echo   2.�������ݿ���� SQLyog.exe
start "" /b "C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\SQLyog.lnk"
echo    
echo   3.�����ȸ������ Chrome.exe
start "" /b "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://www.github.com http://www.stackoverflow.com http://www.csdn.net http://www.baidu.com 
Ping -l 1 -n 1 -w 6000 1.1.1.1 -4 1>nul 2>&1
echo   
echo   4.�����ӿڵ������ Postman.exe
start "" /b "C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Ӧ��\Postman.lnk" 
echo    
echo   5.����PHP���ɿ������� PhpStorm.exe
start "" /b "E:\��װ���\IntelliJIDEALicenseServer(0.0.0.0_41017)\IntelliJIDEALicenseServer_windows_386.exe"
start "" /b "C:\Program Files\JetBrains\PhpStorm 2017.1.3\bin\phpstorm64.exe"
echo   �ȴ����� PhpStorm.exe ����
Ping -l 1 -n 1 -w 18000 1.1.1.1 -4 1>nul 2>&1
echo   
echo   6.���������й��� Cmder.exe
start "" /b "E:\cmder_mini\Cmder.exe"
echo   
echo   7.����git����
start "" /b "C:\Users\Administrator\Desktop\git.build.vbs"