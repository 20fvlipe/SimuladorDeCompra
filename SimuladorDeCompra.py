import os 
os.system("cls")

IVA = 0.19
nombre_producto = input("ingrese nombre del producto\n").title()
try:
    precio = int(input("ingrese precio\n"))
    cantidad = int(input("ingrese cantidad\n"))
    dia = input("ingrese dia de la semana que realizará la compra\n").lower()
    if dia == "lunes" : 
        descuento = 0.05
    elif dia == "martes":
        descuento = 0.08
    elif dia == "miercoles":
        descuento = 0.10
    elif dia == "jueves":
        descuento = 0.12
    elif dia == "viernes":
        descuento = 0.15
    elif dia == "sabado":
        descuento = 0.18
    elif dia == "domingo":
        descuento = 0.20
    else:
        print("el dia detallado no existe")
    
    subtotal = precio * cantidad
    valor_descuento = subtotal * descuento
    valor_provisorio = subtotal - valor_descuento
    
    if cantidad > 5:
        descuento_cantidad = 0.05
    else:
        descuento_cantidad = 0
    
    valor_descuento_dia = valor_provisorio * descuento_cantidad
    valor_total_descuentos = valor_provisorio - valor_descuento_dia
    valor_iva = valor_total_descuentos * IVA
    valor_total_pagar = valor_total_descuentos + valor_iva
    
    print(f"Nombre del producto: {nombre_producto}")
    print(f"Precio: ${precio}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${subtotal}")
    print(f"Descuento por día: ${valor_descuento}")
    print(f"Descuento por cantidad: ${valor_descuento_dia}")
    print(f"Total neto: ${valor_total_descuentos}")
    print(f"IVA: ${valor_iva}")
    print(f"Total final: ${valor_total_pagar}")
    
except:
    print("dato debe ser numerico")
    