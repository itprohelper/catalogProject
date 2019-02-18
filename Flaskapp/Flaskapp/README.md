# Linux server deployment
Project for the Udacity course
# Implemented Amazon's Lightsail for this project.

In your browser visit **http://54.144.244.87.xip.io/** to check out the Items Catalog from previous project.

## You can view JSON API structure on the following URLs:

**Summary of configurations and software used:**

Please refer to the requirements.txt for a list of Python modules used. 

**Configurations made**

The first step in this process is to install mod_wsgi:

`sudo apt-get install libapache2-mod-wsgi`

Add the line below on to your apache virtual host config in this case I used 000-default.conf. This tells Apache to handle requests using the WSGI module.

` WSGIScriptAlias / /var/www/html/capp.wsgi`

Restart Apache:

`sudo apache2ctl restart`

Visit the app in your browser **http://54.144.244.87.xip.io/**

**/login route still not working for me. This is the Google Oauth login method - Any help will be appreciated!**


Access server via SSH on port 2200 with username ***grader*** on 54.144.244.87
**Summary of software installed on this Ubuntu server:**

Apache2

PostgreSQL

libapache2-mod-wsgi 

python-dev

**Third party resources:**

https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps#step-four-%E2%80%93-configure-and-enable-a-new-virtual-host

https://github.com/ga4gh/ga4gh-server/issues/1365


