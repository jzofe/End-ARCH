MAVI=$(echo -e "\e[1;36m")  
MAVIN=$(echo -e "\e[0;36m") 
YK=$(echo -e "\e[0;0;0m")  
KIRN=$(echo -e "\e[1;31m")  
BOM=$(echo -e "\e[1;32m")  
YSL=$(echo -e "\e[0;32m")  
KIRM=$(echo -e "\e[0;31m")  


f_header() {
echo $YSL"
    ▓█████  ███▄    █ ▓█████▄     ▄▄▄       ██▀███   ▄████▄   ██░ ██
    ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌   ▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒
    ▒███   ▓██  ▀█ ██▒░██   █▌   ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░
    ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌   ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██
    ░▒████▒▒██░   ▓██░░▒████▓     ▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓
    ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒     ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒
      ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒      ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░
        ░      ░   ░ ░  ░ ░  ░      ░   ▒     ░░   ░ ░         ░  ░░ ░
        ░  ░         ░    ░             ░  ░   ░     ░ ░       ░  ░  ░
                       ░                            ░
                                                                                                              
"$YK
}
clear
exec > /dev/tty
exec 2>&1
f_header
echo -n $BOM">$YK En : Örnek = $KIRN endertopluluk.com $YK:"$MAVI
read lookup
if [ "$lookup" == "" ] ; then 
echo $KIRN">$YK Eksik giriş veya hatalı giriş, " 
echo
exit
fi
clear
f_header
echo $YK
echo $BOM"> $MAVI$lookup$YK seçildi"
sleep 1.25

echo "Nslookup ile kontrol ediliyor...."
NS=$(nslookup $lookup | sed '0,/Non-authoritative/d' | grep -i Address | sed 's/Address://')
MAXNR=$(echo $NS | sed 's/ /\n/' | wc -l)
for i in $(seq 1 $MAXNR) ; do 
IP=$(echo $NS | sed 's/ /\n/' | sed -n "$i"p)
IP_NETNAME=$(whois $IP | grep -i netname | awk '{print $2}')
echo "$YSL$IP$YK --> $YSL$IP_NETNAME$YK" 
done
sleep 1.25
echo $YK

CPANEL_RESULT=$(nslookup cpanel.$lookup | sed '0,/Non-authoritative/d' | grep -i Address | sed 's/Address://')
if [ "$CPANEL_RESULT" == "" ] ; then 
echo $BOM">$YK Resolve Case 1 of 9$MAVIN [$YK Cpanel$MAVIN ]$KIRN --> $YK$FAIL"
else
echo $BOM">$YK Resolve Case 1 of 9$MAVIN [$YK Cpanel$MAVIN ]$YSL --> $YK$CPANEL_RESULT"
CPANEL_NETNAME=$(whois $CPANEL_RESULT | grep -i netname | awk '{print $2}')
echo "NetName of $YSL$CPANEL_RESULT$YK --> $YSL$CPANEL_NETNAME"
fi
sleep 1.25
echo $YK

FAIL="Çözülemedi"
#
FTP_RESULT=$(nslookup ftp.$lookup | sed '0,/Non-authoritative/d' | grep -i Address | sed 's/Address://')
if [ "$FTP_RESULT" == "" ] ; then 
echo $BOM">$YK Resolve Case 2 of 9$MAVIN [$YK FTP$MAVIN ]$KIRN -----> $YK$FAIL"
else
echo $BOM">$YK Resolve Case 2 of 9$MAVIN [$YK FTP$MAVIN ]$YSL -----> $YK$FTP_RESULT"
FTP_NETNAME=$(whois $FTP_RESULT | grep -i netname | awk '{print $2}')
echo "NetName of$YSL$FTP_RESULT$YK --> $YSL$FTP_NETNAME"
fi
sleep 1.25
echo $YK

WEBDISK_RESULT=$(nslookup webdisk.$lookup | sed '0,/Non-authoritative/d' | grep -i Address | sed 's/Address://')
if [ "$WEBDISK_RESULT" == "" ] ; then 
echo $BOM">$YK Resolve Case 3 of 9$MAVIN [$YK Webdisk$MAVIN ]$KIRN --> $YK$FAIL"
else
echo $BOM">$YK Resolve Case 3 of 9$MAVIN [$YK Webdisk$MAVIN ]$YSL --> $YK$WEBDISK_RESULT"
WEBDISK_NETNAME=$(whois $WEBDISK_RESULT | grep -i netname | awk '{print $2}')
echo "NetName of $YSL$WEBDISK_RESULT$YK --> $YSL$WEBDISK_NETNAME"
fi
sleep 1.25
echo $YK

