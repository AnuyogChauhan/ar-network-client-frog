#!/usr/bin/env python

import os
import json
from datetime import datetime
from fabric.api import env
from fabric.api import run
from fabric.api import local
from fabric.contrib.files import exists
from fabric.context_managers import cd
from fabric.operations import put
from fabric.operations import get
from fabric.operations import sudo

#env.hosts = ['172.19.74.220']
#env.user = 'root'
#env.password = 'ubuntu'


def deployENSImagePrepackaged():
    local("make buildens")
    docker_filename = datetime.strftime(datetime.now(), "ar-network-ens-broadcast_%m-%d_%H%M%S.tar")
    local("docker save 127.0.0.1:5000/ens/ar-network-ens-broadcast > {0}".format(docker_filename))
    with cd("/root/Frog-integration/frog-apps-code/automatic/"):
        put(docker_filename, "./")
        run("docker load -i {0}".format(docker_filename))
        
    docker_filename1 = datetime.strftime(datetime.now(), "ar-network-ens-broadcast_%m-%d_%H%M%S.tar")
    local("docker save 127.0.0.1:5000/ens/ar-network-ens-client > {0}".format(docker_filename1))
    with cd("/root/Frog-integration/frog-apps-code/automatic/"):
        put(docker_filename1, "./")
        run("docker load -i {0}".format(docker_filename1))
        
def deployENSImage():
    run("rm -rf /root/Frog-integration/frog-apps-code/automatic/ar-network/")
    run("mkdir -p /root/Frog-integration/frog-apps-code/automatic/ar-network/")
    put("ens","/root/Frog-integration/frog-apps-code/automatic/ar-network/")
    put("lib","/root/Frog-integration/frog-apps-code/automatic/ar-network/")
    put("app-catalog.db-ar","/root/Frog-integration/frog-apps-code/automatic/ar-network/")
    put("Ar*.py","/root/Frog-integration/frog-apps-code/automatic/ar-network/")
    put("Dockerfile*","/root/Frog-integration/frog-apps-code/automatic/ar-network/")
    put("Makefile","/root/Frog-integration/frog-apps-code/automatic/ar-network/")
    run("cp /root/Frog-integration/frog-apps-code/automatic/ar-network/ens/mecsdk.conf /root/Frog-integration/frog-apps-code/automatic/ar-network/")
    with cd("/root/Frog-integration/frog-apps-code/automatic/ar-network/"):
        run("make buildens")
    put("app-catalog.db-ar", "/root/Frog-integration/tcp_frog-sdk/tcp_frog-sdk/frog-sdk/sdk/cloudlet/bin/app-catalog.db-ar-upload")
    run("mv /root/Frog-integration/tcp_frog-sdk/tcp_frog-sdk/frog-sdk/sdk/cloudlet/bin/app-catalog.db-ar-upload /root/Frog-integration/tcp_frog-sdk/tcp_frog-sdk/frog-sdk/sdk/cloudlet/bin/app-catalog.db")
    
def deployENSClient():
    put("app-catalog.db-ar", "/root/Frog-integration/tcp_frog-sdk/tcp_frog-sdk/frog-sdk/sdk/cloudlet/bin/app-catalog.db-ar-upload")
    run("mv /root/Frog-integration/tcp_frog-sdk/tcp_frog-sdk/frog-sdk/sdk/cloudlet/bin/app-catalog.db-ar-upload /root/Frog-integration/tcp_frog-sdk/tcp_frog-sdk/frog-sdk/sdk/cloudlet/bin/app-catalog.db")
    # cd /root/Frog-integration/tcp_frog-sdk/tcp_frog-sdk/frog-sdk/sdk/cloudlet/bin/
    # source startDispatcher.sh
    # python workload-tester.py app-catalog.db
    put("ens", "/root/Frog-integration/frog-apps-code/automatic/ar-network/")
    put("ens/mecsdk.conf", "/root/Frog-integration/frog-apps-code/automatic/ar-network/")
    put("lib", "/root/Frog-integration/frog-apps-code/automatic/ar-network/")
    put("ArClientENS.py", "/root/Frog-integration/frog-apps-code/automatic/ar-network/")
    # cd /root/Frog-integration/frog-apps-code/automatic/ar-network/
    # python ArClientENS.py

def getAppCatalog():
    get("/root/Frog-integration/tcp_frog-sdk/tcp_frog-sdk/frog-sdk/sdk/cloudlet/bin/app-catalog.db-ar","./")
    get("/root/Frog-integration/tcp_frog-sdk/tcp_frog-sdk/frog-sdk/sdk/cloudlet/bin/app-catalog.db-car","./")
    get("/root/Frog-integration/tcp_frog-sdk/tcp_frog-sdk/frog-sdk/sdk/cloudlet/bin/app-catalog.db-robot","./")

def deployDocker():
    run("rm -rf /home/ubuntu/ar-network")
    run("mkdir -p /home/ubuntu/ar-network")
    put("Dockerfile.traditional", "/home/ubuntu/ar-network/")
    put("Makefile", "/home/ubuntu/ar-network/")
    put("lib", "/home/ubuntu/ar-network/")
    put("Ar*", "/home/ubuntu/ar-network/")
    with("cd /home/ubuntu/ar-network"):
        sudo("make build")
        sudo("make run")


