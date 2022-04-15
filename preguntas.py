"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    #Get the number of rows: len(df)
    #len(df) me permite conocer la longitud de las filas en la tabla.

    Longitud_tb10=len(tbl0)
    return Longitud_tb10
   


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    #Get the number of rows and columns: df.shape
    #df.shape se usa para saber la cantidad de filas y columnas.

    cantidad_columnas= tbl0.shape[1]

    #como yo solamente necesito saber la cantidad de columnas, necesito ver el segundo elemento de
    #lo que me arroja tbl10.shape: (40,4), entonces uso tb10.shape[1]
    return cantidad_columnas
   


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    #lo primero que debo hacer es ordenar las letras alfabéticamente, uso df.sort_values 
    conteo_columna_c1=tbl0._c1.sort_values()

    #Si queremos calcular el número de veces que cada elemento aparece en una columna de un dataframe pandas
    #podemos recurrir a la función value_counts()     
    #conteo_columna_c1= conteo_columna_c1.value_counts(sort= False)
 
    conteo_columna_c1= conteo_columna_c1.value_counts(sort= False)
    return  conteo_columna_c1



def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    #Una operación groupby implica alguna combinación de dividir el objeto, aplicar una función y combinar los resultados. 
    #Esto se puede usar para agrupar grandes cantidades de datos y calcular operaciones en estos grupos
    #GroupBy.mean. Calcula la media de los grupos, excluyendo los valores faltantes.

    promedio_c2= tbl0.groupby("_c1")["_c2"].mean()   
    return promedio_c2
  


def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    #se usa la misma estructura que la anterior, solo cambio mean por max
    maximo_C2= tbl0.groupby("_c1")["_c2"].max()
    return maximo_C2
  


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    #primero ordeno en mayúsculas los valores de la columna _c4
    columna_c4= [x.upper() for x in tbl1._c4]
    #luego los ordeno (sorted) y quito repetidos (set) para que me salga la lista con valores únicos
    valores_unicos= sorted(set(columna_c4))
    return valores_unicos



def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    #se usa la misma estructura que la anterior, solo cambio max por sum
    suma_c2= tbl0.groupby("_c1")["_c2"].sum()
    return suma_c2
   

def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    #DataFrame.assign(**kwargs) 
    # Assign new columns to a DataFrame. Returns a new object with all original columns in addition to new ones. 
    # Existing columns that are re-assigned will be overwritten.

    columna_nueva=tbl0.assign(suma=tbl0._c0+tbl0._c2)
   
    return columna_nueva
  


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    # pandas.to_datetime ---> Convertir argumento a fecha y hora.
   
    fecha=pd.to_datetime(tbl0._c3,infer_datetime_format=True, errors= "ignore" )
    year=[(x[:4]) for x in fecha]
    columna_nueva=tbl0.assign(year=year)
    
    return columna_nueva
   


def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """

    #filtro las columnas _c1, _c2 de la tabla
    data= tbl0.filter(items=("_c1","_c2"))

    #uso sort_values para ordenar la data tomando como base _c2
    data=data.sort_values("_c2")

    #convierto los valores de _c2 a string
    data["_c2"]= data["_c2"].astype(str)
    
    #DataFrameGroupBy.aggregate ---> Aggregate using one or more operations over the specified axis.
    #pongo.agreggate para añadir un diccionario que agregue a cada valor de _c1 
    #los respectivos valores en _c2, y una los valores con ":"

    nueva_tabla= data.groupby(["_c1"],as_index=False).aggregate({"_c2":":".join})

    #DataFrame.set_index---> Establezca el índice de DataFrame utilizando las columnas existentes.
    #El índice puede reemplazar el índice existente o expandirlo.
    #establesco un  C1 como índice
    
    nueva_tabla.set_index("_c1", inplace=True)
    

    return nueva_tabla
 



def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """

    #ordeno los valores que hacen parte de _c4
    data=tbl1.sort_values("_c4")
    
    #por medio del uso de groupby.aggregate creo un diccionario que contenga los valores de _c4
    #separados por "," y mediante el uso de aggregate.join las une.

    tabla_nueva=data.groupby(["_c0"], as_index=False).aggregate({"_c4":",".join})
        
    return tabla_nueva
    


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    
    col_c5= [(x[1]+":"+str(x[2])) for x in tbl2.values]
    data=tbl2.assign(_c5=col_c5)
    data=data.sort_values("_c5")
    nueva_tabla=data.groupby(("_c0"), as_index=False).aggregate({"_c5":",".join})


    return  nueva_tabla
  


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    #La función pandas.merge nos permite realizar "joins" entre tablas.
    # El join es realizado sobre las columnas o sobre las filas. En el primer caso, 
    # las etiquetas de las filas son ignoradas. En cualquier otro caso (joins realizado entre etiquetas de filas, o entre etiquetas de filas y de columnas), 
    # las etiquetas de filas se mantienen.

    datos= pd.merge(tbl0,tbl2, on="_c0")
    suma_c5b=datos.groupby("_c1")["_c5b"].sum()
    return suma_c5b

