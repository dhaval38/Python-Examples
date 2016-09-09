How to install Mongodb on Ubuntu:

Step 1 - Importing the Public Key

Execute below command to import key for official MongoDB repository
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10

After successfully importing the key you will see:

Output
gpg: Total number processed: 1
gpg:               imported: 1  (RSA: 1)


Step 2 - Create List File

Next, we have to add the MongoDB repository details so APT will know where to download the packages from.

Issue the following command to create a list file for MongoDB.
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list

After adding the repository details, we need to update the packages list.
sudo apt-get update

Step 3 — Installing and Verifying MongoDB

Now we can install the MongoDB package itself. Execute below command
sudo apt-get install -y mongodb-org

This command will install several packages containing latest stable version of MongoDB along with helpful management tools for the MongoDB server.

After package installation MongoDB will be automatically started. You can check this by running the following command.
service mongod status

If MongoDB is running, you'll see an output like this (with a different process ID).

Output
mongod start/running, process 1611
You can also stop, start, and restart MongoDB using the service command (e.g. service mongod stop, service mongod start).


How to install pymongo on ubuntu

Use pip for installing pymongo package on ubuntu as follows:
pip install pymongo

After completing the installtion execute the python script to read/write from MongoDB
