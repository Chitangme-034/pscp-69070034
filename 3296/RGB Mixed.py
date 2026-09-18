"""RGB"""
def mixColor(c1, c2):
    """Mix two color value"""
    return (c1 + c2) // 2
def mixRGB(r1, g1, b1, r2, g2, b2):
    """Mix two RGB colors"""
    rMix = mixColor(r1, r2)
    bMix = mixColor(b1, b2)
    gMix = mixColor(g1, g2)
    return(rMix, gMix, bMix)
def main():
    """Mixed RGB color"""
    r1, g1, b1 = map(int, input().split())
    r2, g2, b2 = map(int, input().split())
    rMix, gMix, bMix = mixRGB(r1, g1, b1, r2, g2, b2)
    print(rMix, gMix, bMix)
main()
