# Write a function to convert USD to INR.

def converter(usd_val):
    inr_val = usd_val * 90
    print(usd_val, 'USD =',inr_val, 'INR')
    
converter(158)