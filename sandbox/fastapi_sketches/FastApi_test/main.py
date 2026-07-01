from fastapi import FastAPI, HTTPException, status
from fastapi.responses import Response

app = FastAPI()



BALANCE = {}

@app.get("/totalBalance")
def get_total_balance():
    return {"total_balance": sum(BALANCE.values())}

@app.get("/wallets/{wallet_name}/balance")
def get_wallet_balance(wallet_name: str):
    if wallet_name not in BALANCE:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Wallet '{wallet_name}' not found"
        )
    return {"wallet": wallet_name, "balance": BALANCE[wallet_name]}




@app.post("/wallets/{name}")
def create_wallet(name: str, initital_balance: float = 0):

    if name in BALANCE:
        raise HTTPException(
            status_code=400,
            detail=f"Wallet '{name}' already exists"
            )
    
    BALANCE[name] = initital_balance