def f1(x, y):
    y = y.lower()
    if y == "defended":
        if y in x:
            return 1
        else:
            return 0
    else:
        return 0
        
def f2(x, y):
    y = y.lower()
    if y == "left alone":
        if y in x:
            return 1
        else:
            return 0
    else:
        return 0
        
def f3(x, y):
    y = y.lower()
    if y == "beaten":
        if y in x:
            return 1
        else:
            return 0
    else:
        return 0
        
def f4(x, y):
    y = y.lower()
    if y == "edge":
        if y in x:
            return 1
        else:
            return 0
    else:
        return 0
        
def f5(x, y):   # Caught
    y = y.lower()
    if y == "caught":
        if "OUT" in x:
            for word in ["catch", "caught", "caught out", "what a catch", "into the lap", "in the air"]:
                if word in x:
                    return 1
        return 0
    else:
        return 0

def f6(x, y):   # Runout
    y = y.lower()
    if y == "runout":
        if "OUT" in x:
            for word in ["runout", "run out", "running"]:
                if word in x:
                    return 1
        return 0
    else:
        return 0

def f7(x, y):   # Stumped
    y = y.lower()
    if y == "stumped":
        if "OUT" in x:
            for word in ["stumped", "stumping"]:
                if word in x:
                    return 1
        return 0
    else:
        return 0
        
def f8(x, y):   # Bowled
    y = y.lower()
    if y == "bowled":
        if "OUT" in x:
            for word in ["gets hit", "bowled", "leg stump"]:
                if word in x:
                    return 1
        return 0
    else:
        return 0
        
def f9(x, y):   # LBW
    y = y.lower()
    if y == "lbw":
        if "OUT" in x:
            for word in ["lbw", "LBW", "leg before wicket"]:
                if word in x:
                    return 1
        return 0
    else:
        return 0
        
def f10(x, y):
    y = y.lower()
    if y == "boundary_scored_by_batsman":
        if "FOUR" in x or "SIX" in x:
            return 1
    return 0
    
def f11(x, y):
    y = y.lower()
    if y == "runs_by_batsman":
        if "1 run" in x or "2 runs" in x:
            return 1
    return 0
    
def f12(x, y):
    y = y.lower()
    if y == "boundary_scored_extras":
        if "no ball" in x.lower():
            if "FOUR" in x or "SIX" in x:
                return 1
    return 0
    
def f13(x, y):
    y = y.lower()
    if y == "runs_by_extras":
        if "wide" in x or "no ball" in x.lower():
            return 1
    return 0
    
def f14(x, y):
    y = y.lower()
    if y == "catch_dropped":
        if "in the air" in x and "dropped" in x:
            return 1
        for word in ["dropped catch", "catch dropped"]:
            if word in x:
                return 1
    return 0
    
def f15(x, y):
    y = y.lower()
    if y == "stumping_missed":
        if "OUT" not in x:
            if "stumping" in x or "stumped" in x:
                return 1
    return 0
    
def f16(x, y):
    y = y.lower()
    if y == "runout_missed":
        if "runout" in x and "OUT" not in x:
            return 1
    return 0
    
def f17(x, y):
    y = y.lower()
    if y == "bouncer":
        if "bouncer" in x:
            return 1
    return 0
    
def f18(x, y):
    y = y.lower()
    if y == "yorker":
        if "yorker" in x:
            return 1
    return 0
    
def f19(x, y):
    y = y.lower()
    if y == "overthrow":
        if "overthrow" in x:
            return 1
    return 0
    
def f20(x, y):
    y = y.lower()
    if y == "great_save":
        if "great save" in x:
            return 1
    return 0
    
def f21(x, y):
    y = y.lower()
    if y == "poor_fielding":
        if "poor fielding" in x:
            return 1
    return 0
    
def f22(x, y):
    y = y.lower()
    if y == "free hit":
        if "free hit" in x:
            return 1
    return 0
