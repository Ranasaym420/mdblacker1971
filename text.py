#colour section
red='\033[1;31m'
rset='\033[0m'
grn='\033[1;32m'
ylo='\033[1;33m'
#script coding starts
clear
echo " "
echo " "
echo '
                  _  _  ___  ___   __  ____  ___ 
                 ( )( )(  ,\(   \ (  )(_  _)(  _)
                  )()(  ) _/ ) ) )/__\  )(   ) _)
                  \__/ (_)  (___/(_)(_)(__) (___) v 1.2
'|lolcat
echo " "
echo " "
sleep 6.0
clear
echo -e "$blue                         CHECKING..>$rset"
sleep 2.0
clear
echo -e "$blue                         CHECKING...>$rset"
sleep 2.0
clear
echo -e "$blue                         CHECKING....>$rset"
sleep 2.0
clear
echo -e "$blue
                         CHECKING.....>$rset"
sleep 2.0
clear
echo " "
echo " "
echo -e "$grn                UPDATING THE SMF PLEASE wait$rset"
sleep 2.0
cd $HOME
rm -rf SMF
git clone https://github.com/mdblacker-1971
clear
echo " "
echo -e "$grn               BD HAS BEEN UPDATED CHECK IT NOW...$rset"
sleep 3.0
echo " "
cd $HOME
cd SMF
unzip techcochi.zip
rm -rf techcochi.zip
bash smf.sh
clear
sleep 1.0