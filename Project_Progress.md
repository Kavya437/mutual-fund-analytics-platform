Day 1:
- Data ingestion completed
- Data overview completed
- Live NAV integration completed

Day 2:
- Data cleaning completed
- SQLite database created
- SQL analysis queries executed

Day 3:
- EDA notebook created
- Multiple charts generated and exported
- Created 15+ visualizations
- Exported chart images
- Performed EDA and insight generation
Day 4:
- Calculated Daily Returns
- Computed CAGR
- Calculated Sharpe Ratio
- Calculated Sortino Ratio
- Calculated Maximum Drawdown
- Generated Alpha & Beta metrics
- Created fund_scorecard.csv
- Generated benchmark comparison chart
## Day 6 – Advanced Analytics & Risk Metrics

### Completed Tasks

1. Historical VaR & CVaR Analysis

   * Calculated daily returns from NAV history.
   * Computed 95% Value at Risk (VaR) and Conditional Value at Risk (CVaR) for all mutual fund schemes.
   * Exported results to `var_cvar_report.csv`.

2. Rolling 90-Day Sharpe Ratio

   * Calculated rolling Sharpe Ratio using 90-day rolling returns and volatility.
   * Analyzed top-performing funds based on Sharpe Ratio.
   * Generated and exported `rolling_sharpe_chart.png`.

3. Investor Cohort Analysis

   * Grouped investors by first transaction year.
   * Calculated average investment amount, total invested amount, and investor count for each cohort.
   * Identified preferred fund categories for each cohort.
   * Exported results to `cohort_analysis_report.csv`.

4. SIP Continuity Analysis

   * Measured average transaction gaps for investors.
   * Classified investors as Active or At Risk using a 35-day threshold.
   * Exported results to `sip_continuity_analysis.csv`.

5. Fund Recommendation Engine

   * Developed `recommender.py`.
   * Implemented risk-based fund recommendations using Sharpe Ratio rankings.
   * Supports Low, Moderate, Moderately High, High, and Very High risk categories.

### Deliverables Generated

* Advanced_Analytics.ipynb
* recommender.py
* var_cvar_report.csv
* cohort_analysis_report.csv
* sip_continuity_analysis.csv
* rolling_sharpe_chart.png
