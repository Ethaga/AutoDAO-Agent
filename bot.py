import os
from dotenv import load_dotenv
from web3 import Web3
from openai import OpenAI

# Load API keys from secrets.env
load_dotenv("secrets.env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
INFURA_URL = os.getenv("INFURA_URL")

# Connect to Ethereum via Infura
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
if web3.is_connected():
    print("✅ Connected to Ethereum network")
else:
    print("❌ Failed to connect to Ethereum")
    exit()

# Connect to OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# Example request to OpenAI
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an AI assistant for blockchain queries."},
        {"role": "user", "content": "Hello, can you tell me the latest Ethereum block number?"}
    ]
)

print("🤖 OpenAI says:", response.choices[0].message.content)

# Get latest Ethereum block
latest_block = web3.eth.block_number
print(f"⛓ Latest Ethereum block: {latest_block}")
