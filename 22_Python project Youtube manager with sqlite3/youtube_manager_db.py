import sqlite3
con = sqlite3.connect("youtube_videos.db")
cur = con.cursor()

# ye cursor object query ko execute karnay ka bad apnay pas result hold karta ha 
cur.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')



def list_all_videos():
    cur.execute("SELECT * FROM videos")
    rows = cur.fetchall()
    if not rows:
        print("No videos found.")
    else:
        for row in rows:
            print(f"Id: {row[0]} Name: {row[1]} Duration: {row[2]}")


    

def add_video():
    print("Add video details")
    name = input("Add video name: ")
    duration = input("Add video duration: ")
    cur.execute("INSERT INTO videos(name, time) VALUES(?,?)", (name, duration))
    con.commit()
    

def update_video():
    list_all_videos()
    index = int(input("Enter the video Id no. to update: "))
    name = input("Add video name: ")
    duration = input("Add video duration: ")
    cur.execute("UPDATE videos SET name = ?, time = ?  WHERE id = ?", (name, duration, index))
    con.commit()

    

def delete_video():
    list_all_videos()
    index = int(input("Enter the video Id no. to delete: "))
    cur.execute("DELETE FROM videos  WHERE id = ?", (index,))
    con.commit()

def main():
    while True:
        print("\nYoutube Manager | Choose an option")
        print("1. List all videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case '1':
                list_all_videos()
            case '2':
                add_video()
            case "3": 
                update_video()
            case "4":
                delete_video()
            case "5":
                break
            case _:
                print("Invalid choice")
    
    con.close()

if __name__ == "__main__":
    main()