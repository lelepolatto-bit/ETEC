imovel = input("Seu imóvel é comercial, casa ou apartamento? ").lower()
consumo = float(input("Qual o seu consumo mensal, em m³, de água? "))

match imovel:
    case "comercial":
        print("Tarifa comercial aplicada - consulte o plano corporativo.")

    case "apartamento" if consumo < 10:
        print("Consumo econômico - excelente controle de água!")

    case "apartamento" | "casa" if consumo <= 25:
        print("Consumo moderado - dentro do padrão residencial.")

    case _:
        print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")
