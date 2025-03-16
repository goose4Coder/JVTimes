When deploying on linux machine:

install docker, docker compose and git.

Then enter the directory needed:

git clone *here path to repo*

create .env file

then run in the directory needed

docker-compose build

then create file /etc/systemd/system/myapp.service
write to it the following:

[Unit]
Description=JVTimes dockercompose startup
After=network.target multi-user.target

[Service]
User=*name of user*
WorkingDirectory=*path of the project*
ExecStart=sudo docker-compose up
Restart=always
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=myapp

[Install]
WantedBy=multi-user.target

___

Then run the following commands:

sudo systemctl daemon-reload
sudo systemctl enable myapp.service
sudo systemctl start myapp.service

and check the state of the service by running:

sudo systemctl status myapp.service
or
sudo journalctl -u myapp.service
for logs.

If you reached no errors the deploy is complete. Congrats! 