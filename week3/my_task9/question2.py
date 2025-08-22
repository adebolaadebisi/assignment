# Nigerian Currency Converter (Very Advanced)
# Ask for inputs
amount_naira = float(input("Enter amount in Naira (₦): "))
rate_usd = float(input("Enter exchange rate to US Dollars ($): "))
rate_gbp = float(input("Enter exchange rate to British Pounds (£): "))
# Control flow check (to make sure rates are valid)
if rate_usd <= 0 or rate_gbp <= 0:
    print("Exchange rates must be greater than zero!")
else:
    # Conversion
    usd = amount_naira / rate_usd
    gbp = amount_naira / rate_gbp
    # Print neatly formatted table with escape sequences
    print("\n\tNIGERIAN CURRENCY CONVERTER")
    print("\t------------------------------------")
    print(f"\tAmount in Naira:    ₦{amount_naira:,.2f}")
    print(f"\tEquivalent in USD:  ${usd:,.2f}")
    print(f"\tEquivalent in GBP:  £{gbp:,.2f}")
    print("\t------------------------------------")