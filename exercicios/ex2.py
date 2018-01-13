minutos = float(input('Digite os minutos: '))
if minutos < 200:
    tarifa = 0.20 * minutos
    print('\nSua conta é> %.2f '%tarifa)
else:
    if minutos <= 400:
        tarifa = 0.18 * minutos
        print('\nSua conta é> %.2f '%tarifa)
    else:
        tarifa = 0.15 * minutos
        print('\nSua conta é> %.2f '%tarifa)
    if minutos > 800:
        tarifa = 0.08 * minutos
        print('\nSua conta é> %.2f '%tarifa)

