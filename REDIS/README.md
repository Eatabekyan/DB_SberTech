# REDIS

## STEP1
### RUN DOCKER CONTAINER WITH REDIT

![GitHub Image](/REDIS/images/1.png)
## STEP2
### CHECK REDIS-INSIGHT

DB is empty yet!
![GitHub Image](/REDIS/images/2.png)

## STEP3
### FIND & DOWNLOAD JSON FILE (>20Mb)
**From here:** https://examplefile.com/code/json/20-mb-json

![GitHub Image](/REDIS/images/3.png)

## STEP4
### SAVE LARGE JSON (~20MB) IN THE FORM OF DIFFERENT STRUCTURES - STRING, SET, SET, LIST & TEST SPEED FOR ADDING AND READING

I decided to use Python for that.

[Python Script](/REDIS/main.py)

![GitHub Image](/REDIS/images/4.png)

![GitHub Image](/REDIS/images/5.png)

![GitHub Image](/REDIS/images/6.png)


## STEP 5

### CREATE CLUSTER

I've created directories for each port I want to use for my cluster

Directories: [8401](/REDIS/8401), [8402](/REDIS/8402),[8403](/REDIS/8403)

Added config files(redis.conf) in each of them for each node 

## STEP 6
### RUN CLUSTER

![GitHub Image](/REDIS/images/7.png)

![GitHub Image](/REDIS/images/8.png)

![GitHub Image](/REDIS/images/10.png)

![GitHub Image](/REDIS/images/9.png)

![GitHub Image](/REDIS/images/11.png)

## STEP 7
### ADD DATA IN CLUSTER

[Python Script](/REDIS/main_cluster.py)

![GitHub Image](/REDIS/images/12.png)

![GitHub Image](/REDIS/images/13.png)


# THE END