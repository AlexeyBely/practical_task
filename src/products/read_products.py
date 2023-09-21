from pyspark.sql import SparkSession, DataFrame


def select_products(spark: SparkSession, prod: DataFrame, 
                    catgr: DataFrame, prod_cat: DataFrame) -> DataFrame:
    result = prod.join(prod_cat, prod.prod_id == prod_cat.prod_id, "left"
                       ).join(catgr, catgr.cat_id == prod_cat.cat_id, "left"
                              ).select('prod_name', 'cat_name')
    return result
