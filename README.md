Installation of python and git in ubuntu
git : https://git-scm.com/download/linux
python : 
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
sudo -H pip3 install --upgrade pip

clone the repo
git clone -b <branch> <remote_repo>

running server for long time
nohup long-running-process &

nginx server for public
sudo nano /etc/nginx/sites-available/fastapi_nginx
add to file :
server {
    listen 80;
    server_name 123.246.123.678;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}

sudo service nginx restart

