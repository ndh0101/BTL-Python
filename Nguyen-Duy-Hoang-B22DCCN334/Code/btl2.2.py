import pandas as pd

df = pd.read_csv('results.csv')

# Chọn các cột cần tính toán
numeric_columns = df.columns[5:]
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df.fillna(0, inplace=True)

# Tính toán cho toàn giải
overall_stats = {
    'Name': 'all',
    'Median': [df[col].median() for col in numeric_columns],
    'Mean': [df[col].mean() for col in numeric_columns],
    'Std': [df[col].std() for col in numeric_columns],
}

# Tính toán cho từng đội
team_stats = []
teams = df['Team'].unique()
for team in teams:
    team_data = df[df['Team'] == team]
    team_stats.append({
        'Name': team,
        'Median': [team_data[col].median() for col in numeric_columns],
        'Mean': [team_data[col].mean() for col in numeric_columns],
        'Std': [team_data[col].std() for col in numeric_columns],
    })

# Kết hợp dữ liệu
results = [overall_stats] + team_stats
result_df = pd.DataFrame(results)
result_df.insert(0, 'Index', range(len(result_df)))
final_result_df = pd.DataFrame(columns=['Index', 'Name'])
for col in numeric_columns:
    final_result_df[f'Median of {col}'] = [result_df.iloc[i]['Median'][i] for i in range(len(result_df))]
    final_result_df[f'Mean of {col}'] = [result_df.iloc[i]['Mean'][i] for i in range(len(result_df))]
    final_result_df[f'Std of {col}'] = [result_df.iloc[i]['Std'][i] for i in range(len(result_df))]
final_result_df['Index'] = result_df['Index']
final_result_df['Name'] = result_df['Name']
final_result_df.to_csv('results2.csv', index=False)