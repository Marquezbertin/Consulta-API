import requests


def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        country_data = response.json()
        # Supondo que estamos interessados apenas no primeiro resultado
        country_info = country_data[0]
        return country_info
    elif response.status_code == 404:
        print(f"O país '{country_name}' não foi encontrado na API.")
        return None
    else:
        print("Erro ao obter informações do país:", response.status_code)
        return None


# Função para imprimir as opções disponíveis para consulta
def print_options():
    print("Opções disponíveis para consulta:")
    print("1. Códigos Geográficos")
    print("2. Localização Geográfica")
    print("3. Informações sobre Fronteiras")
    print("4. Área e Limites")
    print("5. Informações de Demografia")
    print("6. Informações Econômicas")
    print("7. Informações sobre Idiomas")
    print("8. Informações sobre Fusos Horários")
    print("9. Informações sobre Bandeiras")
    print("10. Informações sobre Nomes")
    print("11. Informações sobre Abreviações")
    print("12. Informações sobre Blocos Regionais")


# Pedir nome do usuário
user_name = input("Por favor, digite o seu nome: ")
print(f"OK, {user_name}, qual país você gostaria de ter informações?")

# Loop de interação com o usuário
while True:
    country_name = input("Digite o nome de um país (ou 'sair' para encerrar): ")

    if country_name.lower() == "sair":
        print(
            f"Ok, {user_name}, obrigado por utilizar nossa consulta. Por favor, avalie nosso serviço."
        )
        while True:
            try:
                rating = int(
                    input(
                        "Por favor, avalie nosso serviço de consulta (de 0 a 5, onde 0 é muito ruim e 5 é a nota máxima): "
                    )
                )
                if 0 <= rating <= 5:
                    break
                else:
                    print("Por favor, insira uma nota entre 0 e 5.")
            except ValueError:
                print("Por favor, insira um número válido.")

        print(f"Obrigado por sua avaliação, {user_name}!")
        break

    country_info = get_country_info(country_name)

    if country_info:
        while True:
            print(f"{user_name}, informações sobre {country_info['name']['common']}:")
            print_options()

            while True:
                try:
                    choice = int(
                        input("Escolha o número da informação que deseja consultar: ")
                    )
                    if 1 <= choice <= 12:
                        break
                    else:
                        print("Por favor, escolha uma opção válida.")
                except ValueError:
                    print("Por favor, insira um número válido.")

            if choice == 1:
                print(
                    "Códigos Geográficos:",
                    country_info["cca2"],
                    ",",
                    country_info.get("callingCodes", "N/A"),
                    ",",
                    country_info["region"],
                    ",",
                    country_info["subregion"],
                )
            elif choice == 2:
                print("Localização Geográfica:", country_info["latlng"])
            elif choice == 3:
                print(
                    "Informações sobre Fronteiras:", country_info.get("borders", "N/A")
                )
            elif choice == 4:
                print(
                    "Área e Limites:",
                    country_info["area"],
                    ",",
                    country_info.get("borders", "N/A"),
                )
            elif choice == 5:
                if "demographics" in country_info:
                    print(
                        "Informações de Demografia:",
                        country_info["demographics"]["population"],
                        ",",
                        country_info["demographics"]["populationDensity"],
                        ",",
                        country_info["demographics"]["age"]["median"],
                        ",",
                        country_info["demographics"]["lifeExpectancy"]["total"],
                        ",",
                        country_info["demographics"]["birthRate"],
                        ",",
                        country_info["demographics"]["deathRate"],
                    )
                else:
                    print("Informações de Demografia: N/A")
            elif choice == 6:
                print(
                    "Informações Econômicas:",
                    country_info["currencies"].get("primary"),
                    ",",
                    country_info["currencies"].get("iso4217Code", "N/A"),
                    ",",
                    country_info["currencies"].get("symbol", "N/A"),
                    ",",
                    country_info["currencies"].get("conversionRate", "N/A"),
                )
            elif choice == 7:
                print(
                    "Informações sobre Idiomas:", ", ".join(country_info["languages"])
                )
            elif choice == 8:
                print("Informações sobre Fusos Horários:", country_info["timezones"])
            elif choice == 9:
                print("Informações sobre Bandeiras:", country_info["flags"])
            elif choice == 10:
                print(
                    "Informações sobre Nomes:",
                    country_info["name"].get("common", "N/A"),
                    ",",
                    country_info["name"].get("native", "N/A"),
                )
            elif choice == 11:
                print("Informações sobre Abreviações:", country_info["altSpellings"])
            elif choice == 12:
                print(
                    "Informações sobre Blocos Regionais:",
                    country_info.get("regionalBlocs", "N/A"),
                )

            while True:
                option = input(
                    f"{user_name}, deseja consultar outra informação deste país? (sim/não): "
                ).lower()
                if option == "sim":
                    break
                elif option == "não":
                    break
                else:
                    print("Por favor, responda 'sim' ou 'não'.")

            if option == "não":
                break

    while True:
        option = input(
            f"{user_name}, deseja consultar informações de outro país? (sim/não): "
        ).lower()
        if option == "sim":
            break
        elif option == "não":
            print(
                f"Ok, {user_name}, obrigado por utilizar nossa consulta. Por favor, avalie nosso serviço."
            )
            while True:
                try:
                    rating = int(
                        input(
                            "Por favor, avalie nosso serviço de consulta (de 0 a 5, onde 0 é muito ruim e 5 é a nota máxima): "
                        )
                    )
                    if 0 <= rating <= 5:
                        break
                    else:
                        print("Por favor, insira uma nota entre 0 e 5.")
                except ValueError:
                    print("Por favor, insira um número válido.")

            print(f"Obrigado por sua avaliação, {user_name}!")
            exit()
        else:
            print("Por favor, responda 'sim' ou 'não'.")
