# 1. MongoDB Installation (on Ubuntu)

I've successfully installed MongoDB on my Ubuntu machine by following the instructions from the MongoDB documentation: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#import-the-public-key-used-by-the-package-management-system

![GitHub Image](/MongoDB/images/installation1.png)

![GitHub Image](/MongoDB/images/installation2.png)


![GitHub Image](/MongoDB/images/installation3.png)

![GitHub Image](/MongoDB/images/installation4.png)

![GitHub Image](/MongoDB/images/installation5.png)

# 2. Choosing a dataset

I've decided to work with the wine+quality datasets because I enjoy wine and it would be interesting to work with and learn about the characteristics of different types of wines that I would like to taste.

**Dataset link:**
https://archive.ics.uci.edu/dataset/186/wine+quality

### About the datasets

Two datasets are included, related to red and white vinho verde wines, from the north of Portugal. The goal is to model wine quality based on physicochemical tests (see [Cortez et al. (2009)], http://www3.dsi.uminho.pt/pcortez/wine/).

We have 13 variable kinds here: 11 features, 1 target variable, and 1 other variable (characteristic about wine color).

# 3. Creating a DB and collections

I've decided to name my DB `wineDB`.
I want to have 3 collections: `wines` (includes `_id` and `color`), `red_wines` (includes `_id`, `wine_id`(id in collection `wines`) and characteristics for red wines), and `white_wines` (includes `_id`, `wine_id`(id in collection `wines`) and characteristics for white wines)

### 1. Step

First, let's check what databases we have:

![GitHub Image](/MongoDB/images/create1.png)


### 2. Step
I've created my DB `wineDB`

![GitHub Image](/MongoDB/images/create2.png)


### 3. Create collections

Let's create the necessary collections now that we don't have them:

![GitHub Image](/MongoDB/images/create3.png)

![GitHub Image](/MongoDB/images/create4.png)


# 4. Insert data

## Insert into collection "wines"

To insert data into the "wines" collection, I'll use a JavaScript for loop in the mongosh console to add 6 red wines and 6 white wines.

![GitHub Image](/MongoDB/images/insert1.png)

## Insert into collection "red_wines"

To insert data into the "red_wines" collection, I'll use the `insertMany()` method to add 6 red wines.


![GitHub Image](/MongoDB/images/insert2.png)

![GitHub Image](/MongoDB/images/insert3.png)

What we have in collection?

![GitHub Image](/MongoDB/images/insert4.png)


## Insert into collection "white_wines"

To insert data into the "white_wines" collection, I'll also use the `insertMany()` method to add 6 white wines.

![GitHub Image](/MongoDB/images/insert5.png)

![GitHub Image](/MongoDB/images/insert6.png)

What we have in collection?

![GitHub Image](/MongoDB/images/insert7.png)


# 5. Update and Delete

To understand if I want to try a wine, I only need a few variables, so I
decided to delete them using updateMany().

![GitHub Image](/MongoDB/images/update.png)


So I want to delete all red wines that have a quality rating less than 5.166666
and all white wines that have a quality rating less than 6.

![GitHub Image](/MongoDB/images/delete1.png)

![GitHub Image](/MongoDB/images/delete2.png)

![GitHub Image](/MongoDB/images/delete4.png)

![GitHub Image](/MongoDB/images/delete3.png)

Since there are no white wines with a quality rating less than average, I
decide to delete wines with a higher alcohol content.

![GitHub Image](/MongoDB/images/delete5.png)

I read about how to get an array of ids from a cursor here:
https://www.mongodb.com/docs/manual/reference/method/cursor.map/

![GitHub Image](/MongoDB/images/reference.png)


![GitHub Image](/MongoDB/images/delete6.png)



# 6. Indexing and performance comparison

**I want to have a larger dataset for examining indexing and performance comparison, so I will completely refresh my collections by deleting everything and then filling them with data from datasets**

![GitHub Image](/MongoDB/images/delete&fill1.png)

![GitHub Image](/MongoDB/images/delete&fill2.png)

![GitHub Image](/MongoDB/images/delete&fill3.png)

![GitHub Image](/MongoDB/images/delete&fill4.png)

![GitHub Image](/MongoDB/images/delete&fill5.png)

![GitHub Image](/MongoDB/images/delete&fill6.png)


For making performance comparison I create indexes for red_wines collection and try to compare speeds of query "find" with index and without it.

For that I decided to use Profiler(read about it here: https://hevodata.com/learn/mongodb-profiler/) and `explain("executionStats")`
## Create Indexes
**Read here:** https://www.mongodb.com/docs/manual/reference/method/db.collection.createIndex/

I decided to create index for red wines.

![GitHub Image](/MongoDB/images/index&profile1.png)

## Start Profiling

I dropped the old system.profile collection as it was filled with rubbish in my DB, because I decided to play with it to understand how it works =).

I've created a new system.profile collection sized at 5 MB (5000000 bytes), execute the following sequence of commands in mongosh:

![GitHub Image](/MongoDB/images/index&profile2.png)

Level 2 for the profiler collects profiling data for all the database operations.

![GitHub Image](/MongoDB/images/index&profile3.png)


Than I tried to find some kind of wines in my collection "red_wine"
and see stats in collection `system.profile`

![GitHub Image](/MongoDB/images/index&profile4.png)

![GitHub Image](/MongoDB/images/index&profile5.png)

Also I tried to drop index and try the same

![GitHub Image](/MongoDB/images/index&profile6.png)

![GitHub Image](/MongoDB/images/index&profile7.png)

![GitHub Image](/MongoDB/images/index&profile8.png)


**RESULT**: with index MongoDB examines only 569 keys and finds the result without examining documents (it finds the result very quickly), whereas without them it examines all 1599 documents and does not find anything (it takes longer to find the result), because there would not be a result by my parameters as we do not have any wine with this parameters.



Lets do the same using `explain("executionStats")`

### With indexes
![GitHub Image](/MongoDB/images/index&profile9.png)

![GitHub Image](/MongoDB/images/index&profile10.png)

![GitHub Image](/MongoDB/images/index&profile11.png)

### Drop indexes

![GitHub Image](/MongoDB/images/index&profile12.png)

![GitHub Image](/MongoDB/images/index&profile13.png)

![GitHub Image](/MongoDB/images/index&profile14.png)


**RESULT**: same as profiler result 

# END OF MY EXPERIMENT WITH MONGO***DB***