import nn
import transform_data
import extract_and_transform
import psql_connection
df = nn.retreive_data_from_api()
df = extract_and_transform.extract_data(df)
df= transform_data.transform_data(df)
psql_connection.load_data_to_azurepsql(df)