import psycopg2

c_name = ""
c_email = ""
c_phone = 0
coutner = 0

def wyswietl():

    postgreSQL_select_Query = "select * from customers"

    cursor.execute(postgreSQL_select_Query)
    customers_records = cursor.fetchall()
    for row in customers_records:
        print("customers_Id = ", row[0], )
        print("customers_name = ", row[1])
        print("customers_email = ", row[2])
        print("customers_phone  = ", row[3], "\n")

def dodaj():
    postgres_insert_query = """ INSERT INTO customers(name, email, phone)
        VALUES (%s,%s,%s)"""
    print("Podaj name")
    c_name = input()
    print("Podaj email")
    c_email = input()
    print("Podaj phone")
    c_phone = int(input())
    record_to_insert = [(c_name, c_email, c_phone)]
    for i in record_to_insert:
        cursor.execute(postgres_insert_query, i)

        connection.commit()
        count = cursor.rowcount
    print(count, "Record inserted successfully \
        into publisher table")

def modyfikuj():
    print("Który id chcesz modyfikowac")
    c_id = int(input())
    print("Co chcesz modyfikowac?")
    mod = input()
    if(mod == "name"):
        print("podaj nowy name")
        c_name = input()
        sql_update_query = """Update customers set \
                name = %s where customers_id = %s"""
        cursor.execute(sql_update_query,
                       (c_name,
                        c_id))
    elif(mod == "email"):
        print("podaj nowy email")
        c_email = input()
        sql_update_query = """Update customers set \
                        email = %s where customers_id = %s"""
        cursor.execute(sql_update_query,
                       (c_email,
                        c_id))
    elif(mod == "phone"):
        print("podaj nowy phone")
        c_phone = input()
        sql_update_query = """Update customers set \
                                phone = %s where customers_id = %s"""
        cursor.execute(sql_update_query,
                       (c_phone,
                        c_id))
    connection.commit()
    count = cursor.rowcount
    print(count, "Record Updated successfully ")

def usuwanie():
    print("Ktory rekord usunac?")
    c_id = int(input())
    sql_delete_query = """Delete from customers\
           where customers_id = %s"""
    cursor.execute(sql_delete_query, (c_id,))
    connection.commit()
    count = cursor.rowcount
    print(count, "Record deleted successfully ")


try:
    connection = psycopg2.connect(user="hdngjorw",
                                  password="a5sYySccwO_j9O9op-_J4W-S7ewXYX9A",
                                  host="snuffleupagus.db.elephantsql.com",
                                  port="5432",
                                  database="hdngjorw")

    cursor = connection.cursor()
    koniec = "nie"
    while (koniec != 'tak'):
        print("Baza danych customers zostala polaczona")
        print("1 - Wyswietlanie rekordow tablicy")
        print("2 - Dodawanie nowego rekordu")
        print("3 - Modyfikowanie rekordu")
        print("4 - Usuwanie rekordu")
        print("Co chcesz zrobic? Wybierz numer:")

        wybor = int(input())

        if wybor == 1:
            wyswietl()
        elif wybor == 2:
            dodaj()
        elif wybor == 3:
            modyfikuj()
        elif wybor == 4:
            usuwanie()
        else:
            print("Zla opcja wyboru")
        print("Czy koniec?")
        koniec = input("")

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
# closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")