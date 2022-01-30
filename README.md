# Home Work

Ansible automation test.

## Description

Test case to manage 3 servers environment using [Ansible](https://www.ansible.com)

## Getting Started

Following software were used to setup environments :

* [VirtualBox](https://virtualbox.org)
* Oracle Database - binaries/rpm could be downloaded directly from [here](https://www.oracle.com/database/technologies/oracle19c-linux-downloads.html)
* Oracle Instant Client - could be downloaded directly from [here](https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html)

### Dependencies

* CentOS Linux release 7.9
* Ansible 2.9.27
* Python 3.6.8
* cx_Oracle 8.3.0
* git version 1.8.3.1
* oracle-instantclient-basic.x86_64   21.5
* oracle-instantclient-sqlplus.x86_64 21.5
* Oracle Database EE 19.3

OS user centos was used for testing.

### Installing

* Setup 3 Linux VM's. Disable firewall, set folowing hostnames : 
    * srvans1 (ansible server) 
    * srvapp1 (application server)
    * srboradb1 (oracle database server)

* Prepare database (srvoradb1):
    * Install Oracle database software
    * Create database ORCLPDB1
    * Create user ansible, password ansible. Grant create table privilege and unlimited tablespace users.

* Prepare Ansible (srvans1) :
    * Edit /etc/hosts. All 3 VM's should be pingable by hostname. 
    * Install ansible
    ``` 
    sudo yum install epel-release
    sudo yum install ansible
    ```    
    * donwload oracle client rpm's to /home/centos
    * generate SSH key and upload
    ```
    ssh-keygen -t rsa
    ssh-copy-id srvapp1
    ssh-copy-id srvoradb1
    ```
    * preparing project files on srvans1 :
    ```
    cd /home/centos
    git clone https://github.com/giemst/ansible-test1.git
    ```
    * setup Ansible inventory on srvans1 :
    ```
    sudo tee -a /etc/ansible/hosts << EOF
    [appservers]
    srvapp1

    [dbservers]
    srvoradb1
    EOF
    ```
    * Run ansible to update /etc/hosts on all the VM's
    ```
    cd /home/centos/ansible-test1
    ansible-playbook hosts.yml
    ```
    * Install oracle client,Python3, Python3-pip, cx_Oracle on srvapp1
    ```
    ansible-playbook oracle-client-installation.yml
    ansible-playbook python_inst.yml
    ```

### Executing test

* Host: srvans1

    * Change working directory to /home/centos/ansible-test1
    ```
    cd /home/centos/ansible-test1
    ```

    * Run playbook which create table, generate 1M randoom data, extract 100 rows of data in csv format and put into /tmp/gathered_data.csv on srvans1. 
    ```
    ansible-playbook process_data.yml
    ```
    * To check results examine content of file : /tmp/gathered_data.csv

## Authors

Giedrius Mosteikis

## Version History

  * Initial Release

## Acknowledgments

Knowlege, code examples, etc.
* [Ansible docs online](https://docs.ansible.com)
* [w3schools](https://www.w3schools.com)
