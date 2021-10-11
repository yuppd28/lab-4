from dataclasses import dataclass

@dataclass
class TypeOfMainAssets:
    code: int
    type: str
    kg: str
    price: float

@dataclass
class MoveOfMainAssets:
    code: int
    name: str
    price2: float
    price10: float
    price14: float
    price24: float
    month: str

type_array = []
type_array.append(TypeOfMainAssets(10, "Яловичина", "кг.", 25.5))
type_array.append(TypeOfMainAssets(20, "Свинина", "кг.", 26.5))
type_array.append(TypeOfMainAssets(30, "Сало", "кг.", 15.0))

move_array = []
move_array.append(MoveOfMainAssets(10, "Яловичина", 25.5, 23.5, 30.8, 23.7, "серпень"))
move_array.append(MoveOfMainAssets(20, "Свинина", 25.0, 25.5, 25.5, 25.7, "серпень"))
move_array.append(MoveOfMainAssets(30, "Сало", 14.4, 14.5, 14.5, 14.5, "серпень"))
move_array.append(MoveOfMainAssets(10, "Яловичина", 23.5, 24.0, 24.0, 24.5, "вересень"))
move_array.append(MoveOfMainAssets(20, "Свинина", 25.5, 26.0, 26.3, 26.5, "вересень"))
move_array.append(MoveOfMainAssets(30, "Сало", 14.5, 14.6, 14.8, 15.0, "вересень"))
move_array.append(MoveOfMainAssets(10, "Яловичина", 25.0, 25.0, 25.5, 25.5, "жовтень"))
move_array.append(MoveOfMainAssets(20, "Свинина", 26.6, 26.8, 27.0, 27.4, "жовтень"))
move_array.append(MoveOfMainAssets(30, "Сало", 15.5, 15.5, 15.6, 16.0, "жовтень"))

def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Ринкові ціни на продукти по місяцях"
    with names and values'''

    print("Код: {code}, Назва: {name}, Ринкові ціни на 2 число місяця,грн.: {price2}, Ринкові ціни на 10 число місяця,грн.: {price10} Ринкові ціни на 14 число місяця, грн: {price14}, Ринкові ціни на 24 число місяця, грн: {price24}, Місяць:{month}"
          .format(code=moveOfMainAssets.code, name=moveOfMainAssets.name, price2=moveOfMainAssets.price2, price10=moveOfMainAssets.price10,
                 price14=moveOfMainAssets.price14, price24=moveOfMainAssets.price24, month=moveOfMainAssets.month))              
for data in move_array:
     printMoveOfMainAssets(data)
     
def printTypeOfMainAssets(typeOfMainAssets):
    '''printTypeOfMainAssets function prints
    "Довідник товару"
    with names and values'''

    print("Код: {code}, Назва товару: {type}, Одиниця виміру: {kg}, Роздрібна ціна, грн: {price}"
        .format(code=typeOfMainAssets.code, type=typeOfMainAssets.type, kg=typeOfMainAssets.kg, price=typeOfMainAssets.price))

for data in type_array:
    printTypeOfMainAssets(data)