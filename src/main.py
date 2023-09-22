import logging
import math

from geometric import CalcShapes
from products.create_products import (spark_session, create_categories, create_products, 
                                      create_product_category)
from products.read_products import select_products


logger = logging.getLogger(__name__)
        

def main():
    # geometric
    shapes = CalcShapes()
    area = shapes.calc_area(CalcShapes.Shapes.TRIANGLE, 3, 4, 5)
    print(f'area: {area}')
    # products
    spark = spark_session()
    prod = create_products(spark)
    cat = create_categories(spark)
    prod_cat = create_product_category(spark)
    products = select_products(spark, prod, cat, prod_cat)
    products.show()


if __name__ == '__main__':
    main()
