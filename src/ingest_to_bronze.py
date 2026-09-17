from pyspark.sql import Row


def ingest_to_bronze(spark):
    data = [
        Row(order_id=1001, customer_id=101, product="Laptop", quantity=1, amount=55000),
        Row(order_id=1002, customer_id=102, product="Mouse", quantity=2, amount=1500),
        Row(order_id=1003, customer_id=101, product="Keyboard", quantity=1, amount=2500),
        Row(order_id=1004, customer_id=103, product="Monitor", quantity=1, amount=12000),
        Row(order_id=1005, customer_id=104, product="Laptop", quantity=1, amount=60000),
    ]

    df = spark.createDataFrame(data)

    df.write \
        .format("delta") \
        .mode("overwrite") \
        .saveAsTable("sales_catalog.retailpro.bronze_orders")

    return "Bronze ingestion completed"