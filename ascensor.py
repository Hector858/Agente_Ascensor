#INSTRUCCIONES
#INGRESE LA UBICACIÓN Piso1/Piso2/Piso3 
#Ingrese el estado O/1 según corresponda, donde 0 significa activado y 1 significa quieto

from cmath import cos


def ascendor():
    #inicializando el ascensor
    #0 indica activado y 1 indica quieto
    estado_objetivo = {'Piso1': '0', 'Piso2': '0', 'Piso3': '0'}#El esatdo que se quiere llevar
    costo=0
    
    piso = input("Ingrese la ubicación del asensor: ") #se ingresa las opciones de piso1/piso2/piso3
    estado=input("Ingrese el estado: " + piso+" ") #se ingresa el estado del asensor 0/1
    otro_piso=input("Ingrese el otro piso que quiere llegar: ")#Debe de ingresar el piso1/piso2/piso3
    otro_estado=input("Ingrese el otro estado: ")#se ingresa el estado del asensor 0/1
    otro_piso2=input("Ingrese otro piso que quiere llegar: ")#Debe de ingresar el piso1/piso2/piso3
    otro_estado2=input("Ingrese otro estado: ")#se ingresa el estado del asensor 0/1
    print("Meta Deseada:" + str(estado_objetivo))
    
    if piso== 'Piso1':
        #localización Piso1 esta quieto
        print("El asensor esta en el Piso 1: ")
        if estado == '1':#1 indica que esta quieto
            print("El asensor esta quieto")
            estado_objetivo['Piso1']='0'#cambia el esatdo de quieto a activado
            costo+=1#incrementa el costo por activar el ascensor
            print("Asensor moviendose del piso 1")
            print("costo actual: "+str(costo))
            
            if otro_piso=='Piso2':
                #El Piso al que se dirije el ascensor
                print("Subiendo al piso 2")
                if otro_estado=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso2']='0'#cambia el esatdo de quieto a activado
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#Si el estado es 0 indica que esta activo
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            elif otro_piso=='Piso3':
                #El Piso al que se dirije el ascensor
                print("Subiendo al piso 3")
                if otro_estado=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso3']='0'#cambia el esatdo de quieto a activado
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#0 indica que esta activo
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            else: #Caso cuando no se pone niguna de las dos anteriores
                print("El asensor no se movio ya que se escogio el mismo piso")
                print("No realiza acciones. Consto actual: "+str(costo))
            if otro_piso2=='Piso2':
                #El Piso al que se dirije el ascensor
                print("Subiendo al piso 2")
                if otro_estado2=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso2']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#Si el estado es 0 indica que esta activo
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            elif otro_piso2=='Piso3':
                #El Piso al que se dirije el ascensor
                print("Subiendo al piso 3")
                if otro_estado2=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso3']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#0 indica que esta activo
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            else: #Caso cuando no se pone niguna de las dos anteriores
                print("El asensor no se movio ya que se escogio el mismo piso")
                print("No realiza acciones. Consto actual: "+str(costo))
        if estado == '0':
            #Cuando el ascensor esta astivo en el Piso
            print("El asensor esta en movimiento")
            if otro_piso == 'Piso2':#El Piso al que se dirije el ascensor
                print("Subiendo derecho a al piso 2")
                if otro_estado=='1':#si esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso2']='0'#cambia el esatdo de quieto a activado
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#si esta activo
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            elif otro_piso=='Piso3':#El Piso al que se dirije el ascensor
                print("Subiendo derecho a al piso 3")
                if otro_estado=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso3']='0'#cambia el esatdo de quieto a activado
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            else:
                print("El asensor no se movio ya que se escogio el mismo piso")
                print("No realiza acciones. Consto actual: "+str(costo))
            if otro_piso2=='Piso2':
                #El Piso al que se dirije el ascensor
                print("Subiendo al piso 2")
                if otro_estado2=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso2']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#Si el estado es 0 indica que esta activo
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            elif otro_piso2=='Piso3':
                #El Piso al que se dirije el ascensor
                print("Subiendo al piso 3")
                if otro_estado2=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso3']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#0 indica que esta activo
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo)) 
            else:#Caso cuando no se pone niguna de las dos anteriores
                print("No se mueve" + str(costo))
                print("Se eleigio el mismo piso") 
    elif piso== 'Piso2':
        print("El asensor esta en el Piso 2: ")
        if estado == '1':#1 indica que esta quieto
            print("El asensor esta quieto")
            estado_objetivo['Piso1']='0'#cambia el estado de quieto a activado
            costo+=1#incrementa el costo por activar el ascensor
            print("Asensor moviendose del piso 2")
            print("costo actual: "+str(costo))
            
            if otro_piso=='Piso1':
                #El Piso al que se dirije el ascensor
                print("Bajando al piso 1")
                if otro_estado=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso1']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else: #Si el estado es 0 indica que esta activo
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            elif otro_piso=='Piso3':
                #El Piso al que se dirije el ascensor
                print("Subiendo al piso 3")
                if otro_estado=='1': #1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso3']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa costo por subir y abrir las puertas
                    print("costo actual: "+str(costo))
                else:#0 indica que esta activo
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            else: #Caso cuando no se pone niguna de las dos anteriores
                print("El asensor no se movio ya que se escogio el mismo piso")
                print("No realiza acciones. Consto actual: "+str(costo))
            if otro_piso2=='Piso1':
                #El Piso al que se dirije el ascensor
                print("Bajando al piso 1")
                if otro_estado2=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso1']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else: #Si el estado es 0 indica que esta activo
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            elif otro_piso2=='Piso3':
                #El Piso al que se dirije el ascensor
                print("Subiendo al piso 3")
                if otro_estado2=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso3']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else: #0 indica que esta activo
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            else: #Caso cuando no se pone niguna de las dos anteriores
                print("El asensor no se movio ya que se escogio el mismo piso")
                print("No realiza acciones. Consto actual: "+str(costo))
        if estado == '0':
            #Cuando el ascensor esta astivo en el Piso
            print("El asensor esta en movimiento")
            if otro_piso == 'Piso1':#El Piso al que se dirije el ascensor
                print("Bajando derecho al piso 1")
                if otro_estado=='1':#si esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso1']='0'
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else: #0 indica que esta activo
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            elif otro_piso=='Piso3':
            #El Piso al que se dirije el ascensor
                print("Subiendo derecho a al piso 3")
                if otro_estado=='1':#1 indica que esta quieto 
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa el costo al subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso3']='0'
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else: #si esta activo
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            else:#Caso cuando no se pone niguna de las dos anteriores
                print("No se mueve" + str(costo))
                print(costo)
                print("Se eleigio el mismo piso")  
            if otro_piso2 == 'Piso1': #El Piso al que se dirije el ascensor
                print("Bajando derecho al piso 1")
                if otro_estado2=='1':#si esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso1']='0'
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#0 indica que esta activo
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            elif otro_piso2=='Piso3':
                #El Piso al que se dirije el ascensor
                print("Subiendo derecho a al piso 3")
                if otro_estado=='1':#1 indica que esta quieto 
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa el costo al subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso3']='0'
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else: #si esta activo
                    print("Llego al piso 3 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            else:#Caso cuando no se pone niguna de las dos anteriores
                print("No se mueve" + str(costo))
                print("Se eleigio el mismo piso")    
    else:
        #localización Piso3 esta quieto
        print("El asensor esta en el Piso 3: ")
        if estado == '1':#1 indica que esta quieto
            print("El asensor esta quieto")
            estado_objetivo['Piso1']='0'#cambia el estado de quieto a activado
            costo+=1#incrementa el costo por activar el ascensor
            print("Asensor moviendose del piso 3")
            print("costo actual: "+str(costo))
            
            if otro_piso=='Piso1':
                #El Piso al que se dirije el ascensor
                print("Bajando al piso 1")
                if otro_estado=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso1']='0'#incrementa costo por subir
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else: #Si el estado es 0 indica que esta activo
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            elif otro_piso=='Piso2':
                #El Piso al que se dirije el ascensor
                print("Bajando al piso 2")
                if otro_estado=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso2']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#0 indica que esta activo
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            else: #Caso cuando no se pone niguna de las dos anteriores
                print("El asensor no se movio ya que se escogio el mismo piso")
                print("No realiza acciones. Consto actual: "+str(costo))
            if otro_piso2=='Piso1':
                #El Piso al que se dirije el ascensor
                print("Bajando al piso 1")
                if otro_estado2=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso1']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#Si el estado es 0 indica que esta activo
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            elif otro_piso2=='Piso2':
                #El Piso al que se dirije el ascensor
                print("Bajando al piso 2")
                if otro_estado2=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso2']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#0 indica que esta activo
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            else: #Caso cuando no se pone niguna de las dos anteriores
                print("El asensor no se movio ya que se escogio el mismo piso")
                print("No realiza acciones. Consto actual: "+str(costo))
        if estado == '0':
            #Cuando el ascensor esta astivo en el Piso
            print("El asensor esta en movimiento")
            if otro_piso == 'Piso1':#El Piso al que se dirije el ascensor
                print("Bajando derecho al piso 1")
                if otro_estado=='1':#si esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subi
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso1']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#si esta activo
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1##incrementa costo por subir
                    print("costo actual: "+str(costo))
            elif otro_piso=='Piso2':#El Piso al que se dirije el ascensor
                print("Bajando derecho al piso 2")
                if otro_estado=='1':#si esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso2']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#si esta activo
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            else: #Caso cuando no se pone niguna de las dos anteriores
                print("No se mueve" + str(costo))
                print(costo)
                print("Se eleigio el mismo piso")  
            if otro_piso2 == 'Piso1':#El Piso al que se dirije el ascensor
                print("Bajando derecho al piso 1")
                if otro_estado2=='1':#si esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1##incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso1']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#si esta activo
                    print("Llego al piso 1 y se abren las puertas")
                    costo+=1##incrementa costo por sub
                    print("costo actual: "+str(costo))
            elif otro_piso2=='Piso2':#El Piso al que se dirije el ascensor
                print("Bajando derecho al piso 2")
                if otro_estado2=='1':#1 indica que esta quieto
                    print("Activando las puertas del asensor")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
                    estado_objetivo['Piso2']='0'#cambia el estado de quieto a activado
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa el costo por activar el asensor
                    print("costo actual: "+str(costo))
                else:#si esta activo
                    print("Llego al piso 2 y se abren las puertas")
                    costo+=1#incrementa costo por subir
                    print("costo actual: "+str(costo))
            else:#Caso cuando no se pone niguna de las dos anteriores
                print("No se mueve" + str(costo))
                print("Se eleigio el mismo piso") 
    
    #terminado el proceso
    print("estado_objetivo: ")
    print(estado_objetivo)#imprime el estado objetivo actualizado
    print("Medición del desempeño: " + str(costo))         
                
    
ascendor()