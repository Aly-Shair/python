import json

def data_loader():
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def data_saver_helper(videos):
    with open("data.json", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for i, video in enumerate(videos):
        print(f"Sr no. {i} Name: {video['name']} Duration: {video['duration']}")

def add_video(videos):
    print("Add video details")
    name = input("Add video name: ")
    duration = input("Add video duration: ")
    videos.append({"name": name, "duration": duration})
    data_saver_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video Sr no. to update: "))
    name = input("Add video name: ")
    duration = input("Add video duration: ")
    videos[index] = {"name": name, "duration": duration}
    data_saver_helper(videos)

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video Sr no. to delete: "))
    del videos[index]
    data_saver_helper(videos)

def main():
    videos = data_loader()
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
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case "3": 
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()