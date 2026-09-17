def bronze_to_silver(spark):

    bronze_df = spark.table(
        "sales_catalog.retailpro.bronze_orders"
    )

    silver_df = (
        bronze_df
        .filter("order_id IS NOT NULL")
        .filter("customer_id IS NOT NULL")
        .filter("quantity > 0")
        .filter("amount > 0")
    )

    silver_df.write \
        .format("delta") \
        .mode("overwrite") \
        .saveAsTable(
            "sales_catalog.retailpro.silver_orders"
        )

    return "Silver transformation completed"


if __name__ == "__main__":
    print(bronze_to_silver(spark))