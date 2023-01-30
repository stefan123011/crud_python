import psycopg2



class Api:
    connection = ""
    c_name = ""
    c_email = ""
    c_phone = 0
    cursor = ""

    def __init__(self):
        try:
            self.connection = psycopg2.connect(user="hdngjorw",
                                          password="a5sYySccwO_j9O9op-_J4W-S7ewXYX9A",
                                          host="snuffleupagus.db.elephantsql.com",
                                          port="5432",
                                          database="hdngjorw")

            self.cursor = self.connection.cursor()
            self.start()

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

        finally:
            # closing database connection.
            if self.connection:
                self.cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed")

    def start(self):
        koniec = "nie"
        while (koniec != 'tak'):
            print("Baza danych customers zostala polaczona")
            print("1 - Wyswietlanie rekordow tablicy")
            print("2 - Dodawanie nowego rekordu")
            print("3 - Modyfikowanie rekordu")
            print("4 - Usuwanie rekordu")
            print("Co chcesz zrobic? Wybierz numer:")
            wybor = 0
            wybor = int(input())

            if wybor == 1:
                self.wyswietl()
            elif wybor == 2:
                self.dodaj()
            elif wybor == 3:
                self.modyfikuj()
            elif wybor == 4:
                self.usuwanie()
            else:
                print("Zla opcja wyboru")
            print("Czy koniec?")
            koniec = input("")
    def wyswietl(self):

        postgreSQL_select_Query = "select * from customers"

        self.cursor.execute(postgreSQL_select_Query)
        customers_records = self.cursor.fetchall()
        for row in customers_records:
            print("customers_Id = ", row[0], )
            print("customers_name = ", row[1])
            print("customers_email = ", row[2])
            print("customers_phone  = ", row[3], "\n")

    def dodaj(self):
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
            self.cursor.execute(postgres_insert_query, i)

            self.connection.commit()
            count = self.cursor.rowcount
        print(count, "Record inserted successfully \
            into publisher table")

    def modyfikuj(self):
        print("Który id chcesz modyfikowac")
        c_id = int(input())
        print("Co chcesz modyfikowac?")
        mod = input()
        if(mod == "name"):
            print("podaj nowy name")
            c_name = input()
            sql_update_query = """Update customers set \
                    name = %s where customers_id = %s"""
            self.cursor.execute(sql_update_query,
                           (c_name,
                            c_id))
        elif(mod == "email"):
            print("podaj nowy email")
            c_email = input()
            sql_update_query = """Update customers set \
                            email = %s where customers_id = %s"""
            self.cursor.execute(sql_update_query,
                           (c_email,
                            c_id))
        elif(mod == "phone"):
            print("podaj nowy phone")
            c_phone = input()
            sql_update_query = """Update customers set \
                                    phone = %s where customers_id = %s"""
            self.cursor.execute(sql_update_query,
                           (c_phone,
                            c_id))
        self.connection.commit()
        count = self.cursor.rowcount
        print(count, "Record Updated successfully ")

    def usuwanie(self):
        print("Ktory rekord usunac?")
        c_id = int(input())
        sql_delete_query = """Delete from customers\
               where customers_id = %s"""
        self.cursor.execute(sql_delete_query, (c_id,))
        self.connection.commit()
        count = self.cursor.rowcount
        print(count, "Record deleted successfully ")


polaczenie = Api()
