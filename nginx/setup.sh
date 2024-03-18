sudo apt-get install -y nginx
sudo cp api.conf /etc/nginx/sites-available/api.conf
sudo ln -s /etc/nginx/sites-available/api.conf /etc/nginx/sites-enabled/api.conf
sudo nginx -t
sudo systemctl restart nginx.service