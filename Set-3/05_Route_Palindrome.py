import re


def is_route_palindrome(description):
    hubs = [code.upper() for code in re.findall(r"[A-Za-z]+", description)]
    left = 0
    right = len(hubs) - 1
    while left < right:
        if hubs[left] != hubs[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    routes = ["DEL -> MUM -> HYD -> mum -> del", "DEL, MUM, HYD, CHE", "BLR / HYD / BLR", ""]
    for route in routes:
        print(f"{route!r}: {is_route_palindrome(route)}")
