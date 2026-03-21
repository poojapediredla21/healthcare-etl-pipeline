-- Total Claims
SELECT COUNT(*) AS total_claims FROM fact_claims;

-- Total Revenue
SELECT SUM(paid_amount) AS total_paid FROM fact_claims;

-- Claims by Insurance Type
SELECT insurance_type, COUNT(*) AS claim_count
FROM fact_claims
GROUP BY insurance_type;

-- Top Providers by Revenue
SELECT provider_id, SUM(paid_amount) AS total_paid
FROM fact_claims
GROUP BY provider_id
ORDER BY total_paid DESC
LIMIT 10;

-- Claim Status Distribution
SELECT claim_status, COUNT(*) AS count
FROM fact_claims
GROUP BY claim_status;

-- Monthly Trends
SELECT 
    strftime('%Y-%m', date_of_service) AS month,
    SUM(paid_amount) AS total_paid
FROM fact_claims
GROUP BY month
ORDER BY month;
