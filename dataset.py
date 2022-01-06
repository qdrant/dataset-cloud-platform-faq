import pandas as pd


dataset_names = [
    'aws_processed.csv',
    'yandex_cloud_processed.csv',
    'gcp_processed.csv',
    'hetzner_processed.csv',
    'ibm_processed.csv',
    'azure_processed.csv'
]

dfs = []
for dataset_name in dataset_names:
    path = 'data/processed/' + dataset_name
    df = pd.read_csv(path, index_col=0)
    dfs.append(df)

concat_df = pd.concat(dfs)
print(concat_df.shape)
concat_df.to_json('data/faq.csvl', index=True, lines=True, orient="records")