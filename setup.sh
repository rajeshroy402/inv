sudo apt install speedtest-cli

echo "copy service files"

sudo cp restart* /etc/systemd/system/

cd /etc/systemd/system/
sudo systemctl start restart_sheet.service
sudo systemctl enable restart_sheet.service
sudo systemctl start restart_speed.service
sudo systemctl enable restart_speed.service

cd /home/nvidia/inv

