# Telecom-Customer-Churn-Prediction

Overview
It is the Telecom Churn dataset from IBM (Can be sourced from Kaggle):
https://www.kaggle.com/datasets/ylchang/telco-customer-churn-1113
Customer Churn is basically a customer leaving a service provider for various
reasons like better services from the competitors, relocation etc. The
predictive model should give us the risk of a customer leaving the service
provider to enable any preventive action.
The dataset has a variety of information related to each customer in the
dataset as features. The dataset has over 7000 entries and
customer/subscription/demographic information in six files as independent
variables and 1 churn indicator.
The dataset information is contained in 6 files (extracted from 6 Database
Tables by provider) – split based on categories.
1. Telco_customer_churn.xlsx (Basic Data)
Add On Information: The following files are from an updated version of
the data set, with more information related to the customer. Some of the
information in the Basic Data above is repeated in the below tables, but the
below tables also have additional information. We would merge these
tables and remove any duplicate features.)
2. Telco_customerchurn_demographics.xlsx
3. Telco_customerchurn_location.xlsx
4. Telco_customerchurn_population.xlsx
5. Telco_customerchurn_services.xlsx
6. Telco_customerchurn_status.xlsx
Below are the details of each feature, in the above datasets, grouped by
categories, for better understanding.
https://community.ibm.com/community/user/businessanalytics/blogs/steve
n-macko/2019/07/11/telco-customer-churn-1113
Demographics
1. CustomerID: A unique ID that identifies each customer.
2. Count: A value used in reporting/dashboarding to sum up the number
of customers in a filtered set.
3. Gender: The customer’s gender: Male, Female
4. Age: The customer’s current age, in years, at the time the fiscal
quarter ended.
5. Senior Citizen: Indicates if the customer is 65 or older: Yes, No
6. Married: Indicates if the customer is married: Yes, No
7. Dependents: Indicates if the customer lives with any dependents:
Yes, No. Dependents could be children, parents, grandparents, etc.
8. Number of Dependents: Indicates the number of dependents that
live with the customer.
Location
1. CustomerID: A unique ID that identifies each customer.
2. Count: A value used in reporting/dashboarding to sum up the number
of customers in a filtered set.
3. Country: The country of the customer’s primary residence.
4. State: The state of the customer’s primary residence.
5. City: The city of the customer’s primary residence.
6. Zip Code: The zip code of the customer’s primary residence.
7. Lat Long: The combined latitude and longitude of the customer’s
primary residence.
8. Latitude: The latitude of the customer’s primary residence.
9. Longitude: The longitude of the customer’s primary residence.
Population
1. ID: A unique ID that identifies each row.
2. Zip Code: The zip code of the customer’s primary residence.
3. Population: A current population estimate for the entire Zip Code
area.
Services
1. CustomerID: A unique ID that identifies each customer.
2. Count: A value used in reporting/dashboarding to sum up the number
of customers in a filtered set.
3. Quarter: The fiscal quarter that the data has been derived from (e.g.
Q3).
4. Referred a Friend: Indicates if the customer has ever referred a
friend or family member to this company: Yes, No
5. Number of Referrals: Indicates the number of referrals to date that
the customer has made.
6. Tenure in Months: Indicates the total amount of months that the
customer has been with the company by the end of the quarter
specified above.
7. Offer: Identifies the last marketing offer that the customer accepted,
if applicable. Values include None, Offer A, Offer B, Offer C, Offer D,
and Offer E.
8. Phone Service: Indicates if the customer subscribes to home phone
service with the company: Yes, No
9. Avg Monthly Long Distance Charges: Indicates the customer’s
average long distance charges, calculated to the end of the quarter
specified above.
10. Multiple Lines: Indicates if the customer subscribes to multiple
telephone lines with the company: Yes, No
11. Internet Service: Indicates if the customer subscribes to
Internet service with the company: No, DSL, Fiber Optic, Cable.
12. Avg Monthly GB Download: Indicates the customer’s average
download volume in gigabytes, calculated to the end of the quarter
specified above.
13. Online Security: Indicates if the customer subscribes to an
additional online security service provided by the company: Yes, No
14. Online Backup: Indicates if the customer subscribes to an
additional online backup service provided by the company: Yes, No
15. Device Protection Plan: Indicates if the customer subscribes
to an additional device protection plan for their Internet equipment
provided by the company: Yes, No
16. Premium Tech Support: Indicates if the customer subscribes
to an additional technical support plan from the company with reduced
wait times: Yes, No
17. Streaming TV: Indicates if the customer uses their Internet
service to stream television programing from a third party provider:
Yes, No. The company does not charge an additional fee for this
service.
18. Streaming Movies: Indicates if the customer uses their
Internet service to stream movies from a third party provider: Yes, No.
The company does not charge an additional fee for this service.
19. Streaming Music: Indicates if the customer uses their Internet
service to stream music from a third party provider: Yes, No. The
company does not charge an additional fee for this service.
20. Unlimited Data: Indicates if the customer has paid an
additional monthly fee to have unlimited data downloads/uploads: Yes,
No
21. Contract: Indicates the customer’s current contract type:
Month-to-Month, One Year, Two Year.
22. Paperless Billing: Indicates if the customer has chosen
paperless billing: Yes, No
23. Payment Method: Indicates how the customer pays their bill:
Bank Withdrawal, Credit Card, Mailed Check
24. Monthly Charge: Indicates the customer’s current total
monthly charge for all their services from the company.
25. Total Charges: Indicates the customer’s total charges,
calculated to the end of the quarter specified above.
26. Total Refunds: Indicates the customer’s total refunds,
calculated to the end of the quarter specified above.
27. Total Extra Data Charges: Indicates the customer’s total
charges for extra data downloads above those specified in their plan,
by the end of the quarter specified above.
28. Total Long Distance Charges: Indicates the customer’s total
charges for long distance above those specified in their plan, by the
end of the quarter specified above.
Status
1. CustomerID: A unique ID that identifies each customer.
2. Count: A value used in reporting/dashboarding to sum up the number
of customers in a filtered set.
3. Quarter: The fiscal quarter that the data has been derived from (e.g.
Q3).
4. Satisfaction Score: A customer’s overall satisfaction rating of the
company from 1 (Very Unsatisfied) to 5 (Very Satisfied).
5. Satisfaction Score Label: Indicates the text version of the score (1-
5) as a text string.
6. Customer Status: Indicates the status of the customer at the end of
the quarter: Churned, Stayed, or Joined
7. Churn Label: Yes = the customer left the company this quarter. No
= the customer remained with the company. Directly related to Churn
Value.
8. Churn Value: 1 = the customer left the company this quarter. 0 =
the customer remained with the company. Directly related to Churn
Label.
9. Churn Score: A value from 0-100 that is calculated using the
predictive tool IBM SPSS Modeler. The model incorporates multiple
factors known to cause churn. The higher the score, the more likely
the customer will churn.
10. Churn Score Category: A calculation that assigns a Churn
Score to one of the following categories: 0-10, 11-20, 21-30, 31-40,
41-50, 51-60, 61-70, 71-80, 81-90, and 91-100
11. CLTV: Customer Lifetime Value. A predicted CLTV is calculated
using corporate formulas and existing data. The higher the value, the
more valuable the customer. High value customers should be
monitored for churn.
12. CLTV Category: A calculation that assigns a CLTV value to one
of the following categories: 2000-2500, 2501-3000, 3001-3500, 3501-
4000, 4001-4500, 4501-5000, 5001-5500, 5501-6000, 6001-6500, and
6501-7000.
13. Churn Category: A high-level category for the customer’s
reason for churning: Attitude, Competitor, Dissatisfaction, Other, Price.
When they leave the company, all customers are asked about their
reasons for leaving. Directly related to Churn Reason.
14. Churn Reason: A customer’s specific reason for leaving the
company. Directly related to Churn Category.

The main problem to solve is, giving the telecom company a way to know if
a particular customer or a set of customers are having a higher probability
of moving out (churn) / port out from the current telecom service provider.
If the company is made aware of such customers, they could take actions to
try and retain their business. Customer retention is an important factor in
the Telecom Industry. Customers especially corporate ones can have a major
impact on revenues and margins.
Based on various demographic, account related info, usage of services the
model must predict if the customer has a likelihood of moving out or not.
Apart from retaining customers, this will also help increase the customer
satisfaction in general due to affirmative action by the company. The model
should also preferably give areas where the service provider must work on
to retain the customers.