WEBMAIL_RESULT=$(nslookup webmail.$lookup | sed '0,/Non-authoritative/d' | grep -i Address | sed 's/Address://')
if [ "$WEBMAIL_RESULT" == "" ] ; then 
echo $BOM">$YK Resolve Case 4 of 9$MAVIN [$YK Webmail$MAVIN ]$KIRN --> $YK$FAIL"
else
echo $BOM">$YK Resolve Case 4 of 9$MAVIN [$YK Webmail$MAVIN ]$YSL --> $YK$WEBMAIL_RESUL$"
WEBMAIL_NETNAME=$(whois $WEBMAIL_RESULT | grep -i netname | awk '{print $2}')
echo "NetName of$YSL$WEBMAIL_RESULT$YK --> $YSL$WEBMAIL_NETNAME"
fi
sleep 1.25
echo $YK""

WHM_RESULT=$(nslookup whm.$lookup | sed '0,/Non-authoritative/d' | grep -i Address | sed 's/Address://')
if [ "$WEBDISK_RESULT" == "" ] ; then 
echo $BOM">$YK Resolve Case 5 of 9$MAVIN [$YK Whm$MAVIN ]$KIRN --> $YK$FAIL"
else
echo $BOM">$YK Resolve Case 5 of 9$MAVIN [$YK Whm$MAVIN ]$YSL --> $YK$WHM_RESULT"
WHM_NETNAME=$(whois $WHM_RESULT | grep -i netname | awk '{print $2}')
echo "NetName of $YSL$WHM_RESULT$YK --> $YSL$WHM_NETNAME"
fi
sleep 1.25
echo $YK

MAIL_RESULT=$(nslookup mail.$lookup | sed '0,/Non-authoritative/d' | grep -i Address | sed 's/Address://')
if [ "$MAIL_RESULT" == "" ] ; then 
echo $BOM">$YK Resolve Case 6 of 9$MAVIN [$YK Mail$MAVIN ]$KIRN ----> $YK$FAIL"
else
echo $BOM">$YK Resolve Case 6 of 9$MAVIN [$YK Mail$MAVIN ]$YSL ----> $YK$MAIL_RESULT"
MAIL_NETNAME=$(whois $MAIL_RESULT | grep -i netname | awk '{print $2}')
echo "NetName of$YSL$MAIL_RESULT$YK --> $YSL$MAIL_NETNAME"
fi
sleep 1.25
echo $YK""

DIRECT_RESULT=$(nslookup direct.$lookup | sed '0,/Non-authoritative/d' | grep -i Address | sed 's/Address://')
if [ "$DIRECT_RESULT" == "" ] ; then 
echo $BOM">$YK Resolve Case 7 of 9$MAVIN [$YK Direct$MAVIN ]$KIRN --> $YK$FAIL"
else
echo $BOM">$YK Resolve Case 7 of 9$MAVIN [$YK Direct$MAVIN ]$YSL --> $YK$DIRECT_RESULT"
DIRECT_NETNAME=$(whois $DIRECT_RESULT | grep -i netname | awk '{print $2}')
echo "NetName of$YSL$DIRECT_RESULT$YK --> $YSL$DIRECT_NETNAME"
fi
sleep 1.25
echo $YK""

DIRECT_RESULTC=$(nslookup direct-connect.$lookup | sed '0,/Non-authoritative/d' | grep -i Address | sed 's/Address://')
if [ "$DIRECTC_RESULT" == "" ] ; then 
echo $BOM">$YK Resolve Case 8 of 9$MAVIN [$YK Direct-Connect$MAVIN ]$KIRN --> $YK$FAIL"
else
echo $BOM">$YK Resolve Case 8 of 9$MAVIN [$YK Direct-Connect$MAVIN ]$YSL --> $YK$DIRECTC_RESUL$"
DIRECT_NETNAME=$(whois $DIRECTC_RESULT | grep -i netname | awk '{print $2}')
echo "NetName of$YSL$DIRECTC_RESULT$YK --> $YSL$DIRECTC_NETNAME"
fi
sleep 1.25
echo $YK""

PORTAL_RESULT=$(nslookup portal.$lookup | sed '0,/Non-authoritative/d' | grep -i Address | sed 's/Address://')
if [ "$PORTAL_RESULT" == "" ] ; then 
echo $BOM">$YK Resolve Case 9 of 9$MAVIN [$YK Portal$MAVIN ]$KIRN --> $YK$FAIL"
else
echo $BOM">$YK Resolve Case 9 of 9$MAVIN [$YK Portal$MAVIN ]$YSL --> $YK$PORTAL_RESUL$"
PORTAL_NETNAME=$(whois $PORTAL_RESULT | grep -i netname | awk '{print $2}')
echo "NetName of$YSL$PORTAL_RESULT$YK --> $YSL$PORTAL_NETNAME"
fi
sleep 1.25
echo $YK""

echo $KIRM">$YK Çözümleme tamamlandı$KIRM <$YK"
echo "$MAVIN Devam etmek için ENTER'e basın...$MAVIE"
read enter
echo $YK""
bash dnsresolver.sh
 
