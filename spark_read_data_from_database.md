# Spark read data from database using JDBC

```python
from pyspark.sql import SparkSession

# Create an entry point to Spark Cluster
spark = SparkSession.builder \
    .appName("MyApp") \
    .config("spark.driver.extraClassPath", "path/to/postgresql-42.2.10.jar")) \
    .master("local[*]") \
    .getOrCreate()

jdbcDF = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://{}:5432/{}".format(HOST_URL, DB_NAME)) \
    .option("query", SQL_QUERY) \
    .option("user", DB_USER) \
    .option("password", DB_PASSWORD) \
    .option("driver", "org.postgresql.Driver") \
    .load()

```
