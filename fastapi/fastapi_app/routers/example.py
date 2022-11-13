from fastapi import APIRouter

router = APIRouter(
    prefix = "/example",
    tags = ["example"]
)

@router.get('/endpoint1')
def getAdsData():
    return 'welcome to test'
