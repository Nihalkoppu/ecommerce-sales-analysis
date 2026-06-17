-- ============================================
-- E-Commerce Sales Analysis - SQL Queries
-- Tool: MySQL
-- Dataset: Superstore Dataset (Kaggle)
-- ============================================

-- Query 1: Which region generates the most revenue?
SELECT Region, 
       ROUND(SUM(Sales), 2) AS Total_Revenue
FROM orders
GROUP BY Region
ORDER BY Total_Revenue DESC;

-- Result: West($725,457) > East($678,781) > Central($501,239) > South($391,721)

-- -----------------------------------------------

-- Query 2: Which product category has the highest profit margin?
SELECT Category, 
       ROUND(SUM(Profit), 2) AS Total_Profit, 
       ROUND(SUM(Sales), 2) AS Total_Sales, 
       ROUND((SUM(Profit)/SUM(Sales))*100, 2) AS Profit_Margin_Percent 
FROM orders 
GROUP BY Category 
ORDER BY Profit_Margin_Percent DESC;

-- Result: Technology(17.40%) > Office Supplies(17.04%) > Furniture(2.49%)

-- -----------------------------------------------

-- Query 3: What are the monthly sales trends?
SELECT DATE_FORMAT(STR_TO_DATE(Order_Date, '%m/%d/%Y'), '%Y-%m') AS Month, 
       ROUND(SUM(Sales), 2) AS Monthly_Sales 
FROM orders 
GROUP BY Month 
ORDER BY Month ASC;

-- Result: Sales peak in Sep, Nov, Dec every year. Best month: Nov 2017 ($118,447)

-- -----------------------------------------------

-- Query 4: Which customer segment drives the most orders?
SELECT Segment, 
       COUNT(DISTINCT Order_ID) AS Total_Orders, 
       ROUND(SUM(Sales), 2) AS Total_Sales 
FROM orders 
GROUP BY Segment 
ORDER BY Total_Orders DESC;

-- Result: Consumer(2586) > Corporate(1514) > Home Office(909)

-- -----------------------------------------------

-- Query 5: Top 10 products by sales?
SELECT Product_Name, 
       ROUND(SUM(Sales), 2) AS Total_Sales 
FROM orders 
GROUP BY Product_Name 
ORDER BY Total_Sales DESC 
LIMIT 10;

-- Result: Canon imageCLASS 2200 Copier is #1 at $61,599