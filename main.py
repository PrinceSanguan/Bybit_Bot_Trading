import ccxt
import api_keys

# Initialize Bybit with ccxt
bybit = ccxt.bybit({
    'apiKey': api_keys.api_key,
    'secret': api_keys.api_secret,
    'enableRateLimit': True
})

print(bybit.fetch_balance())