# Data Quality Report

## Data Quality Issues Addressed

| Cleaning step | Data quality dimension | Reason |
|---|---|---|
| Removed exact duplicate rows | Uniqueness | Duplicate records were removed so that the same record does not appear more than once. |
| Removed extra spaces and converted region names to title case | Consistency | Region names were standardized so that different formats of the same region are treated consistently. |
| Standardized region names to the 9 active canonical region names | Validity | Region values were brought into the expected set of valid canonical region values. |
| Filled missing category values using the product-category lookup | Completeness | Missing category values were filled instead of dropping the affected rows. |
| Filled missing profit values using the category-wise mean profit margin | Completeness | Missing profit values were calculated and filled using the required method. |

## Data Quality Dimensions

The cleaning pipeline directly addressed the following dimensions:

- **Uniqueness:** Exact duplicate records were removed.
- **Consistency:** Region names were standardized.
- **Validity:** Region values were standardized to the expected canonical region names.
- **Completeness:** Missing category and profit values were imputed.

The following dimensions were not directly addressed by the required cleaning steps:

- **Accuracy:** No external source was used to verify whether the recorded values were factually correct.
- **Timeliness:** No date or time-related transformation was required.
- **Relevance:** No records or fields were removed based on their relevance to the dataset.
