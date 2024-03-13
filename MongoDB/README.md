# 1. MangoDB Installation(on Ubuntu)
I've installed MangoDB by instructions from this link: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#import-the-public-key-used-by-the-package-management-system

![GitHub Image](/MongoDB/images/installation1.png)

![GitHub Image](/MongoDB/images/installation2.png)


![GitHub Image](/MongoDB/images/installation3.png)

![GitHub Image](/MongoDB/images/installation4.png)

![GitHub Image](/MongoDB/images/installation5.png)

# 2. Choosing DataSet

I've decided to choose the wine+quality datasets because I enjoy wine, and it would be interesting to work with and, at the same time, learn about the characteristics of different types of wines that I would like to taste.

**Dataset Link:**
https://archive.ics.uci.edu/dataset/186/wine+quality

### About Datasets
Two datasets are included, related to red and white vinho verde wines, from the north of Portugal. The goal is to model wine quality based on physicochemical tests (see [Cortez et al. (2009)], http://www3.dsi.uminho.pt/pcortez/wine/).

We have 13 variable kinds here: 11 features, 1 target variable, and 1 other variable (characteristic about wine color).

# 3. Create DB & Collections

I've decided to name my DB wineDB.
I want to have 3 collections: wines (includes wine_id and color), red_wines (includes IDs and characteristics for red wines), white_wines (includes IDs and characteristics for white wines)

### 1 Step
I've decided to watch at first what dbs do i have

![GitHub Image](/MongoDB/images/create1.png)


### 2 Step
I've created my DB wineDB

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

