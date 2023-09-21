from pyspark.sql import SparkSession


def spark_session():
    return SparkSession.builder.getOrCreate()


def create_products(spark):
    prod = spark.createDataFrame([
        (1, 'product1'),
        (2, 'product2'),
        (3, 'product3')
    ], schema='prod_id integer, prod_name string')
    prod.createOrReplaceTempView('products')
    return prod


def create_categories(spark):
    categories = spark.createDataFrame([
        (1, 'category1'),
        (2, 'category2'),
        (3, 'category3')
    ], schema='cat_id integer, cat_name string')
    categories.createOrReplaceTempView('categories')
    return categories


def create_product_category(spark):
    prod_cat = spark.createDataFrame([
        (1, 1, 1, 'description1'),
        (2, 1, 2, 'description2'),
        (3, 2, 2, 'description3'),
    ], schema='prod_cat_id integer, prod_id integer, cat_id integer, \
        prod_cat_description string')
    prod_cat.createOrReplaceTempView('prod_cat')
    return prod_cat
