def bronze_to_silver(spark):
    # Read Bronze table
    bronze_df = spark.table(
        "sales_catalog.retailpro.bronze_orders"
    )

    # Clean and validate the data
    silver_df = (
        bronze_df
        .filter("order_id IS NOT NULL")
        .filter("customer_id IS NOT NULL")
        .filter("quantity > 0")
        .filter("amount > 0")
    )

    # Write Silver table
    silver_df.write \
        .format("delta") \
        .mode("overwrite") \
        .saveAsTable(
            "sales_catalog.retailpro.silver_orders"
        )

    return "Silver transformation completed"