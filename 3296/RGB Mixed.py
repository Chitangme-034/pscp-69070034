"""RGB Mixed"""
def mix_color(c1, c2):
    """Two color values"""
    return (c1 + c2) // 2
def mix_rgb(color1, color2):
    """Two RGB colors"""
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r_mix = mix_color(r1, r2)
    g_mix = mix_color(g1, g2)
    b_mix = mix_color(b1, b2)
    return r_mix, g_mix, b_mix
def main():
    """Mixed RGB color"""
    color1 = tuple(map(int, input().split()))
    color2 = tuple(map(int, input().split()))
    r_mix, g_mix, b_mix = mix_rgb(color1, color2)
    print(r_mix, g_mix, b_mix)
main()
