# -------------------------------------------------

def update_campo_alunno(lista, matricola, campo, nuovo_valore):
    if matricola not in lista:
        print("Matricola non trovata!")
        return False

    alunno = lista[matricola]

    # Check if the field exists before updating
    if campo in alunno:
        alunno[campo] = nuovo_valore

        # Update modification date ANY time a change happens
        alunno["data_modificazione"] = get_timestamp()

        print(f"{campo} aggiornato con successo!")
        return True
    else:
        print(f"Campo '{campo}' non trovato!")
        return False