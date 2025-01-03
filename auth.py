from fastapi import APIRouter, Depends, HTTPException
import httpx
from fastapi.security import OAuth2PasswordBearer
from .config import GOOGLE_CLIENT_ID, GITHUB_CLIENT_ID

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()

@router.post("/google")
async def google_login(code: str):
    # Handle Google OAuth authentication here
    pass

@router.post("/github")
async def github_login(code: str):
    # Handle GitHub OAuth authentication here
    pass
