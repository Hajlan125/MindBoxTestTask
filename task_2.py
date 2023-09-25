from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()

    products = spark.read.csv('data/product.csv', header=True)
    categories = spark.read.csv('data/category.csv', header=True)
    product_to_category = spark.read.csv('data/product_to_category.csv', header=True)

    task = products.join(product_to_category, products.id == product_to_category.product_id, 'left') \
            .join(categories, product_to_category.category_id == categories.id, 'left') \
            .select(['product', 'category']).show()