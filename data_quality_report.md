# Data Quality Report

## Data Quality Issues Addressed

| Cleaning Step | Data Quality Dimension | Reason |
|---|---|---|
| Removed exact duplicate rows | Uniqueness | Dropped duplicate records so each record is represented once without inflating totals. |
| Removed extra whitespace and converted region text to Title Case | Consistency | Standardized region text so variations of the same region name are treated consistently in aggregations. |
| Filled missing category values via product lookup table | Completeness | Restored missing category values based on existing product-to-category relationships without dropping rows. |
| Imputed missing profit values via category-wise mean margin | Completeness | Populated missing profit values using calculated category-level margins while preserving the dataset rows. |

---

## Analysis of Data Quality Dimensions

### Addressed Dimensions

- **Uniqueness:** Identified and removed exact duplicate records using `df.drop_duplicates()`.

- **Consistency:** Standardized region names using `.str.strip()` and `.str.title()` so different textual representations of the same region are treated consistently.

- **Completeness:** Filled missing `category` values using the product-category lookup and missing `profit_inr` values using category-wise mean profit margins.

### Unaddressed Dimensions

- **Accuracy:** No external source was used to verify whether the recorded values were factually correct.

- **Timeliness:** No date or time-related transformation or validation was required by the cleaning steps.

- **Validity:** No separate validation of data values against predefined valid-value rules was performed.

- **Relevance:** No records or fields were removed based on their relevance to the analysis.

## Schema Validation

The `validate_schema()` function was used to verify that all required columns were present in the cleaned dataset. A deliberately broken copy was also tested to confirm that missing required columns were correctly detected and reported.