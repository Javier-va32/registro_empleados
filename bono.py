# Bloque de funcinoes para ingresar datos de sueldo, porcentaje y cálculo de bono

def calcular_bono(sueldo_base, porcentaje_bono):
    bono = sueldo_base * porcentaje_bono
    sueldo_final = sueldo_base + bono
    print ("Cálculo realizado.")
    return bono, sueldo_final
