    $ apt-get install git python-pip
    $ pip install ansible
    $ git clone https://github.com/iwebhosting/php-benchmarks.git
    $ cd php-benchmarks
    $ ansible-playbook -i inventory -c local apache2.2_fpm_magento.yml
    …..
    $ curl -I localhost
    HTTP/1.1 200 OK
    ………
