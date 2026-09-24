import pandas as pd
import numpy as np

def clean_and_build_abt(filepath):
    # Load dataset
    df = pd.read_csv(filepath)
    
    # 1. Clean missing fees
    df['Airport_fee'] = df['Airport_fee'].fillna(0)
    
    # 2. Revenue & Fee Impact Metrics
    df['total_fees'] = (
        df['cbd_congestion_fee'] + 
        df['congestion_surcharge'] + 
        df['Airport_fee'] + 
        df['mta_tax'] + 
        df['improvement_surcharge']
    )
    
    df['net_revenue'] = df['total_amount'] - df['total_fees']
    df['net_revenue_per_hour'] = (df['net_revenue'] / df['duration_min']) * 60
    df['fee_impact_pct'] = (df['total_fees'] / df['total_amount']) * 100
    
    # 3. Engineer Fare & Trip Length Thresholds
    df['fare_tier'] = pd.qcut(df['total_amount'], q=3, labels=['Low Fare', 'Medium Fare', 'High Fare'])
    df['trip_length_tier'] = pd.qcut(df['trip_distance'], q=3, labels=['Short Trip', 'Medium Trip', 'Long Trip'])
    
    # 4. Engineer Traffic Congestion Levels
    speed_bins = [0, 8, 15, 100]
    speed_labels = ['Heavy Traffic', 'Moderate Traffic', 'Light Traffic']
    df['congestion_level'] = pd.cut(df['speed_mph'], bins=speed_bins, labels=speed_labels)
    
    return df

if __name__ == "__main__":
    input_path = '../data/NYC_Taxi_Cleaned_Analysis_Ready.csv'
    output_path = '../data/NYC_Taxi_ABT.csv'
    
    print("Building ABT...")
    abt_df = clean_and_build_abt(input_path)
    abt_df.to_csv(output_path, index=False)
    print(f"ABT successfully saved to {output_path}")