#                      DATA CLUSTERING

1. cluster :- Group of similar things.(Grouping of similar data).

   Real-time example :-

   A restaurant wants to group their customers based on:

   How much money they spend.

   How many times they visit.

   | Customer | Total Money Spent | Number of Visits |

   | -------- | ----------------- | ---------------- |

   | A        | 200               | 2                |

   | B        | 1500              | 15               |

   | C        | 300               | 3                |

   | D        | 1200              | 12               |

   | E        | 250               | 2                |

   * What clustering will do ?
     
        . It will automatically group similar customers:

        | Cluster             | Restaurant Action                            |

        | ------------------- | -------------------------------------------- |

        | Low Spending Group  | Send Discount Coupons to make them come more |

        | High Spending Group | Give Loyalty Rewards to keep them happy      |

    * "Clustering helps the restaurant automatically group customers with similar spending and visiting behavior, so they can
    
      target them better.

2. Association :- A connection or relationship between two variables, but it does not mean one causes the other.

   Concept :- Just because two things happen together (increase or decrease together), doesn’t mean one is causing the other.

   Real-time Example :-

   On weekends, both customer visits and dessert sales increase. But dessert sales didn’t cause customer visits. Both happen 
   
   together (may be due to weekend mood).

3. Dependence :- One variable changes because of another. There’s a cause-effect link.

   Concept :- When one thing (output) relies on another thing (input). If you change one, the other definitely changes.

   Real-time Example :-

   Order Total (bill amount) depends on the Number of Items Ordered. 
   
   More items ordered → Higher bill. There is mathematical dependence here.

4. Causation :- One variable directly causes a change in another variable.

   Concept :- There’s a clear cause and effect. You do something → That makes something else happen.

   Real-time Example :- 

   You run a "Buy 1 Get 1 Free" Pizza offer → This directly causes an increase in pizza sales.

   The offer (cause) → Increased sales (effect).

5. Correlation :- A numerical measure (between -1 and 1) showing how strongly two variables move together (positively or 
  
   negatively).

   Concept :- Tells how much two variables are linked in terms of direction and strength, but does not prove cause.

   Real-time Example :- 

   You check correlation between "number of customers" and "total sales", If correlation is 0.9, it means when customer count
   
   increases, sales also increases (strong positive relationship). But it doesn’t prove that customer count is the cause, it just 
   
   shows they move together.

6. Variance :- Variance measures how much a single variable's values spread out from its average (mean).

   Concept :- It tells you whether your data points (values) are close to each other or widely spread out.

   Low variance → Values are close together (more consistent).

   High variance → Values are far apart (more inconsistent).

   Real-time Example :-

   You want to check the variance in daily sales amount for 7 days.

   If your daily sales are like: 1000, 1020, 980, 1010, 995, 1005, 1015 → Low Variance (sales are stable).

   If your daily sales are like: 500, 1500, 700, 2000, 300, 1800, 600 → High Variance (sales are fluctuating a lot)

   So, Variance tells you how stable or unstable your sales are over time.

7. Co-variance :- Covariance measures how two variables change together.

   Concept :- Positive Covariance: Both variables increase together or decrease together.

   Negative Covariance: One variable increases while the other decreases.

   Zero Covariance: No clear relationship between them. 

   Real-time Example :-

   You want to check whether the number of customers and total sales are changing together.

   | Day | Number of Customers | Total Sales (\$) |

   | --- | ------------------- | ---------------- |

   | 1   | 50                  | 500              |

   | 2   | 60                  | 600              |

   | 3   | 70                  | 700              |

   | 4   | 80                  | 800              |

   | 5   | 90                  | 900              |

   As the number of customers increases, the total sales also increases → Positive Covariance.

   Another Example :- If number of customers increases, but total sales decreases (maybe due to discounts or low spending) → This 
   
   would show Negative Covariance.

8. Simpsons Paradox:-  "When a trend is true in smaller groups but changes or reverses when the groups are combined.

   Concept :- Sometimes, when you analyze data separately (by groups), you see one trend (like "A is better than B" in each 
    
   group). But when you combine all the groups together, the trend changes direction or even becomes opposite (now "B looks 
    
   better than A").

   Real-time Example :- 

   Scenario:

   You want to check:

   "Are customers happier with Dine-in or Takeaway?"

   You have data from two branches: Branch A and Branch B . 

   | Branch   | Dine-in Positive Review % | Takeaway Positive Review % | Which looks better? |

   | -------- | ------------------------- | -------------------------- | ------------------- |

   | Branch A | 90% (9 out of 10)         | 80% (8 out of 10)          | Dine-in             |

   | Branch B | 70% (7 out of 10)         | 60% (6 out of 10)          | Dine-in             |

   * In both branches Dine-in is better.

   . But when you combine both branches; 

   | Order Type | Total Positive Reviews | Total Orders | Overall Positive % |

   | ---------- | ---------------------- | ------------ | ------------------ |

   | Dine-in    | 16 out of 30           | 53%          |                    |

   | Takeaway   | 60 out of 80           | 75%          |                    |

   





    







