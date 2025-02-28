import pandas as pd
from apyori import apriori

dataset=pd.read_csv('GroceryDataset.csv',header=None)

transactions = dataset.apply(lambda x: x.astype(str)).values.tolist()


rules=list(apriori(transactions,min_support=0.003,min_confidence=0.2,min_lift=3,min_length=2))

print(f"there are {list(rules)} relations derived")


output=[{'Rule':'->'.join(list(rule.items)),
         'support': rule.support,
         'confidence':stat.confidence,
         'lift':stat.lift}for rule in rules for stat in rule.ordered_statistics]

for r in output:
    print(f"Rule:{r['Rule']}\nsupport:{r['support']}\nconfidence:{r['confidence']}\nlift:{r['lift']}\n{'='*40}")

