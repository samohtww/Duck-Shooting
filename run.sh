apt update && apt -y upgrade
apt install -y python3-tk python3-pip python3-venv
python3 -m venv ./venv
./venv/bin/pip install pillow playsound
