import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
transaction_file = "transaction_data.csv"
purchase_file = "purchase_behaviour.csv"

df_transactions = pd.read_csv(transaction_file)
df_purchase = pd.read_csv(purchase_file)

# Merge transaction data with customer demographics
df = df_transactions.merge(df_purchase, on="LYLTY_CARD_NBR", how="left")

# Identify the top 3 most profitable products
product_sales = df.groupby(["PROD_NBR", "PROD_NAME"])["TOT_SALES"].sum().reset_index()
top_products = product_sales.sort_values(by="TOT_SALES", ascending=False).head(3)

# Identify the most loyal customer segment (highest spending group)
customer_spending = df.groupby(["LYLTY_CARD_NBR", "LIFESTAGE", "PREMIUM_CUSTOMER"])["TOT_SALES"].sum().reset_index()
loyal_customer_segment = customer_spending.groupby(["LIFESTAGE", "PREMIUM_CUSTOMER"])["TOT_SALES"].sum().reset_index()
top_loyal_segment = loyal_customer_segment.sort_values(by="TOT_SALES", ascending=False).head(1)

# Display findings
print("Top 3 Most Profitable Products:")
print(top_products)

print("\nMost Loyal Customer Segment:")
print(top_loyal_segment)

# Visualization
plt.figure(figsize=(10,5))
sns.barplot(data=top_products, x="PROD_NAME", y="TOT_SALES", palette="viridis")
plt.xticks(rotation=45, ha="right")
plt.title("Top 3 Most Profitable Products")
plt.ylabel("Total Sales ($)")
plt.show()

plt.figure(figsize=(8,4))
sns.barplot(data=loyal_customer_segment.sort_values(by="TOT_SALES", ascending=False), x="LIFESTAGE", y="TOT_SALES", hue="PREMIUM_CUSTOMER")
plt.xticks(rotation=45, ha="right")
plt.title("Total Sales by Customer Segment")
plt.ylabel("Total Sales ($)")
plt.legend(title="Customer Type")
plt.show()
