sudo apt update
sudo apt install python3 python3-venv python3-pip -y
python3 -m venv myenv
source myenv/bin/activate
pip install --upgrade pip
echo "requests" > requirements.txt
pip install -r requirements.txt
python check_requests.py
