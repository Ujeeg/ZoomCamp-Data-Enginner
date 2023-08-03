# ZoomCamp-Data-Enginner
## Free Course From DataTalksClub 
## Week 1: Introduction & Prerequisites
    Course overview
    Introduction to GCP
    Docker and docker-compose
    Running Postgres locally with Docker
    Setting up infrastructure on GCP with Terraform
    Preparing the environment for the course

### 1. Seting Network Locally 
![Source](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/main/Week_1_setup/Setting%20Network%20Manually.yml)

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
![Source](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/cc3b37ab51db7318bb120bc80eb7b1c22ca65a40/Week_1_setup/Make%20Image%20to%20Ingest%20data.yml)
#### A. Create Dockerfile
![Source](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/cc3b37ab51db7318bb120bc80eb7b1c22ca65a40/Week_1_setup/Dockerfile)
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
        Result
        ![](https://github.com/Ujeeg/ZoomCamp-Data-Enginner/blob/29d38e2f0b478eaf3dce77d8e86b4b179fce691d/Picture/GCP/IM%20ADMIN%20SERVICE%20ACCOUNT%203.png)

### 4. Setting up GCP
#### A. Installing Google Cloud SDK ![Link](https://cloud.google.com/sdk/docs/downloads-interactive)
#### B. Intalling Python 3 (e.g. installed with Anaconda) ![Link](https://www.anaconda.com/download)
#### C.Docker with docker-compose
