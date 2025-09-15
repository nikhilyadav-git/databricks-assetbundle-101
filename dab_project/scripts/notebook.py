from databricks.connect import DatabricksSession  # this is databricks session

# from pyspark.sql import SparkSession # -> this is pyspark session
# spark = SparkSession.builder.getOrCreate()

spark = DatabricksSession.builder.profile("databricks-playground").remote(
    cluster_id="68fdb3f87ec05372"
).getOrCreate()

spark.sql("SELECT 1").show()
