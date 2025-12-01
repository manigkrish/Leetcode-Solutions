SELECT
  patient_id,
  patient_name,
  conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%'        -- DIAB1 at the start
   OR conditions LIKE '% DIAB1%';     -- DIAB1 after a space (i.e. another condition before it)