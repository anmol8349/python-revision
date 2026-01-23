import getpass
import time
import mysql.connector
from datetime import datetime 





DB_CONFIG = {
    
    "host":"localhost",
    "user":"root",
    "password":"@Anmol8349",
    "database":"notes_app"
}


def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print("Database connection failed",e)
        return None



APP_PASSWORD ="1234"

def authenticate():
    for attempt in range(3):
        pwd = getpass.getpass("enter password: ")
        
        if pwd==APP_PASSWORD:
            print("access granted: ")
            return True
        else:
            print("Wrong password")
            if attempt == 2:
                print("Too many attempts. Try again after 10 seconds.")
                time.sleep(10)
        
        return False



def add_note():
    try:
        title = input("Enter tiltle: ").strip()
        content = input("Enter content: ").strip()
        created_at = datetime.now()
        
        conn=get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO notes (title,content,created_at) VALUES (%s,%s,%s)",
            (title,content,created_at)
        )
        
        conn.commit()
        conn.close()
        print("Note add successfully")
        
    except Exception as e:
        print("Error adding note: ",e)







def view_notes():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM notes WHERE deleted = False")
        
        notes =cursor.fetchall()    
        
        conn.close()
        
        if not notes:
            print("no matches found ")
            
        for note in notes:
            print(f"ID: {note['id']} | {note['title']}")
            print(f"Date: {note['created_at']}")
            print(f"Content: {note['content']}")
            print("-" * 40)
            
    except Exception as e:
        print("View error:", e)
        
        
        
        
        
# ======----------------------
        
        
        
        
        
def search_notes():
    try:
        keyword = input("Enter keyword : ").strip()
        if not keyword:
            print("Keyword cannot be empty.")
            return
        
        conn = get_connection()
        
        if not conn:
            print("Database not available.")
            return

        cursor=conn.cursor(dictionary=True)
        
        query = """
        SELECT * FROM notes
        WHERE deleted = FALSE
        AND (title LIKE %s OR content LIKE %s)
        """
        
        cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
        
        results = cursor.fetchall()
        
        conn.close()
        
        if not results:
            print("No match found.")
            return

        for note in results:
            print(note["title"], "-", note["content"])
            
    except Exception as e:
        print("Search error:", e)
        
        
        
        
        
        
#  ----------------------------


def delete_note():
    try:
        note_id = int(input("Enter note ID: "))

        conn = get_connection()
        cursor = conn.cursor()
       
      
        cursor.execute("UPDATE notes SET deleted = TRUE WHERE id = %s", (note_id,))
        conn.commit()
        conn.close()  
        
        print("Note soft-deleted!")

    except Exception as e:
        print("Delete error:", e)
        
        
        
        
# ---------------------------------------------



def undo_delete():
    try:
        note_id = int(input("Enter note ID to restore: "))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE notes SET deleted = FALSE WHERE id = %s", (note_id,))
        conn.commit()
        conn.close()

        print("Note restored!")

    except Exception as e:
        print("Undo error:", e)





# ------------------------------------------------------------------


def edit_note():
    try:
        note_id = int(input("Enter note ID: "))
        new_title = input("New title: ")
        new_content = input("New content: ")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE notes SET title=%s, content=%s WHERE id=%s AND deleted=FALSE",
            (new_title, new_content, note_id)
        )

        conn.commit()
        conn.close()
        print("Note updated!")

    except Exception as e:
        print("Edit error:", e)


# -------------------------------------------------------------------------------------------


def filter_notes():
    try:
        print("1. By Date")
        print("2. By Keyword")
        ch = input("Choose: ")

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        if ch == "1":
            date_str = input("YYYY-MM-DD: ")
            cursor.execute(
                "SELECT * FROM notes WHERE DATE(created_at)=%s AND deleted=FALSE",
                (date_str,)
            )
        else:
            kw = input("Keyword: ")
            cursor.execute(
                "SELECT * FROM notes WHERE deleted=FALSE AND (title LIKE %s OR content LIKE %s)",
                (f"%{kw}%", f"%{kw}%")
            )

        results = cursor.fetchall()
        conn.close()

        for note in results:
            print(note["title"], "-", note["content"])

    except Exception as e:
        print("Filter error:", e)








# ---------------- MENU ----------------
def menu():
    print("\n=== ADVANCED NOTES APP ===")
    print("1. Add Note")
    print("2. View All Notes")
    print("3. Search Note")
    print("4. Delete Note")
    print("5. Edit Note")
    print("6. Undo Delete")
    print("7. Filter Notes")
    print("8. Exit")



def main():
    if not authenticate():
       return


    while True:
        menu()
        choice = input("Enter choice: ")


        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            search_notes()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            edit_note()
        elif choice == '6':
            undo_delete()
        elif choice == '7':
            filter_notes()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")




if __name__ == "__main__":
    main()