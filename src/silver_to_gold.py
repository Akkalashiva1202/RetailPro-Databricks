def silver_to_gold(spark):
    # Read Silver table
    silver_df = spark.table(
        "sales_catalog.retailpro.silver_orders"
    )

    # Create product-level business summary
    gold_df = (
        silver_df
        .groupBy("product")
        .agg(
            {"quantity": "sum", "amount": "sum"}
        )
        .withColumnRenamed(
            "sum(quantity)",
            "total_quantity"
        )
        .withColumnRenamed(
            "sum(amount)",
            "total_revenue"
        )
    )

    # Write Gold table
    gold_df.write \
        .format("delta") \
        .mode("overwrite") \
        .saveAsTable(
            "sales_catalog.retailpro.gold_product_sales"
        )

    return "Gold transformation completed"