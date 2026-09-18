## Initial Observations & Notable Findings

### 1. Dataset Scale & Volume
* **High Transaction Volume:** The dataset contains approximately **3.94 million records** (3,946,698 trips), providing a dense sample size across all operating hours and zones.
* **Granularity:** Records capture individual trip events containing pickup/drop-off spatial identifiers, metered timestamps, fee breakdowns, and payment attributes.

### 2. Missing Value Patterns & Structural Gaps
* **Selective Null Clustering:** Over **757,000 records** exhibit missing values in `Airport_fee`. This pattern corresponds structurally to standard street hails that do not originate at airport terminals (JFK or LaGuardia).
* **Unrecorded Operational Expenses:** The dataset does not track vehicle operating expenditures (fuel consumption, vehicle depreciation, maintenance, or vehicle lease fees).
* **Payment-Restricted Tipping:** Recorded values in `tip_amount` are populated exclusively for credit card transactions (`payment_type == 1`); cash tips are systematically unrecorded and register as zero.

### 3. Data Representation & Formatting Nuances
* **Nominal IDs as Numeric Types:** Identifier columns (such as `VendorID`, `RatecodeID`, and `PULocationID`) are stored as numeric/floating-point types rather than categorical variables.
* **Distorted Descriptive Statistics:** Standard summary methods calculate mathematically invalid metrics for identifiers (e.g., a mean `VendorID` of 1.79) and render counts in scientific notation (`3.946698e+06`).
* **Variable Interaction Sensitivity:** Mathematical comparisons and column-wise evaluations are sensitive to mixed column data types across boolean flags and numeric values.

### 4. Revenue Composition, Anomalies & Fee Friction
* **Negative Charge Artifacts:** Descriptive statistics (`.min()` and `.describe()`) revealed negative values in certain fee columns, specifically `extra` (-17.39), `mta_tax` (-7.81), and `cbd_congestion_fee` (-0.75). These anomalies logically represent meter dispute corrections, refunded fares, or system resets rather than standard operational trips.
* **Gross Revenue Inflation:** Raw fare totals (`total_amount`) reflect gross passenger charges rather than driver take-home earnings due to stacked regulatory surcharges (`cbd_congestion_fee`, `congestion_surcharge`, `mta_tax`, `improvement_surcharge`, and `Airport_fee`).
* **Fee Disproportionality:** Flat-rate fees represent a significantly higher proportion of short, low-fare trips compared to long-distance fares.
* **Congestion and Speed Variance:** Wide spreads in `duration_min` and `speed_mph` indicate substantial traffic friction across different pickup locations, suggesting that trip distance alone does not reliably predict trip duration or occupied earning efficiency.