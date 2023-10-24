def countMatches(items,ruleKey,ruleValue):
    count = 0
    if ruleKey == "type":
        arrValue = 0
    elif ruleKey == "color":
        arrValue = 1
    elif ruleKey == "name":
        arrValue = 2

    for subArr in items:
        if ruleValue == subArr[arrValue]:
            count += 1
        
    return count


items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
countMatches(items,ruleKey,ruleValue)


items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
countMatches(items,ruleKey,ruleValue)