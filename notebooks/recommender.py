import pandas as pd

perf = pd.read_csv("data/07_scheme_performance.csv")

def recommend_funds(risk_level):

    funds = perf[
        perf['risk_grade'].str.lower()
        == risk_level.lower()
    ]

    top_funds = (
        funds.sort_values(
            'sharpe_ratio',
            ascending=False
        )
        [['scheme_name', 'sharpe_ratio']]
        .head(3)
    )

    return top_funds


risk = input(
    "Enter Risk Level (Low/Moderate/Moderately High/High/Very High): "
    
)

print(
    recommend_funds(risk)
)
