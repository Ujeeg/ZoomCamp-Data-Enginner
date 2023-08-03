# ZoomCamp-Data-Enginner
## Free Course From DataTalksClub 
## Week 1: Introduction & Prerequisites
    * Course overview
    * Introduction to GCP
    * Docker and docker-compose
    * Running Postgres locally with Docker
    * Setting up infrastructure on GCP with Terraform
    * Preparing the environment for the course

### 1. Seting Network Locally 
* ![Source](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/main/Week_1_setup/Setting%20Network%20Manually.yml)

#### A. Use Local to open PGADMIN
![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/77cd2bad0c70d8a2bcd59366274809c9602a27da/Picture/Setting%20up%20Connection/PG%20ADMIN%20Locally.png)

#### B. Connect to Server 
##### (Create Server Name)
![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/77cd2bad0c70d8a2bcd59366274809c9602a27da/Picture/Setting%20up%20Connection/Connecting%20Server%201.png)
##### (Connect with Host Name, User, and password)
![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/77cd2bad0c70d8a2bcd59366274809c9602a27da/Picture/Setting%20up%20Connection/connecting%20server%202.png)
##### (also can connect use pgcli with gitbash)
![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/77cd2bad0c70d8a2bcd59366274809c9602a27da/Picture/Setting%20up%20Connection/connect%20with%20gitbash%20using%20pgcli.png)

### 3. Make Image and Upload data to PGADMIN local server

* ![Source](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/cc3b37ab51db7318bb120bc80eb7b1c22ca65a40/Week_1_setup/Make%20Image%20to%20Ingest%20data.yml)

#### A. Create Dockerfile
* ![Source](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/cc3b37ab51db7318bb120bc80eb7b1c22ca65a40/Week_1_setup/Dockerfile)
![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/e0d128a7fea15be3255d421af0fa1f24a665a44e/Picture/Make%20imange%20to%20ingest_data%20to%20server/Make%20Docker%20file.png)
#### B. Create Ingest_data.py
![Source](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/cc3b37ab51db7318bb120bc80eb7b1c22ca65a40/Week_1_setup/ingest_data.py)

![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/e0d128a7fea15be3255d421af0fa1f24a665a44e/Picture/Make%20imange%20to%20ingest_data%20to%20server/Make%20ingest_data.png)
#### C. Create Image Ingest_data.V001
![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/e0d128a7fea15be3255d421af0fa1f24a665a44e/Picture/Make%20imange%20to%20ingest_data%20to%20server/make%20Image%20Ingest%20data.png)
#### D. Run Image ingest_data.V001
![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/e0d128a7fea15be3255d421af0fa1f24a665a44e/Picture/Make%20imange%20to%20ingest_data%20to%20server/Run%20Image%20Ingest_data.png)
##### After upload data to local server
![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/e0d128a7fea15be3255d421af0fa1f24a665a44e/Picture/Make%20imange%20to%20ingest_data%20to%20server/PGADMIN%20AFTER%20Ingest_data.png)
### 5. Setup for Access Google Console 
#### 1. IAM Roles for Service account:
Go to the IAM section of IAM & Admin https://console.cloud.google.com/iam-admin/iam
Click the Edit principal icon for your service account.
Add these roles in addition to Viewer : Storage Admin + Storage Object Admin + BigQuery Admin
        ![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/29d38e2f0b478eaf3dce77d8e86b4b179fce691d/Picture/GCP/IM%20ADMIN%20SERVICE%20ACCOUNT%201.png) ![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/29d38e2f0b478eaf3dce77d8e86b4b179fce691d/Picture/GCP/IM%20ADMIN%20SERVICE%20ACCOUNT%202.png) 
        
**Result**
![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/29d38e2f0b478eaf3dce77d8e86b4b179fce691d/Picture/GCP/IM%20ADMIN%20SERVICE%20ACCOUNT%203.png)

### 4. environment variable to point to your downloaded GCP keys: 

        export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"

        export GOOGLE_APPLICATION_CREDENTIALS=/c/Users/fajar/Downloads/snappy-byte-394006-2ddf7aea62ff.json /#Example
        
        gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS

        Refresh token/session, and verify authentication
            
            gcloud auth application-default login

![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/cb8ba643e87d0bc54cd1e53de7e7dad0c0d241fc/Picture/GCP/CMD%20connect%20google.png)

        Result
![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/13f4ad55962ead6fe906d6bdb566a851f3e169d5/Picture/GCP/connected%20allow.png)

### 5. Installing and setting up Terraform 
* ![source](https://www.terraform.io/)

Use this in folder terraform for setting up terrafom
       
        terraform init

![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/13f4ad55962ead6fe906d6bdb566a851f3e169d5/Picture/Setting%20up%20terraform/Terraform%20init.png)

Use this for prepare the bucket
        
        terraform plan
![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/13f4ad55962ead6fe906d6bdb566a851f3e169d5/Picture/GCP/terraform%20apply.png)

Use this to push bucket to gcp

        terraform apply

![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/13f4ad55962ead6fe906d6bdb566a851f3e169d5/Picture/GCP/terraform%20plant%20apply.png)

Result

![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/13f4ad55962ead6fe906d6bdb566a851f3e169d5/Picture/GCP/data%20bucket.png)

### 6. Setting up the environment on cloud VM
### 7. Generating SSH keys
* Create folder .ssh in HOME directory
   mkdir .ssh
* Create SSH Key
  ssh-keygen -t rsa -f ~/.ssh/KEY_FILENAME -C USERNAME -b 2048
  * Example
    ssh-keygen -t rsa -f ~/.ssh/GCP -C ujeeg -b 2048
![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/558318a7f3f6ed1406dbc090b4a4a2b261915a13/Picture/VM%20Setting/create%20ssh%20bash.png)

* Open GCP ssh
![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/558318a7f3f6ed1406dbc090b4a4a2b261915a13/Picture/VM%20Setting/open%20gcp.pub.png)

* Copy to GCP > Metadata > SSH Key > Save
![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/558318a7f3f6ed1406dbc090b4a4a2b261915a13/Picture/VM%20Setting/copy%20ssh.png)

* Test SSH connection
     ssh -i ~/.ssh/<ssh-name> username@ipexternal
  ![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/558318a7f3f6ed1406dbc090b4a4a2b261915a13/Picture/VM%20Setting/run%20VM.png)
   * Result when VM running correctly
     ![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/558318a7f3f6ed1406dbc090b4a4a2b261915a13/Picture/VM%20Setting/VM%20running.png)
* Create ssh config
  You can run VM with ssh de-zoomcamp
     ![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/558318a7f3f6ed1406dbc090b4a4a2b261915a13/Picture/VM%20Setting/Config%20ssh.png)
   *testing
     ![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/558318a7f3f6ed1406dbc090b4a4a2b261915a13/Picture/VM%20Setting/resut%20config.png)

## After this you can install environment in VM and reapeat step 1 until 5, so you can run docker and made image or pgserver in VM
