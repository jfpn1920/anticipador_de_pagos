import random
ids = []
nombres = []
descripciones = []
valores = []
fechas_registro = []
fechas_vencimiento = []
estados = []
observaciones = []
#-----------------------------------------#
#--|menu_principal_anticipador_de_pagos|--#
#-----------------------------------------#
while True:
    print("menu principal anticipador de pagos")
    print("1) crear pago")
    print("2) editar pago")
    print("3) eliminar pago")
    print("4) buscar pago")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #----------------#
    #--|crear_pago|--#
    #----------------#
    if opcion == "1":
        if len(ids) == 0:
            id_pago = 1
        else:
            id_pago = ids[-1] + 1
        nombre = input("nombre del pago: ")
        descripcion = input("descripción: ")
        valor = float(input("valor del pago: "))
        fecha_registro = input("fecha de registro: ")
        fecha_vencimiento = input("fecha de vencimiento: ")
        estado = input("estado (anticipado, pendiente o pagado): ")
        observacion = input("observación: ")
        ids.append(id_pago)
        nombres.append(nombre)
        descripciones.append(descripcion)
        valores.append(valor)
        fechas_registro.append(fecha_registro)
        fechas_vencimiento.append(fecha_vencimiento)
        estados.append(estado)
        observaciones.append(observacion)
        print("pago registrado correctamente.")
        print("id:", id_pago)
    #-----------------#
    #--|editar_pago|--#
    #-----------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen pagos registrados.")
        else:
            print("editar pago")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | ${valores[i]:.2f} | {estados[i]}")
            id_buscar = int(input("ingrese la id del pago: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | ${valores[posicion]:.2f}")
                nombres[posicion] = input("nuevo nombre: ")
                descripciones[posicion] = input("nueva descripción: ")
                valores[posicion] = float(input("nuevo valor: "))
                fechas_registro[posicion] = input("nueva fecha de registro: ")
                fechas_vencimiento[posicion] = input("nueva fecha de vencimiento: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                print("pago actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-------------------#
    #--|eliminar_pago|--#
    #-------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen pagos registrados.")
        else:
            print("eliminar pago")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | ${valores[i]:.2f} | {estados[i]}")
            id_buscar = int(input("ingrese la id del pago: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del pago")
                print(f"{ids[posicion]} | {nombres[posicion]} | ${valores[posicion]:.2f}")
                respuesta = input("¿desea eliminar este pago? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    descripciones.pop(posicion)
                    valores.pop(posicion)
                    fechas_registro.pop(posicion)
                    fechas_vencimiento.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("pago eliminado correctamente.")
                else:
                    print("el pago no fue eliminado.")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|buscar_pago|--#
    #-----------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen pagos registrados.")
        else:
            print("buscar pago")
            id_buscar = int(input("ingrese la id del pago: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("descripción:", descripciones[posicion])
                print("valor: $", format(valores[posicion], ".2f"))
                print("fecha de registro:", fechas_registro[posicion])
                print("fecha de vencimiento:", fechas_vencimiento[posicion])
                print("estado:", estados[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen pagos registrados.")
        else:
            anticipados = 0
            pendientes = 0
            pagados = 0
            total = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | ${valores[i]:.2f} | {estados[i]}")
                total += valores[i]
                if estados[i].lower() == "anticipado":
                    anticipados += 1
                elif estados[i].lower() == "pendiente":
                    pendientes += 1
                elif estados[i].lower() == "pagado":
                    pagados += 1
            promedio = total / len(ids)
            print("estadísticas anticipador de pagos")
            print("cantidad de pagos:", len(ids))
            print("pagos anticipados:", anticipados)
            print("pagos pendientes:", pendientes)
            print("pagos realizados:", pagados)
            print("valor total registrado: $", format(total, ".2f"))
            print("promedio por pago: $", format(promedio, ".2f"))
            posicion = random.randint(0, len(ids) - 1)
            print("pago seleccionado")
            print("id:", ids[posicion])
            print("nombre:", nombres[posicion])
            print("descripción:", descripciones[posicion])
            print("valor: $", format(valores[posicion], ".2f"))
            print("fecha de registro:", fechas_registro[posicion])
            print("fecha de vencimiento:", fechas_vencimiento[posicion])
            print("estado:", estados[posicion])
            print("observación:", observaciones[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el anticipador de pagos.")
        break
    else:
        print("opción no válida.")