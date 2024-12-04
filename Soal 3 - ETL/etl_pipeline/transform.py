import pandas as pd
import numpy as np
import logging

# Logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clean_data(sales_df, product_data):
    try:
        logger.info("Cleaning and normalizing data")
        # Fill missing values
        sales_df.fillna({'quantity': 0, 'total_price': 0}, inplace=True)
        sales_df.dropna(subset=['product_id'], inplace=True)
        product_data = pd.DataFrame(product_data).dropna()
        return sales_df, product_data
    except Exception as e:
        logger.error(f"Error during data cleaning: {e}")
        raise

def calculate_metrics(sales_df, product_data):
    try:
        logger.info("Calculating derived metrics")
        merged_df = pd.merge(sales_df, product_data, on='product_id', how='inner')

        # Total revenue per product
        total_revenue = merged_df.groupby('product_name')['total_price'].sum().reset_index()

        # Sales performance by channel
        sales_by_channel = sales_df.groupby('sales_channel')['total_price'].sum().reset_index()

        # Customer purchase frequency
        purchase_frequency = sales_df.groupby('customer_id').size().reset_index(name='purchase_count')

        # Inventory valuation
        inventory_valuation = merged_df.groupby('product_name').apply(
            lambda x: (x['quantity'] * x['base_price']).sum()
        ).reset_index(name='inventory_value')

        return total_revenue, sales_by_channel, purchase_frequency, inventory_valuation
    except Exception as e:
        logger.error(f"Error during metric calculations: {e}")
        raise

