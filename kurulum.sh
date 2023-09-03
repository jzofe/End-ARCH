#Bu scripti "sudo ./kurulum.sh" ile çalıştırabilirsiniz
echo Kurulum başladı
sudo pacman -S python3 

sudo pacman -S python-colorama --noconfirm

sudo chmod +x EndArch.py

cd /bin/ 

chmod 777 *

cd ..

clear
echo Kurulum tamamlandı. "sudo python3 EndArch.py" komudu ile scripti çalıştırabilirsiniz.
