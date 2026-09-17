def silver_to_gold(spark):

    silver_df = spark.table(
        "sales_catalog.retailpro.silver_orders"
    )

    gold_df = (
        silver_df
        .groupBy("product")
        .agg(
            {
                "quantity": "sum",
                "amount": "sum"
            }
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

    gold_df.write \
        .format("delta") \
        .mode("overwrite") \
        .saveAsTable(
            "sales_catalog.retailpro.gold_product_sales"
        )

    return "Gold transformation completed"


if __name__ == "__main__":
    print(silver_to_gold(spark))