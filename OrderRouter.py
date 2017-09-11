import takeImage
import detectImage
from app import check_kitchen
def recognizeOrder(orderGiven):
    if orderGiven.find('check'):
        check_kitchen()
        return 'going to check kitchen and order things if not available'