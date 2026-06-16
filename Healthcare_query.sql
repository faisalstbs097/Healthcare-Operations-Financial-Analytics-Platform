CREATE DATABASE healthcare_db;

USE healthcare_db;
SELECT USER();

SHOW TABLES;

-- Q1. Total Patients
SELECT COUNT(DISTINCT pat_id) AS total_patients
FROM patn;

-- Q2. Total Visits
SELECT COUNT(DISTINCT refr_no) AS total_visits
FROM vist;

-- Q3. Total Revenue
SELECT SUM(bill_amt) AS total_revenue
FROM billing;

-- Q4. Average Bill Amount
SELECT AVG(bill_amt) AS avg_bill
FROM billing;

-- Q5. Top 10 Most Common Diagnoses
SELECT dig_des,
       COUNT(*) AS diagnosis_count
FROM diag1
GROUP BY dig_des
ORDER BY diagnosis_count DESC
LIMIT 10;

-- Q6. Top 10 Most Common Treatments
SELECT trtm_des,
       COUNT(*) AS treatment_count
FROM treatment
GROUP BY trtm_des
ORDER BY treatment_count DESC
LIMIT 10;

-- Q7. Patients Having More Than 5 Visits
SELECT pat_id,
       COUNT(*) AS visit_count
FROM vist
GROUP BY pat_id
HAVING COUNT(*) > 5;

-- Q8. Visits Having Multiple Diagnoses
SELECT refr_no,
       COUNT(*) AS diagnosis_count
FROM diag1
GROUP BY refr_no
HAVING COUNT(*) > 1;

-- Q9. Visits Having Multiple Treatments
SELECT refr_no,
       COUNT(*) AS treatment_count
FROM treatment
GROUP BY refr_no
HAVING COUNT(*) > 1;

-- Q10. Revenue By Visit Type
SELECT v.vtype_des,
       SUM(b.bill_amt) AS revenue
FROM billing b
JOIN vist v
ON b.refr_no = v.refr_no
GROUP BY v.vtype_des
ORDER BY revenue DESC;

-- Q11. Revenue By Room
SELECT v.rom_id,
       SUM(b.bill_amt) AS revenue
FROM billing b
JOIN vist v
ON b.refr_no = v.refr_no
GROUP BY v.rom_id
ORDER BY revenue DESC;

-- Q12. Diagnosis Affecting Highest Number Of Patients
SELECT d.dig_des,
       COUNT(DISTINCT v.pat_id) AS patient_count
FROM diag1 d
JOIN vist v
ON d.refr_no = v.refr_no
GROUP BY d.dig_des
ORDER BY patient_count DESC
LIMIT 1;

-- Q13. Patients Above Average Billing
SELECT pat_id,
       SUM(bill_amt) AS total_bill
FROM billing
GROUP BY pat_id
HAVING SUM(bill_amt) >
(
    SELECT AVG(patient_bill)
    FROM
    (
        SELECT SUM(bill_amt) AS patient_bill
        FROM billing
        GROUP BY pat_id
    ) t
);

-- Q14. Second Highest Bill Amount
SELECT MAX(bill_amt)
FROM billing
WHERE bill_amt <
(
    SELECT MAX(bill_amt)
    FROM billing
);

-- Q15. Top 5 Revenue Generating Patients
WITH patient_revenue AS
(
    SELECT pat_id,
           SUM(bill_amt) AS revenue
    FROM billing
    GROUP BY pat_id
)
SELECT *
FROM patient_revenue
ORDER BY revenue DESC
LIMIT 5;

-- Q16. Patients Above Average Revenue
WITH patient_revenue AS
(
    SELECT pat_id,
           SUM(bill_amt) AS revenue
    FROM billing
    GROUP BY pat_id
)
SELECT *
FROM patient_revenue
WHERE revenue >
(
    SELECT AVG(revenue)
    FROM patient_revenue
);

-- Q17. Rank Patients By Revenue
SELECT pat_id,
       SUM(bill_amt) AS revenue,
       RANK() OVER
       (
           ORDER BY SUM(bill_amt) DESC
       ) AS revenue_rank
FROM billing
GROUP BY pat_id;

-- Q18. Dense Rank Patients By Revenue
SELECT pat_id,
       SUM(bill_amt) AS revenue,
       DENSE_RANK() OVER
       (
           ORDER BY SUM(bill_amt) DESC
       ) AS revenue_rank
FROM billing
GROUP BY pat_id;

-- Q19. Row Number For Patients
SELECT pat_id,
       SUM(bill_amt) AS revenue,
       ROW_NUMBER() OVER
       (
           ORDER BY SUM(bill_amt) DESC
       ) AS row_num
FROM billing
GROUP BY pat_id;

-- Q20. Top 3 Revenue Generating Patients
WITH patient_revenue AS
(
    SELECT pat_id,
           SUM(bill_amt) AS revenue
    FROM billing
    GROUP BY pat_id
)
SELECT *
FROM patient_revenue
ORDER BY revenue DESC
LIMIT 3;

-- Q21. Top 5 Revenue Generating Visits
SELECT refr_no,
       SUM(bill_amt) AS revenue
FROM billing
GROUP BY refr_no
ORDER BY revenue DESC
LIMIT 5;

-- Q22. Monthly Revenue Trend
SELECT MONTH(bill_date) AS month_no,
       SUM(bill_amt) AS revenue
FROM billing
GROUP BY MONTH(bill_date)
ORDER BY month_no;

-- Q23. Highest Revenue Month
SELECT MONTH(bill_date) AS month_no,
       SUM(bill_amt) AS revenue
FROM billing
GROUP BY MONTH(bill_date)
ORDER BY revenue DESC
LIMIT 1;

-- Q24. Running Revenue Total
SELECT bill_date,
       bill_amt,
       SUM(bill_amt)
       OVER
       (
           ORDER BY bill_date
       ) AS running_revenue
FROM billing;

-- Q25. Previous Bill Amount (LAG)
SELECT bill_date,
       bill_amt,
       LAG(bill_amt)
       OVER
       (
           ORDER BY bill_date
       ) AS previous_bill
FROM billing;

-- Q26. Next Bill Amount (LEAD)
SELECT bill_date,
       bill_amt,
       LEAD(bill_amt)
       OVER
       (
           ORDER BY bill_date
       ) AS next_bill
FROM billing;