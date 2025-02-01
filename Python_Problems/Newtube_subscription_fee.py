def calculate_subscription_fee(duration, plan_type, device_limit):
    if duration <= 0:
        return "Invalid subscription duration"
    
    if 1 <= duration <= 3:
        monthly_fee = 50
    elif 4 <= duration <= 6:
        monthly_fee = 45
    elif duration >= 7:
        monthly_fee = 40
    
    total_fee = duration * monthly_fee
    
    if plan_type == 1:  
        total_fee += 100  
    elif plan_type == 2:  
        total_fee *= 0.85  

    if device_limit == 1:  
        total_fee *= 0.95  

    return int(total_fee)
duration = int(input())
plan_type = int(input())
device_limit = int(input())
print(calculate_subscription_fee(duration, plan_type, device_limit))
