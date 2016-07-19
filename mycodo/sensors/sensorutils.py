# coding=utf-8
#
# From https://github.com/mk-fg/sht-sensor


def dewpoint(temperature, humidity):
    dict_tn = dict(water=243.12, ice=272.62) # Table 9
    dict_m = dict(water=17.62, ice=22.46) # Table 9
    'With t and rh provided, does not access the hardware.'
    if t is None: t, rh = self.read_t(), None
    if rh is None: rh = self.read_rh(t)
    t_range = 'water' if t >= 0 else 'ice'
    tn, m = dict_tn[t_range], dict_m[t_range]
    return (
        tn * (math.log(rh / 100.0) + (m * t) / (tn + t))
        / (m - math.log(rh / 100.0) - m * t / (tn + t)) )