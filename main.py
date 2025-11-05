authors = [
    {
        'id':1,
        'name':'Agatha',
        'surname': 'Cristie'
    },
    {
        'id': 2,
        'name': 'Umberto',
        'surname': 'Eco'
    },
    {
        'id':3,
        'name': 'Vladimir',
        'surname': 'Nabokov'
    }
]
id_counter = 3
while True:
    print("Pasirinkite, ką norite daryti")
    print("1. Peržiūrėti autoriu sarasa")
    print("2. Pridėti naują autoriu")
    print("3. Redaguoti autoriu")
    print("4. Ištrinti autoriu")
    print("5. Išeiti iš autoriu saraso")

    option = input()
    match option:
        case '1':
            print("jus pasirinkote perziureti autoriu sarasa")
            for item in authors:
                print(item)
        case '2':
            print("jus pasirinkote itraukti nauja autoriu i sarasa")
            print("iveskite autoriaus varda")
            manufacturer = input()
            print("iveskite autoriaus pavarde")
            type = input()
            id_counter +=1
            item = {'id':id_counter, "name": name , "surname": surname }
            authors.append(item)

        case '3':
            print("jus pasirinkote redaguoti autoriu")
            print("irasykite prekes id kuria norite redaguoti")
            edit_id = input()
            for i, item in enumerate(author):
                if str(item['id']) == edit_id:
                    print(item)
                    print("iveskite autoriaus varda")
                    author[i]['name'] = input()
                    print("iveskite autoriaus pavarde")
                    author[i]['type'] = input()
        case '4':
            print("jus pasirinkote pasalinti autoriu")
            print("irasykite autoriaus id kuria norite salinti")
            del_id = input()
            for item in author:
                if str(item['id']) == del_id:
                    author.remove(item)
                    break
        case '5':
            print("jus pasirinkote iseiti")
            break


