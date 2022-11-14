def ver_rg(dado: str) -> bool: 
    rg = ''.join(re.findall('\d', str(dado)))
    return True if (len(rg) == 9) else False