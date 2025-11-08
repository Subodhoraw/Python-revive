import matplotlib.pyplot as plt
import numpy as np 
sales_data = {'jahn': [5000,3000,5000,6000],
              'sarah': [3000,4000,9000,8000],
              'mike': [2000,50000,4000,9000]
              }

print(f"{'sales range analysis':^50}")
print("="*40)

for person, sales in sales_data.items():
    range_val = max(sales) - min(sales)
    mean_val = np.means(sales)

    print(f"\n{person}:")
    print(f" Range: ${range_val:,}")
    print(f"Average: ${mean_val:,.0f}")
    print(f" Min: ${min(sales):,}")
    print(f"  Max: $ {max(sales):,}")
    

