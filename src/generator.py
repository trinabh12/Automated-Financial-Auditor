import pandas as pd
from faker import Faker
import random
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class DataGenerator:


    def __init__(self, seed=42):
        self.fake = Faker()
        Faker.seed(seed)
        random.seed(seed)
        self.internal_df = None
        self.gateway_df = None

    def create_base_data(self, n=100):
        logging.info(f"Generating {n} base records...")
        data = [{
            "TX_ID": f"TXN-{1000 + i}",
            "Customer": self.fake.name(),
            "Amount": round(random.uniform(50.0, 500.0), 2),
            "Date": self.fake.date_between(start_date='-30d', end_date='today')
        } for i in range(n)]

        self.internal_df = pd.DataFrame(data)
        return self.internal_df

    def inject_chaos(self, missing_count=5, mismatch_count=3, duplicate_count=2):
        if self.internal_df is None:
            raise ValueError("Base data not generated. Call create_base_data() first.")

        logging.info("Injecting controlled chaos into Gateway data...")
        df_messy = self.internal_df.copy()

        drop_indices = random.sample(range(len(df_messy)), missing_count)
        df_messy = df_messy.drop(drop_indices)

        mismatch_indices = df_messy.index[:mismatch_count]
        df_messy.loc[mismatch_indices, 'Amount'] = df_messy.loc[mismatch_indices, 'Amount'] - 0.50

        dup_rows = df_messy.iloc[-duplicate_count:]
        df_messy = pd.concat([df_messy, dup_rows], ignore_index=True)

        self.gateway_df = df_messy
        return self.gateway_df

    def save_to_csv(self, folder="data"):
        if not os.path.exists(folder):
            os.makedirs(folder)

        int_path = os.path.join(folder, "internal_records.csv")
        gat_path = os.path.join(folder, "gateway_statement.csv")

        self.internal_df.to_csv(int_path, index=False)
        self.gateway_df.to_csv(gat_path, index=False)

        logging.info(f"Files exported to {folder}/")