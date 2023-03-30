---
title: ER Generic
author: Adhiraj Deshmukh
date: 30-03-2023
---

# Added

- date
- purpose
- conclusion


## Cognitive_Test

- test_id as PK
- subject_id as FK

## MOCA_Test

- test_id as PK
- subject_id as FK
- cognitive_test_id as FK
- Added this as a new table since MOCA is a standard cognitive test

## Blood_Test

- test_id as PK
- subject_id as FK
- region_code as FK

## Brain_MRI_Scan

- Created a Generic Table of Brain Scan
- Added Fields based on CamCan table, since its pretty standard and generic dataset
- region_code

## Brain_Region

- region_code as PK
- region_name

# Remove

## Subject

- Experimenter
- age, sex, education codes
- remove all sorts of codes in general ?

## Cognitive_Test

- GD_code
- MOCA test fields

## CamCan

- Removed this Table to be replaced by a table with more generic name
