from sqlalchemy import create_engine
import logging

# Logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_to_database(dataframes, table_names, db_uri):
    try:
        logger.info("Loading data into the database")
        engine = create_engine(db_uri)
        for df, table in zip(dataframes, table_names):
            df.to_sql(table, engine, if_exists='replace', index=False)
        logger.info("Data successfully loaded into the database")
    except Exception as e:
        logger.error(f"Error during data loading: {e}")
        raise

